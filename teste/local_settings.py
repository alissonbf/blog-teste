# -*- coding: utf-8 -*-
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

allowed_hosts = []

settings = {
    'DEBUG': True,
    'TEMPLATE_DEBUG': True,
    'LOCAL': True,
    'ALLOWED_HOSTS': allowed_hosts,

    'DEFAULT_DB_ENGINE': 'django.db.backends.sqlite3',
    'DEFAULT_DB_NAME': os.path.join(BASE_DIR, 'blog_db.sqlite3'),
    'DEFAULT_DB_USER': '',
    'DEFAULT_DB_PASSWORD': '',
    'DEFAULT_DB_HOST': '',

    # S3 Config
    'DEFAULT_FILE_STORAGE': 'storages.backends.s3boto.S3BotoStorage',
    'AWS_S3_SECURE_URLS': False,
    'AWS_QUERYSTRING_AUTH': False,
    'AWS_S3_ACCESS_KEY_ID': 'AKIAJP4KLR4HYQEYCUOQ',
    'AWS_S3_SECRET_ACCESS_KEY': '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',
    'AWS_STORAGE_BUCKET_NAME': 'heimdallbucket',
    'AWS_S3_CUSTOM_DOMAIN': 'heimdallbucket.s3.amazonaws.com',


    'STATIC_URL': '/static/',
    'STATICFILES_STORAGE': 'storages.backends.s3boto.S3BotoStorage',

    'BROKER_URL': 'redis://127.0.0.1:6379/0',
    'BROKER_TRANSPORT': 'redis',
    'CELERYBEAT_SCHEDULER': 'djcelery.schedulers.DatabaseScheduler',
    'CELERY_SEND_EVENTS': True,

    # Apple Config
    "APPLE_SANDBOX_STORE": "https://sandbox.itunes.apple.com/verifyReceipt",
    "APPLE_LIVE_STORE": "https://buy.itunes.apple.com/verifyReceipt",
    "APPLE_SHARED_SECRET": "",
}