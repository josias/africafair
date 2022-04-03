import django_on_heroku
import os


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


# Static files (CSS, JavaScript, Images)
STATIC_ROOT =  [BASE_DIR /'staticfiles',]
STATIC_URL = '/static/'

# Extra places for collecstatic
STATICFILES_DIRS = [BASE_DIR /'static']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# DATABASE CONFIGURATION
# import dj_database_url
#if 'DATABASE_URL' in os.environ:
#    DATABASES = {
#        'default' : dj_database_url.config(),
#    }

DATABASES = {'default': {   'ATOMIC_REQUESTS': False,
                            'AUTOCOMMIT': True,
                            'CONN_MAX_AGE': 600,
                            'ENGINE': 'django.db.backends.postgresql_psycopg2',
                            'HOST': 'ec2-3-209-61-239.compute-1.amazonaws.com',
                            'NAME': 'dum9gs0mf2g7u',
                            'OPTIONS': {'sslmode': 'require'},
                            'PASSWORD': '********************',
                            'PORT': 5432,
                            'TEST': {'CHARSET': None,
                                    'COLLATION': None,
                                    'MIGRATE': True,
                                    'MIRROR': None,
                                    'NAME': None},
                            'TIME_ZONE': None,
                            'USER': 'zzktxuxwbnvjee'
                        }
                }                                            
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

django_on_heroku.settings(locals())