import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from . forms import PaymentForm
from . models import Payment
from . tasks import make_payment, process_payment_success


class PaymentHistory(LoginRequiredMixin, ListView):

	model = Payment
	context_object_name = 'payments'

	def get_queryset(self):
		client_profile = self.request.user.profile
		return Payment.objects.filter(client=client_profile)


class InitiatePayment(LoginRequiredMixin, CreateView):

	model = Payment
	form_class = PaymentForm

	def get_form_kwargs(self, *args, **kwargs):
		kwargs = super(InitiatePayment, self).get_form_kwargs(*args, **kwargs)
		kwargs.update({'request': self.request})
		return kwargs

	def form_valid(self, form):
		self.object = form.save()
		make_payment.delay(self.object.id, self.object.client.id, self.object.payment_type.id)
		return super(ContactView, self).form_valid(form)


class PaymentSent(LoginRequiredMixin, View):

	def get(self, request):
		return render(request, 'payments/payment_sent.html', {})


class PaymentSuccess(View):

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super(PaymentSuccess, self).dispatch(request, *args, **kwargs)

	def post(self, request):
		data = json.loads(request.body.decode('utf-8'))
		process_payment_success.delay(data)
		
		return JsonResponse({'status':'done'})
