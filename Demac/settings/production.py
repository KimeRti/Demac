from .base import *

DEBUG = False

ALLOWED_HOSTS = ['45.147.46.199', 'demacimportexport.com', 'www.demacimportexport.com']
STATIC_ROOT = 'Demac/static/'


DATABASES = {
    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'Demac',

        'USER': 'postgres',

        'PASSWORD': '123',

        'HOST': 'localhost',

        'PORT': '5432',

    }
}