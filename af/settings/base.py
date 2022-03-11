"""
Django settings for af project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
import environ
from pathlib import Path
from datetime import timedelta

env = environ.Env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path('__file__').resolve().parent

# Take environment variables from .env file
environ.Env.read_env(BASE_DIR/'af/settings/.env')

ALLOWED_HOSTS = []
APPEND_SLASH = True
# Application definition

INSTALLED_APPS = [
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'django_countries',
    'import_export',
    'versatileimagefield',
    'phonenumber_field',
    'crispy_forms',
    'rest_framework',
    'guardian',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist', 
    'drjr', 
   # 'drf_spectacular',
    'drf_openapi3.apps.DRFOpenApi3Config',
    'treebeard',
    'accounts.apps.AccountsConfig',
    'fair.apps.FairConfig',
    'products.apps.ProductsConfig',
    'fair_sites.apps.FairSitesConfig',
    'businesses.apps.BusinessesConfig',
    'offers.apps.OffersConfig', 

]

ROOT_URLCONF = 'af.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


#Custom User Model

AUTH_USER_MODEL = "accounts.CustomUser"

LOGIN_REDIRECT_URL = 'fair:home'

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

USE_THOUSAND_SEPARATOR = True


# Django import_export configurations
IMPORT_EXPORT_USE_TRANSACTIONS = True

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

GUARDIAN_MONKEY_PATCH = False
GUARDIAN_GET_INIT_ANONYMOUS_USER = 'accounts.models.get_anonymous_user_instance'
ANONYMOUS_USER_NAME = 'anonymous@af.com'
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'guardian.backends.ObjectPermissionBackend'
)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ],

    'DEFAULT_PERMISSION_CLASSES': [
        'accounts.api.permissions.CustomObjectPermissions',
    ],

  #  'DEFAULT_SCHEMA_CLASS': [
  #      'drf_spectacular.openapi.AutoSchema',
  #  ],

}

SIMPLE_JWT = {
    'REFRESH_TOKEN_LIFETIME': timedelta(days=15),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True
}

# Expiration time in seconds
DJANGO_REST_JWT_REGISTRATION = {
    # Optional - in the form of `app_name.module_name.class_name`
    #'CREATE_USER_SERIALIZER': 'core.serializers.CreateUserSerializer',
    'CREATE_USER_SERIALIZER': 'accounts.api.serializers.CustomUserDRJRSerializer',
    # Optional
    'REGISTRATION_TOKEN_LIFETIME': int(os.getenv('REGISTRATION_TOKEN_LIFETIME', '3600')),
    # Optional
    'REGISTRATION_DELETE_TOKEN_LIFETIME': int(os.getenv('REGISTRATION_DELETE_TOKEN_LIFETIME', '3600')),
    # Optional
    'PASSWORD_CHANGE_TOKEN_LIFETIME': int(os.getenv('PASSWORD_CHANGE_TOKEN_LIFETIME', '3600')),
    # Optional
    'EMAIL_CHANGE_TOKEN_LIFETIME': int(os.getenv('EMAIL_CHANGE_TOKEN_LIFETIME', '3600')),
    # Optional
    'DELETE_EXPIRED_TOKENS_INTERVAL': int(os.getenv('DELETE_EXPIRED_TOKENS_INTERVAL', '60')),
    # Optional
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_PORT = int(env('EMAIL_PORT'))
EMAIL_USE_TLS = bool(env('EMAIL_USE_TLS'))
# EMAIL_USE_SSL = bool(env('EMAIL_USE_SSL'))

# new  line
CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
    'http://127.0.0.1:3000'
]

CSRF_TRUSTED_ORIGINS = [
    'localhost',
    '127.0.0.1'
]

VERSATILEIMAGEFIELD_SETTINGS = {
    # The amount of time, in seconds, that references to created images
    # should be stored in the cache. Defaults to `2592000` (30 days)
    'cache_length': 2592000,
    # The name of the cache you'd like `django-versatileimagefield` to use.
    # Defaults to 'versatileimagefield_cache'. If no cache exists with the name
    # provided, the 'default' cache will be used instead.
    'cache_name': 'versatileimagefield_cache',
    # The save quality of modified JPEG images. More info here:
    # https://pillow.readthedocs.io/en/latest/handbook/image-file-formats.html#jpeg
    # Defaults to 70
    'jpeg_resize_quality': 70,
    # The name of the top-level folder within storage classes to save all
    # sized images. Defaults to '__sized__'
    'sized_directory_name': '__sized__',
    # The name of the directory to save all filtered images within.
    # Defaults to '__filtered__':
    'filtered_directory_name': '__filtered__',
    # The name of the directory to save placeholder images within.
    # Defaults to '__placeholder__':
    'placeholder_directory_name': '__placeholder__',
    # Whether or not to create new images on-the-fly. Set this to `False` for
    # speedy performance but don't forget to 'pre-warm' to ensure they're
    # created and available at the appropriate URL.
    'create_images_on_demand': True,
    # A dot-notated python path string to a function that processes sized
    # image keys. Typically used to md5-ify the 'image key' portion of the
    # filename, giving each a uniform length.
    # `django-versatileimagefield` ships with two post processors:
    # 1. 'versatileimagefield.processors.md5' Returns a full length (32 char)
    #    md5 hash of `image_key`.
    # 2. 'versatileimagefield.processors.md5_16' Returns the first 16 chars
    #    of the 32 character md5 hash of `image_key`.
    # By default, image_keys are unprocessed. To write your own processor,
    # just define a function (that can be imported from your project's
    # python path) that takes a single argument, `image_key` and returns
    # a string.
    'image_key_post_processor': None,
    # Whether to create progressive JPEGs. Read more about progressive JPEGs
    # here: https://optimus.io/support/progressive-jpeg/
    'progressive_jpeg': False
}

VERSATILEIMAGEFIELD_RENDITION_KEY_SETS = {
    'image_gallery': [
        ('gallery_large', 'crop__800x450'),
        ('gallery_square_small', 'crop__50x50')
    ],
    'primary_image_detail': [
        ('hero', 'crop__600x283'),
        ('social', 'thumbnail__800x800')
    ],
    'primary_image_list': [
        ('list', 'crop__400x225'),
    ],
    'headshot': [
        ('headshot_small', 'crop__150x175'),
    ],
    'logo': [
        ('full_size', 'url'),
        ('thumbnail', 'thumbnail__100x100'),
    ]
}


SPECTACULAR_SETTINGS = {
    'TITLE': 'My Fair API',
    'DESCRIPTION': 'World-class discounts market',
    'VERSION': '1.0.0',
    # OTHER SETTINGS
}