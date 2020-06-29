""" Production settings """
import django_heroku
from decouple import config
import dj_database_url
# prod_db  =  dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(prod_db)
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.contrib.gis.db.backends.postgis',
#         'NAME': config('PROD_DB_NAME'),
#         'USER': config('PROD_DB_USER'),
#         'PASSWORD': config('PROD_DB_PASSWORD'),
#         'HOST': config('PROD_DB_HOST'),
#         'PORT': config('PROD_DB_PORT')
#     }
# }

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

# STATIC_URL = '/static/'
# MEDIA_URL = '/media/'
# DEFAULT_FILE_STORAGE = AWS_FILE_STORAGE
# STATICFILES_STORAGE = AWS_STATICFILES_STORAGE
# AWS_ACCESS_KEY_ID = ACCESS_KEY_ID
# AWS_SECRET_ACCESS_KEY = SECRET_ACCESS_KEY
# AWS_STORAGE_BUCKET_NAME = BUCKET_NAME
# AWS_DEFAULT_ACL = DEFAULT_ACL
# AWS_QUERYSTRING_AUTH = QUERYSTRING_AUTH
# STATIC_ROOT = AWS_MEDIA_URL
# MEDIA_ROOT = AWS_STATIC_URL

# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )


# Celery Settings

# BROKER_URL = config('AWS_REDIS_URL')
# CELERY_RESULT_BACKEND = config('AWS_REDIS_URL')
# CELERY_ACCEPT_CONTENT = ['application/json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_TIMEZONE = 'Africa/Nairobi'
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}
# django_heroku.settings(locals())
