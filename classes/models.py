import uuid
from django.db import models
from taggit.managers import TaggableManager
from django.conf import settings


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
    file = models.FileField(upload_to='%Y')
    tags = TaggableManager()
    date_uploaded = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='lesson_owner')
#
#
# class Comment(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='lesson_comment')
#     comment = models.TextField()
#     commenter = models.UUIDField()
