""" Project production settings """

import os
from decouple import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(n4m%0oc_ko7ht@b=bi7!z&qz5r60gq+8zjke*gps%3gs50-_('
# SECRET_KEY = config("SECRET_KEY")


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'django.contrib.gis',
    'django.contrib.sites',
    'taggit'

    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'allauth',
    'allauth.account',
    # 'allauth.socialaccount',
    'rest_auth.registration',
    # 'storages',
    # 'widget_tweaks',
    # 'leaflet',

    'accounts',
    # 'api',
    # 'payments',
    # 'properties',
    'classes',

]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': False,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 'properties.middleware.PropertyMiddleware',
]

WSGI_APPLICATION = 'core.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Nairobi'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Site admins

ADMINS = (
    ('Mohammed Mwijaa', 'mm.mwijaa@gmail.com'),
    ('Oscar Mwongera', 'oscamwongera@gmail.com')
)

# Email Settings

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST_USER = config('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')


# Auth settings

# LOGIN_URL = 'accounts:login'
# LOGIN_REDIRECT_URL = 'properties:home'
# LOGOUT_REDIRECT_URL = 'properties:home'


# Authentication settings
# Custom user model and related all-auth settings

AUTH_USER_MODEL = 'accounts.User'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_EMAIL_VERIFICATION = 'none'
OLD_PASSWORD_FIELD_ENABLED = True
LOGOUT_ON_PASSWORD_CHANGE = True
# EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'accounts.serializers.ProfileSerializer'
}

# Leaflet settings for geodjango admin

LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (-.023, 36.87),
    'DEFAULT_ZOOM': 5,
    'MAX_ZOOM': 20,
    'MIN_ZOOM': 3,
    'SCALE': 'both',
    'ATTRIBUTION_PREFIX': 'Off to the next step #OscaMwongera',
}

# DRF Settings

REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

SITE_ID = 1

# Mpesa Settings

# BUSINESS_SHORT_CODE = config('BUSINESS_SHORT_CODE')
# PHONE_NUMBER = config('PHONE_NUMBER')
# LNM_PASSKEY = config('LNM_PASSKEY')
# CONSUMER_KEY = config('CONSUMER_KEY')
# CONSUMER_SECRET = config('CONSUMER_SECRET')
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )
