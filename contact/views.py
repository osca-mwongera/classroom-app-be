from django.contrib import messages
from django.views.generic.edit import CreateView

from . models import Message
from . forms import MessageForm
from . tasks import send_contact_message


class ContactView(CreateView):
	model = Message
	form_class = MessageForm

	def get_form_kwargs(self, *args, **kwargs):
		kwargs = super(ContactView, self).get_form_kwargs(*args, **kwargs)
		kwargs.update({'request': self.request})

		return kwargs

	def form_valid(self, form):
		self.object = form.save()
		send_contact_message.delay(self.object.id)
		messages.success(self.request, 'Your message was sent successfully')

		return super(ContactView, self).form_valid(form)
