import base64
from datetime import datetime

from celery.utils.log import get_task_logger
from django.conf import settings
from django.utils import timezone
from requests.auth import HTTPBasicAuth
import requests

from accounts.models import Profile
from core.celery import app
from . models import LNMOnline, Payment, PaymentType

logger = get_task_logger(__name__)

consumer_key = settings.CONSUMER_KEY
consumer_secret = settings.CONSUMER_SECRET
bsc = settings.BUSINESS_SHORT_CODE
passkey = settings.LNM_PASSKEY

def generate_password(timestamp):
    data = bsc + passkey + timestamp
    encoded_string = base64.b64encode(data.encode())
    decoded_password = encoded_string.decode('utf-8')

    return decoded_password

def get_timestamp():
    now = timezone.now()
    formatted = now.strftime("%Y%m%d%H%M%S")

    return formatted

@app.task(bind=True, retry_backoff=True)
def generate_access_token(self):
	logger.info('Generating access token...')

	try:
		api_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
		r = requests.get(api_url, auth=HTTPBasicAuth(consumer_key, consumer_secret))
		data = r.json()

		return data['access_token']
	except Exception as e:
		logger.info('Error: %s' % e)
		raise self.retry(exc=e, max_retries=3)

@app.task(bind=True, retry_backoff=True)
def make_payment(self, payment_object_id, client_profile_id, payment_type_id):
	logger.info('Initiating payment request...')

	try:
		customer_profile = Profile.objects.get(pk=client_profile_id)
		payment_type = PaymentType.objects.get(pk=payment_type_id)
		payment = Payment.objects.get(pk=payment_object_id)

		timestamp = get_timestamp()
		password = generate_password(timestamp)
		access_token = generate_access_token()

		api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
		headers = { "Authorization": "Bearer %s" % access_token }
		request = {
	    	"BusinessShortCode": bsc,
			"Password": password,
			"Timestamp": timestamp,
			"TransactionType": "CustomerPayBillOnline",
			"Amount": payment_type.amount, 
			"PartyA": customer_profile.phone_number,
			"PartyB": bsc,
			"PhoneNumber": customer_profile.phone_number,
			"CallBackURL": "https://rafika-api.localtunnel.me/payments/payment-successful/", 
			"AccountReference": 987654,
			"TransactionDesc": payment_type.name, #payment_type.name
		}

		response = requests.post(api_url, json=request, headers=headers)
		data = response.json()
		logger.info('MPESA API Response: %s' % data)

		if 'ResponseCode' in data and int(data['ResponseCode']) == 0:
			checkout_rq_id = data.get('CheckoutRequestID', None)
			merchant_rq_id = data.get('MerchantRequestID', None)

			if checkout_rq_id and merchant_rq_id:
				payment.checkout_request_id = data['CheckoutRequestID']
				payment.merchant_request_id = data['MerchantRequestID']
				payment.status = 'Processing'
				payment.save()
		else:
			payment.status = 'Failed'
			payment.save()
	except Exception as e:
		logger.info('Error: %s' % e)
		raise self.retry(exc=e, max_retries=5)

@app.task(bind=True, retry_backoff=True)
def process_payment_success(self, api_response):
	logger.info('Processing payment confirmation from data: %s' % api_response)

	data = api_response['Body']['stkCallback']
	if 'CheckoutRequestID' in data and 'MerchantRequestID' in data:
		try:
			transaction = LNMOnline()
			transaction.checkout_request_id = data['CheckoutRequestID']
			transaction.merchant_request_id = data['MerchantRequestID']
			transaction.result_code = data['ResultCode']
			transaction.result_desc = data['ResultDesc']

			if 'CallbackMetadata' in data:
				vals = {}
				for i in data['CallbackMetadata']['Item']:
					vals[i['Name']] = i.get('Value', None)

				transaction.amount = vals['Amount']
				transaction.mpesa_receipt_number = vals['MpesaReceiptNumber']
				transaction.phone_number = vals['PhoneNumber']
				transaction.timestamp = timezone.make_aware(datetime.strptime(str(vals['TransactionDate']), '%Y%m%d%H%M%S'))

			transaction.save()

			payment = Payment.objects.get(
				checkout_request_id=data['CheckoutRequestID'],
				merchant_request_id=data['MerchantRequestID']
			)
			payment.transaction = transaction
			payment.save()
		except Exception as e:
			logger.info('Error: %s' % e)
			raise self.retry(exc=e, max_retries=3)
