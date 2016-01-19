from .base import *

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS += [
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DB_DIEGOFORERO'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASS']
    }
}
