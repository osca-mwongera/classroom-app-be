from datetime import timedelta

from celery.utils.log import get_task_logger
from django.core.mail import mail_admins
from django.utils import timezone

from core.celery import app
from . models import Message

logger = get_task_logger(__name__)

@app.task(bind=True, retry_backoff=True, retry_backoff_max=20)
def send_contact_message(self, message_id):
	logger.info('Sending email')

	try:
		m = Message.objects.get(pk=message_id)
		result = mail_admins(m.subject, m.text)
		m.mail_sent = True
		m.save()
	except Exception as e:
		logger.info('Could not send email: %s' %e)
		raise self.retry(exc=e, max_retries=5)

@app.task(bind=True)
def check_unsent_mail(self):
	logger.info('Checking for unsent mail')

	now = timezone.now()
	last = now - timedelta(hours=24)

	try:
		messages = Message.objects.filter(timestamp__range=(last, now), mail_sent=False)
		if messages:
			for m in messages:
				send_contact_message.delay(m.id)

		logger.info('All mail sent')
	except Exception as e:
		logger.info('An error occured: %s' %e)
