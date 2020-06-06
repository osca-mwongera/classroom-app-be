from django import forms
from django.contrib.admin.widgets import RelatedFieldWidgetWrapper
from django.db.models import ManyToOneRel, ManyToManyRel

from accounts.models import Profile
from . models import Property, Category, Facility


class PropertyForm(forms.ModelForm):
	realtor = forms.ModelChoiceField(queryset=None, widget=forms.RadioSelect, empty_label=None)
	slug = forms.CharField(widget=forms.HiddenInput)

	class Meta:
		model = Property
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(PropertyForm, self).__init__(*args, **kwargs)
		realtor_rel = ManyToOneRel(self.instance.realtor, Profile, 'id')
		self.fields['realtor'].widget = RelatedFieldWidgetWrapper(self.fields['realtor'].widget,realtor_rel,self.admin_site)
		self.fields['realtor'].queryset = Profile.objects.filter(is_realtor=True)

		self.fields['facilities'].required = False
		self.fields['slug'].required = False

	def clean_realtor(self):
		realtor = self.cleaned_data['realtor']
		if not realtor.is_realtor:
			raise forms.ValidationError('The chosen caretaker should have a realtor profile')

		return realtor


		
