from .base import *

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'smart_task',
        'USER': 'smart_task_user',
        'PASSWORD': 'pass@123!@#',
        'HOST': 'localhost',
        'PORT': '',
    }
}

DEBUG = True