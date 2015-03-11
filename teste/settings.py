# -*- coding: utf-8 -*-
"""
Django settings for teste project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))


try:
    import teste.local_settings as local_settings_module
    lsettings = local_settings_module.settings
except:
    lsettings = {}

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n$u6)vg7q=-)i31ah@t@r_+l3+7qberihrvi$tgu28!!i@c=kr'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = lsettings.get('DEBUG', True)

LOCAL = lsettings.get('LOCAL', False) # Marca se o projeto esta em desenvolvimento

TEMPLATE_DEBUG = lsettings.get('TEMPLATE_DEBUG', True)

ALLOWED_HOSTS = lsettings.get('ALLOWED_HOSTS', ['*'])


# Application definition

INSTALLED_APPS = (
    # Pacotes de terceiros
    'grappelli.dashboard',
    'grappelli',
    #'filebrowser',
    'storages',

    # Pacotes do django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Pacotes de terceiros
    'pycard',
    'haystack',
    'whoosh',
    'djcelery',
    'rest_framework',

    # Pacotes alisson
    'blog',
    'card',
    'galeria',
    'apple',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)


ROOT_URLCONF = 'teste.urls'

WSGI_APPLICATION = 'teste.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': lsettings.get('DEFAULT_DB_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': lsettings.get('DEFAULT_DB_NAME', os.path.join(BASE_DIR, 'blog_db.sqlite3')),
    }
}

# Utiliza o sqlite em testes para agilizar
if 'test' in sys.argv:
    DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3'}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Configuração das urls de login e logout
LOGIN_REDIRECT_URL  = '/'
LOGIN_URL           = '/entrar/'
LOGOUT_URL          = '/sair/'

# Configuração do Boto
AWS_STORAGE_BUCKET_NAME = lsettings.get('AWS_STORAGE_BUCKET_NAME', '')
AWS_ACCESS_KEY_ID = lsettings.get('AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = lsettings.get('AWS_SECRET_ACCESS_KEY', '')

# Tell django-storages that when coming up with the URL for an item in S3 storage, keep
# it simple - just use this domain plus the path. (If this isn't set, things get complicated).
# This controls how the `static` template tag from `staticfiles` gets expanded, if you're using it.
# We also use it in the next setting.
AWS_S3_CUSTOM_DOMAIN = lsettings.get('AWS_S3_CUSTOM_DOMAIN', '')

# This is used by the `static` template tag from `static`, if you're using that. Or if anything else
# refers directly to STATIC_URL. So it's safest to always set it.
STATIC_URL = lsettings.get('STATIC_URL', '')

# Tell the staticfiles app to use S3Boto storage when writing the collected static files (when
# you run `collectstatic`).
STATICFILES_STORAGE = lsettings.get('STATICFILES_STORAGE', 'storages.backends.s3boto.S3BotoStorage')

DEFAULT_FILE_STORAGE = lsettings.get('DEFAULT_FILE_STORAGE', 'storages.backends.s3boto.S3BotoStorage')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATIC_ROOT = os.path.join(PROJECT_PATH, 'static')

STATICFILES_DIRS = (
    ('site', os.path.join(PROJECT_PATH, 'sitestatic')),
)

# Arquivos enviados pelo usuario via upload

MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')

MEDIA_URL = '/media/'

# Localização dos templates do projeto

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates'),
)

# Configuração do Grappelli
GRAPPELLI_ADMIN_TITLE = "Blog Teste"
GRAPPELLI_INDEX_DASHBOARD = 'teste.somefile.CustomIndexDashboard'

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    },
}

#Celery Config
BROKER_URL = lsettings.get('BROKER_URL', 'redis://127.0.0.1:6379/0')
BROKER_TRANSPORT = lsettings.get('BROKER_TRANSPORT', 'redis')
CELERYBEAT_SCHEDULER = lsettings.get('CELERYBEAT_SCHEDULER', 'djcelery.schedulers.DatabaseScheduler')
# needed for worker monitoring
CELERY_SEND_EVENTS = lsettings.get('CELERY_SEND_EVENTS', True)

# Apple Config
APPLE_SHARED_SECRET = lsettings.get('APPLE_SHARED_SECRET', '')
APPLE_SANDBOX_STORE = lsettings.get('APPLE_SANDBOX_STORE', 'https://sandbox.itunes.apple.com/verifyReceipt')
APPLE_LIVE_STORE = lsettings.get('APPLE_LIVE_STORE', 'https://buy.itunes.apple.com/verifyReceipt')

#Celerycam fix
import djcelery
djcelery.setup_loader()

SENDSMS_BACKEND = 'sendsms.backends.smspubli.SmsBackend'

# Configuração do File Browser
"""
FILEBROWSER_VERSIONS_BASEDIR = '_versions'
FILEBROWSER_DIRECTORY = 'uploads/'
FILEBROWSER_EXTENSIONS = {
    'Folder': [''],
    'Image': ['.jpg','.jpeg','.gif','.png','.tif','.tiff'],
    'Document': ['.pdf','.doc','.docx','.rtf','.txt','.xls','.csv'],
    'Video': ['.mov','.wmv','.mpeg','.mpg','.avi','.rm','.mp4'],
    'Audio': ['.mp3','.wav','.aiff','.midi','.m4p']
}
FILEBROWSER_MAX_UPLOAD_SIZE = 10485760
FILEBROWSER_NORMALIZE_FILENAME = True
FILEBROWSER_OVERWRITE_EXISTING = False


from filebrowser.sites import site

# Image actions
from teste.actions import make_monochrome, flv_to_mp4
site.add_action(make_monochrome)
site.add_action(flv_to_mp4)
"""

# Configuração de logs
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(PROJECT_PATH, 'logs/debug.log'),
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}