import django_heroku
import os
import dj_database_url

from af.settings.base import *

DEBUG = os.environ['DEBUG']

# ALLOWED_HOSTS = [
#    'localhost',
#    '0.0.0.0',
#    'fair-bkd-cachalot.herokuapp.com',
#]

ALLOWED_HOSTS = [
    '127.0.0.1',
    '.herokuapp.com',
]

SECRET_KEY = os.environ['SECRET_KEY']

INSTALLED_APPS.insert(0, 'whitenoise.runserver_nostatic')

# MIDDLEWARE_CLASSES = (
    # Simplified static file serving.
    # https://warehouse.python.org/project/whitenoise/
#    'whitenoise.middleware.WhiteNoiseMiddleware',
#)

MIDDLEWARE = [
    # Simplified static file serving.
    # https://warehouse.python.org/project/whitenoise/
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',    
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

# Static files (CSS, JavaScript, Images)
STATIC_ROOT =  [BASE_DIR /'staticfiles',]
STATIC_URL = '/static/'

# Extra places for collecstatic
STATICFILES_DIRS = [BASE_DIR /'static']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        
    }
}

DATABASES['default'] =  dj_database_url.config(conn_max_age=600, ssl_require=True)
                                            

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('%(asctime)s [%(process)d] [%(levelname)s] '
                       'pathname=%(pathname)s lineno=%(lineno)s '
                       'funcname=%(funcName)s %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}

django_heroku.settings(locals())