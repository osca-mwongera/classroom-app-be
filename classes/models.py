import uuid
from django.db import models
from taggit.managers import TaggableManager


# Create your models here.
class Lesson(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    audience = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    comments_enabled = models.BooleanField()
    file = models.FileField(upload_to='')
    tags = TaggableManager()
    date_uploaded = models.DateField(auto_now_add=True)
    owner = models.UUIDField()


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='lesson_comment')
    comment = models.TextField()
    commenter = models.UUIDField()
