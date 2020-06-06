from datetime import timedelta

from django.utils import timezone
from storages.backends.s3boto3 import S3Boto3Storage

StaticRootS3BotoStorage = lambda: S3Boto3Storage(location='static')
MediaRootS3BotoStorage  = lambda: S3Boto3Storage(location='media')

def set_expiry():
	later = timezone.now() + timedelta(days=60)
	return later.strftime("%A, %d %B %Y 20:00:00 GMT")
