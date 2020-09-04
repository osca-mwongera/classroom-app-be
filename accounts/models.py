from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
import uuid
from django.contrib.auth.models import PermissionsMixin

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Unspecified', 'Leave Unspecified')
)


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(verbose_name='email address', blank=False, max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        name_str = self.email.split('@')[0]
        if self.first_name and self.last_name:
            name_str = self.get_full_name()

        self.username = name_str
        super(User, self).save()


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/%Y%m%d')
    phone_number = models.CharField(max_length=13)
    is_tutor = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        profile_str = 'Profile: %s ~ %s' % (self.fullname, self.phone_number)
        if self.is_tutor:
            profile_str = profile_str.replace('Profile', 'Tutor')
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
