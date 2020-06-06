from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

GENDER_CHOICES = (
	('Male', 'Male'),
	('Female', 'Female'),
	('Unspecified', 'Leave Unspecified')
)


class User(AbstractUser):
	email = models.EmailField(unique=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	def __str__(self):
		return self.username

	def save(self, *args, **kwargs):
		name_str = self.email.split('@')[0]
		if self.first_name and self.last_name:
			name_str = self.get_full_name()

		self.username = slugify(name_str)
		super(User, self).save()


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	avatar = models.ImageField(upload_to='avatars/%Y/%m/%d')
	gender = models.CharField(max_length=25, choices=GENDER_CHOICES)
	phone_number = models.CharField(max_length=13)

	alt_phone = models.CharField(max_length=13, null=True)
	address = models.CharField(max_length=99, null=True)
	zip_code = models.CharField(max_length=5, null=True)
	town = models.CharField(max_length=99, null=True)
	region = models.CharField(max_length=99, null=True)
	is_realtor = models.BooleanField(default=False)

	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		profile_str = 'Profile: %s ~ %s' %(self.fullname, self.phone_number)
		if self.is_realtor:
			profile_str = profile_str.replace('Profile', 'Realtor')
		return profile_str

	@property
	def fullname(self):
		return self.user.get_full_name()

	@property
	def email(self):
		return self.user.email
	

	@receiver(post_save, sender=User)
	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			Profile.objects.create(user=instance)

	@receiver(post_save, sender=User)
	def save_user_profile(sender, instance, **kwargs):
		instance.profile.save()
		