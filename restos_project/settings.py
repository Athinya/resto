"""
Django settings for restos_project project.

Generated by 'django-admin startproject' using Django 5.0.9.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIRs / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-m4&jr^2z0j#s-+c-(yh0do*aer8h%k)wq^)72=9r^(#vo-pk=i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "buypk8.ddns.net",  # Allow buypk8.ddns.net for all ports
    "localhost",        # Optionally include localhost for testing
    "127.0.0.1",        # Include localhost IP if needed
    "::1"  ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'corsheaders',
    'rest_framework',
    'restos_app',
]

MIDDLEWARE = [
    # 'restos_app.middleware.CustomCorsMiddleware',  # Add your custom middleware here
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# CORS_ALLOWED_ORIGINS = [
#     "http://buypk8.ddns.net",
#     "https://buypk8.ddns.net",
#     "www.buypk8.ddns.net",
#     "1",
#     "127.0.0.1", 

# ]

# CORS_ALLOW_CREDENTIALS = True  # Uncomment if necessary
# CORS_ALLOW_ALL_ORIGINS = True  # Use for testing, change in production

# CORS_ALLOW_METHODS = [
#     "GET",
#     "POST",
#     "PUT",
#     "PATCH",
#     "DELETE",
#     "OPTIONS",
# ]

# CORS_ALLOW_HEADERS = [
#     "Authorization",
#     "Content-Type",
#     "access-control-allow-origin",
#     "X-CSRFToken",
# ]
ROOT_URLCONF = 'restos_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'restos_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'Testing',
        'USER': 'logsr',
        'PASSWORD': '1234',
        'HOST': '103.48.180.245',  # Use 'localhost' for local development
        'PORT': '1433',  # Default MSSQL port
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',  # Make sure to have the correct ODBC driver installed
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
