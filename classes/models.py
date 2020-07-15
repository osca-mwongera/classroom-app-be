import os
import uuid

from django.conf import settings
from django.db import models
from django.dispatch import receiver
from taggit.managers import TaggableManager


# Create your models here.
class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)


class Lesson(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='lesson_category')
    name = models.CharField(max_length=255)
    description = models.TextField()
    comments_enabled = models.BooleanField(default=True)
    file = models.FileField(upload_to='uploads/%Y')
    tags = TaggableManager(blank=True)
    date_uploaded = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='lesson_owner')


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='lesson_comment')
    comment = models.TextField()
    commenter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='lesson_commenter')
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


@receiver(models.signals.post_delete, sender=Lesson)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)


@receiver(models.signals.pre_save, sender=Lesson)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.id:
        return False

    try:
        old_file = sender.objects.get(id=instance.id).file
    except sender.DoesNotExist:
        return False

    new_file = instance.file
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
