from .base import *  #noqa

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env.str('POSTGRES_DB', 'django_intro_local'),
        'USER': env.str('POSTGRES_USER', 'django_intro'),
        'PASSWORD': env.str('POSTGRES_PASSWORD', 'django_intro'),
        'HOST': env.str('DB_HOST', 'postgres'),
        'PORT': env.int('DB_PORT', 5432),
    }
}
