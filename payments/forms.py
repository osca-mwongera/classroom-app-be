from django import forms

from . models import Payment
from properties.models import Property

class PaymentForm(forms.ModelForm):

	class Meta:
		model = Payment
		fields = ['payment_type', 'property_item', 'client']

	def __init__(self, *args, **kwargs):
		self.request = kwargs.pop('request')
		property_id = self.request.GET.get('property_id')
		super(PaymentForm, self).__init__(*args, **kwargs)
		self.fields['property_item'].initial = Property.objects.get(pk=property_id)
		self.fields['property_item'].widget = forms.HiddenInput()
		self.fields['client'].initial = self.request.user.profile
