from django import forms

from . models import Message


class MessageForm(forms.ModelForm):
	sender = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Your Name'}))
	email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder':'Your Email'}))
	subject = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'Subject (Optional)'}))
	text = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder':'Your Message'}))

	class Meta:
		model = Message
		exclude = ['mail_sent']

	def __init__(self, *args, **kwargs):
		self.request = kwargs.pop('request')
		super(MessageForm, self).__init__(*args, **kwargs)
		if self.request.user.is_authenticated:
			self.fields['sender'].initial = self.request.user.get_full_name()
			self.fields['email'].initial = self.request.user.email
