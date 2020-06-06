import datetime

ACCESS_KEY_ID = 'AKIAYPFFQW6J5BA5KJMM'
SECRET_ACCESS_KEY = '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'
STORAGE_BUCKET_NAME = 'rafika-files'

S3_REGION_NAME = 'us-east-2'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage' 
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage' 
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % STORAGE_BUCKET_NAME

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=604800',
}

AWS_STATIC_URL = AWS_S3_CUSTOM_DOMAIN + 'static/'
AWS_MEDIA_URL = AWS_S3_CUSTOM_DOMAIN + 'media/'
ADMIN_MEDIA_PREFIX = AWS_STATIC_URL + 'admin/'
MEDIA_ROOT = AWS_MEDIA_URL

AWS_FILE_STORAGE = 'core.aws.utils.MediaRootS3BotoStorage'
AWS_STATICFILES_STORAGE = 'core.aws.utils.StaticRootS3BotoStorage'
DEFAULT_ACL = None



# AWS_FILE_EXPIRE = 200
# AWS_PRELOAD_METADATA = True
# AWS_QUERYSTRING_AUTH = True

# S3DIRECT_REGION = 'eu-west-2'
# S3_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME


# ACCESS_KEY_ID = "AKIA4QOX2GHBPLUULYGS"
# SECRET_ACCESS_KEY = "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"
# BUCKET_NAME = 'rafika-heroku'
# S3_URL = '//%s.s3.amazonaws.com/' % BUCKET_NAME
# AWS_MEDIA_URL = S3_URL + 'media/'
# AWS_STATIC_URL = S3_URL + 'static/'
# ADMIN_MEDIA_PREFIX = AWS_STATIC_URL + 'admin/'
# QUERYSTRING_AUTH = False


# AWS_FILE_EXPIRE = 200
# AWS_PRELOAD_METADATA = True
# S3DIRECT_REGION = 'us-east-2'

# two_months = datetime.timedelta(days=61)
# date_two_months_later = datetime.date.today() + two_months
# expires = set_expiry()

# AWS_HEADERS = {
#     'Expires': expires,
#     'Cache-Control': 'max-age=%d' % (int(two_months.total_seconds()), ),
# }

