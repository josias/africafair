import django_heroku
import os
import dj_database_url

from af.settings.base import *

DEBUG = False

ALLOWED_HOSTS = [
    'localhost',
    '0.0.0.0',
    'africafair-backend.herokuapp.com',
]

SECRET_KEY = os.environ['SECRET_KEY']



MIDDLEWARE_CLASSES = (
    # Simplified static file serving.
    # https://warehouse.python.org/project/whitenoise/
    'whitenoise.middleware.WhiteNoiseMiddleware',
)

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
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

DATABASES = {'default' : dj_database_url.config(conn_max_age=600, ssl_require=True)}


django_heroku.settings(locals())