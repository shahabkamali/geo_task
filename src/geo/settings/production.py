from .base import *
from .config import *


DEBUG = False

ALLOWED_HOSTS = []

SECRET_KEY = os.environ.get('SECRET_KEY', None)

DB_PASS = os.environ.get('DB_PASS', None)


if not SECRET_KEY:
    raise Exception('Add SECRET_KEY env variable, example: export SECRET_KEY=123456')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'geodb',
        'USER': 'geo',
        'PASSWORD': DB_PASS,
        'HOST': 'localhost',
        'PORT': '',
    }
}
