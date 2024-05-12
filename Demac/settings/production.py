from .base import *

DEBUG = True

ALLOWED_HOSTS = ['demacimportexport.com', 'www.demacimportexport.com']
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

CSRF_TRUSTED_ORIGINS = ['http://www.demacimportexport.com', 'http://demacimportexport.com', 'https://www.demacimportexport.com', 'https://demacimportexport.com']
CORS_ALLOWED_ORIGINS = ['http://www.demacimportexport.com', 'http://demacimportexport.com', 'https://www.demacimportexport.com', 'https://demacimportexport.com']
CORS_ALLOWED_ORIGIN_REGEXES = ['http://www.demacimportexport.com', 'http://demacimportexport.com', 'https://www.demacimportexport.com', 'https://demacimportexport.com']
CORS_ALLOW_ALL_ORIGINS = ['http://www.demacimportexport.com', 'http://demacimportexport.com', 'https://www.demacimportexport.com', 'https://demacimportexport.com']


DATABASES = {
    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'demac',

        'USER': 'kimerti',

        'PASSWORD': 'kimerti123',

        'HOST': 'localhost',

        'PORT': '5432',

    }
}