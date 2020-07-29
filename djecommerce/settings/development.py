from .base import *

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': '',
        }
}

STRIPE_PUBLIC_KEY = 'rtgtg'
STRIPE_SECRET_KEY = 'defrg'
