""" Production settings """
import django_heroku
import dj_database_url
from rest_framework.settings import api_settings

from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ['https://classroom-be.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'accounts2',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
DATABASES['default']['CONN_MAX_AGE'] = 500

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

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# Activate Django-Heroku.
django_heroku.settings(locals())
