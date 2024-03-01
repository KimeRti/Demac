from .base import *

DEBUG = True

ALLOWED_HOSTS = []

STATICFILES_DIRS = [
     os.path.join(BASE_DIR, 'static/')
     ]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase', 
    }
}