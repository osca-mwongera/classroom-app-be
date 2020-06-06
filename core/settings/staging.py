""" Heroku staging settings """

import os

import dj_database_url

from . base import *
from core.aws.conf import *

# Quick start settings
# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True
ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config()
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = AWS_STATIC_URL
MEDIA_ROOT = AWS_MEDIA_URL

DEFAULT_FILE_STORAGE = AWS_FILE_STORAGE
STATICFILES_STORAGE = AWS_STATICFILES_STORAGE
AWS_ACCESS_KEY_ID = ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = SECRET_ACCESS_KEY
AWS_STORAGE_BUCKET_NAME = STORAGE_BUCKET_NAME
AWS_S3_REGION_NAME = S3_REGION_NAME
AWS_DEFAULT_ACL = DEFAULT_ACL

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# AWS_QUERYSTRING_AUTH = QUERYSTRING_AUTH



# Celery Settings

BROKER_URL = os.environ['REDIS_URL']
CELERY_RESULT_BACKEND = os.environ['REDIS_URL']
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Africa/Nairobi'

# Django debug toolbar settings
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html

# INSTALLED_APPS += [ 'debug_toolbar', ]
# MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')

# def show_toolbar(request):
#     return request.user.is_superuser

# DEBUG_TOOLBAR_CONFIG = {
#     'SHOW_TOOLBAR_CALLBACK': 'core.settings.staging.show_toolbar',
# }

# DEBUG_TOOLBAR_PANELS = [
#     'debug_toolbar.panels.versions.VersionsPanel',
#     'debug_toolbar.panels.timer.TimerPanel',
#     'debug_toolbar.panels.settings.SettingsPanel',
#     'debug_toolbar.panels.headers.HeadersPanel',
#     'debug_toolbar.panels.request.RequestPanel',
#     'debug_toolbar.panels.sql.SQLPanel',
#     'debug_toolbar.panels.staticfiles.StaticFilesPanel',
#     'debug_toolbar.panels.templates.TemplatesPanel',
#     'debug_toolbar.panels.cache.CachePanel',
#     'debug_toolbar.panels.signals.SignalsPanel',
#     'debug_toolbar.panels.logging.LoggingPanel',
#     'debug_toolbar.panels.redirects.RedirectsPanel',
#     'debug_toolbar.panels.profiling.ProfilingPanel',
# ]
