from django.db import models
from django.urls import reverse


class Message(models.Model):
	sender = models.CharField(max_length=100)
	subject = models.CharField(max_length=50, blank=True)
	email = models.EmailField()
	text = models.CharField(max_length=350)
	mail_sent = models.BooleanField(default=False)

	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return 'Message from %s - %s' %(self.sender, self.timestamp)

	def get_absolute_url(self):
		return reverse('contact:contact-us')

	def save(self, *args, **kwargs):
		if not self.subject:
			self.subject = 'New Message From %s' % self.sender
		super(Message, self).save(*args, **kwargs)
