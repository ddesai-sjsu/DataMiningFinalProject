"""
Django settings for h1bprediction project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import pickle
import os
import sklearn
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-s0^xiugudkyj&piaeqcuj7ygfre-#8gcd_d(40%v-dc6v-rkod'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'h1bpredictor'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'h1bprediction.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'h1bprediction.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
ML_URL = os.path.join(BASE_DIR, 'h1bprediction/static/')
NN_MODEL = pickle.load(open(ML_URL+'Nearest Neighbors', 'rb'))
EMP_NAME_LE = pickle.load(open(ML_URL+'EMPLOYER_NAME_le', 'rb'))
EMP_STATE_LE = pickle.load(open(ML_URL+'EMPLOYER_STATE_le', 'rb'))
NAICS_CODE_LE = pickle.load(open(ML_URL+'NAICS_CODE_le', 'rb'))
SOC_CODE_LE = pickle.load(open(ML_URL+'SOC_CODE_le', 'rb'))
WORKSTATE_LE=pickle.load(open(ML_URL+'WORKSITE_STATE_le', 'rb'))


EMP_NAMES_FILE = open(ML_URL+"EMPLOYER_NAME.txt", "r")
EMP_NAMES_LIST = EMP_NAMES_FILE.read().split('\n')
EMP_NAMES_LIST.sort()
EMP_NAMES_CHOICES = [(i,i) for i in EMP_NAMES_LIST]

EMP_STATE_FILE = open(ML_URL+"EMPLOYER_STATE.txt", "r")
EMP_STATE_LIST = EMP_STATE_FILE.read().split('\n')
EMP_STATE_LIST.sort()
EMP_STATE_CHOICES = [(i,i) for i in EMP_STATE_LIST]

NAICS_CODE_FILE = open(ML_URL+"NAICS_CODE.txt", "r")
NAICS_CODE_LIST = NAICS_CODE_FILE.read().split('\n')
NAICS_CODE_CHOICES = [(i,i) for i in NAICS_CODE_LIST]

SOC_CODE_FILE = open(ML_URL+"SOC_CODE.txt", "r")
SOC_CODE_LIST = SOC_CODE_FILE.read().split('\n')
SOC_CODE_CHOICES = [(i,i) for i in SOC_CODE_LIST]

WORKSITE_STATE_FILE = open(ML_URL+"WORKSITE_STATE.txt", "r")
WORKSITE_STATE_LIST = WORKSITE_STATE_FILE.read().split('\n')
WORKSITE_STATE_CHOICES = [(i,i) for i in WORKSITE_STATE_LIST]