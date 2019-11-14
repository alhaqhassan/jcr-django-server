"""
Django settings for __jcr__ project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from .secret import SECRET

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRET['SERVER']['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = SECRET['SERVER']['DEBUG']

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'admin_reorder',

    'core',
    'seeker',
    'employer',
    'admin_auto_filters',
    'import_export',
    'partner'

]

MIDDLEWARE = [
    'django_hosts.middleware.HostsRequestMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'admin_reorder.middleware.ModelAdminReorder',
    # 'core.middleware.DelayMiddleware',
    'django_hosts.middleware.HostsResponseMiddleware'
]

ROOT_URLCONF = '__jcr__.urls'
ROOT_HOSTCONF = '__jcr__.hosts'
DEFAULT_HOST = 'dev'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = '__jcr__.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': SECRET['DB']['NAME'],
        'USER': SECRET['DB']['USER'],
        'PASSWORD': SECRET['DB']['PASSWORD'],
        'HOST': SECRET['DB']['HOST'],

    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Rest framework conf
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DATE_INPUT_FORMATS': [
        '%Y-%m-%dT%H:%M:%S.000Z',  # Trying this because of ant.design
        '%Y-%m-%dT%H:%M:%S.%Z',
        '%Y-%m-%dT%H:%M:%S.%f%z',
        'iso-8601']
}

ADMIN_REORDER = [
    {
        'app': 'auth',
        'label': 'Permission management',
        'models': (
            'auth.Group',
            {'model': 'auth.User', 'label': 'Users'},
        ),
    }, {
        'app': 'employer',
        'label': 'Employer',
        'models': (
            {'model': 'employer.Organisation', 'label': 'Organisation'},
            {'model': 'employer.Employer', 'label': 'Employer Accounts'},
            {'model': 'core.Job', 'label': 'Jobs Available'},
            {'model': 'core.JobTitle', 'label': 'Jobs Title'},

        )
    }, {
        'app': 'seeker',
        'label': 'Seeker',
        'models': (
            {'model': 'seeker.Seeker', 'label': 'Seekers'},
            {'model': 'core.JobApplication', 'label': 'Job Application'},
        )
    }, {
        'app': 'partner',
        'label': 'Partner',
        'models': (
            {'model': 'partner.Partner', 'label': 'Partners'},
        )
    },
]

CORS_ORIGIN_WHITELIST = SECRET['REACT_APPLICATIONS']

if SECRET['SERVER']['PRODUCTION']:
    INSTALLED_APPS += [
        'storages'
    ]

    S3 = SECRET['AWS']['S3']

    AWS_ACCESS_KEY_ID = SECRET['AWS']['USER']['ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = SECRET['AWS']['USER']['SECRET_ACCESS_KEY']
    AWS_STORAGE_BUCKET_NAME = S3['BUCKET_NAME']
    AWS_QUERYSTRING_AUTH = True
    STATICFILES_STORAGE = '__jcr__.s3.StaticStorage'
    DEFAULT_FILE_STORAGE = '__jcr__.s3.MediaStorage'
    AWS_S3_SIGNATURE_VERSION = 's3v4'
    AWS_S3_REGION_NAME = S3['REGION']
    AWS_S3_CUSTOM_DOMAIN = SECRET['AWS']['CDN']['PRIMARY']
    # AWS_DEFAULT_ACL = None

    # STATIC_URL = f'http://{AWS_S3_CUSTOM_DOMAIN}/{S3["STATIC_FOLDER"]}'
    # MEDIA_URL = f'http://{AWS_S3_CUSTOM_DOMAIN}/{S3["MEDIA_FOLDER"]}'
