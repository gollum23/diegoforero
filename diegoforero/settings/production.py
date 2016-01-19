from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['.diegoforero.xyz']

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
