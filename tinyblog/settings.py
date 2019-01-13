# -*- coding: utf-8 -*-
"""
Django settings for myblog project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
from ast import literal_eval as b_eval
import os
from django.contrib.messages import constants as messages

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR = os.path.dirname(os.path.abspath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = b_eval(os.environ.get("DEBUG", "False").title())
ALLOWED_HOSTS = []

SITE_ID = 1
# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.sitemaps",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django_extensions",
    "haystack",
    "taggit",
    "accounts",
    "analytics",
    "blog",
    "robots",
    "gunicorn",
    "meta",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "tinyblog.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "loaders": [
                (
                    "django.template.loaders.cached.Loader",
                    (
                        "django.template.loaders.filesystem.Loader",
                        "django.template.loaders.app_directories.Loader",
                    ),
                )
            ],
        },
    }
]


# Set the path where you will place your custom templates.
# Please use same name so that you don't need to change anything when upgrading
CUSTOM_TEMPLATES = os.path.join(os.path.dirname(BASE_DIR), "custom_dir/templates")

# Insert into the template list if CUSTOM_TEMPLATES exists
if os.path.exists(CUSTOM_TEMPLATES):
    TEMPLATES[0]["DIRS"].append(CUSTOM_TEMPLATES)


WSGI_APPLICATION = "tinyblog.wsgi.application"
# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["BLOG_DATABASE_NAME"],
        "USER": os.environ["BLOG_DATABASE_USER"],
        "PASSWORD": os.environ["BLOG_DATABASE_PASSWORD"],
        "CONN_MAX_AGE": None,
    }
}


SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor",
            "IGNORE_EXCEPTIONS": True,
        },
        "KEY_PREFIX": "blog",
    }
}

DJANGO_REDIS_IGNORE_EXCEPTIONS = True
DJANGO_REDIS_LOG_IGNORED_EXCEPTIONS = True

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Europe/Dublin"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATICFILES_DIRS = [os.path.join(DIR, "assets/")]

CATEGORIES_IN_DETAIL = b_eval(os.environ.get("CATEGORIES_IN_DETAIL", "true").title())

# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
STATIC_URL = "/static/"
MEDIA_URL = "/media/"
STATIC_ROOT = os.path.join(DIR, "static")
MEDIA_ROOT = os.path.join(DIR, "media")

# Set the path where you will place your custom static.
# Please use same name so that you don't need to change anything when upgrading
CUSTOM_STATIC = os.path.join(os.path.dirname(BASE_DIR), "custom_dir/static")

if os.path.exists(CUSTOM_STATIC):
    # Insert into the STATICFILES_DIR list if CUSTOM_STATIC exists
    STATICFILES_DIRS.append(("custom", CUSTOM_STATIC))

SITE_LOGO = os.environ.get("SITE_LOGO", "image/py.png")

#  django-taggit settings
TAGGIT_CASE_INSENSITIVE = True


HAYSTACK_CONNECTIONS = {
    "default": {
        "ENGINE": "haystack.backends.whoosh_backend.WhooshEngine",
        "PATH": os.path.join(os.path.dirname(__file__), "whoosh_index"),
    }
}

HAYSTACK_SIGNAL_PROCESSOR = "haystack.signals.RealtimeSignalProcessor"

#  return empty on next and previous page is page is 1
EMPTY_ON_1 = True


if DEBUG:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


MESSAGE_TAGS = {
    messages.DEBUG: "alert-info",
    messages.INFO: "alert-info",
    messages.SUCCESS: "alert-success",
    messages.WARNING: "alert-warning",
    messages.ERROR: "alert-danger",
}

# template
# set to true if you want you index page to be different from you list of blogs page
HAS_INDEX_PAGE = b_eval(os.environ.get("HAS_INDEX_PAGE", "False").title())
INDEX_TEMPLATE = os.environ.get(
    "INDEX_TEMPLATE", "index.html"
)  # Path to your index template


# Django Meta
META_SITE_PROTOCOL = os.environ.get("META_SITE_PROTOCOL", "http")
META_SITE_DOMAIN = os.environ.get("META_SITE_DOMAIN", "blog.example.com")
META_SITE_NAME = os.environ.get("META_SITE_NAME")
META_USE_OG_PROPERTIES = b_eval(
    os.environ.get("META_USE_OG_PROPERTIES", "False").title()
)
META_USE_TWITTER_PROPERTIES = b_eval(
    os.environ.get("META_USE_TWITTER_PROPERTIES", "False").title()
)
META_USE_GOOGLEPLUS_PROPERTIES = b_eval(
    os.environ.get("META_USE_GOOGLEPLUS_PROPERTIES", "False").title()
)

DEFAULT_META_DESCRIPTION = os.environ.get("DEFAULT_META_DESCRIPTION", "")
DEFAULT_META_KEYWORDS = os.environ.get("DEFAULT_META_KEYWORDS", "")
DEFAULT_META_TITLE = os.environ.get("DEFAULT_META_TITLE", "")


if b_eval(os.environ.get("ENABLE_CELERY", "false").title()):
    CELERY_BROKER_URL = os.environ.get("BROKER_URL", "redis://localhost:6379")
    CELERY_RESULT_BACKEND = os.environ.get("RESULT_BACKEND", "redis://localhost:6379")
    CELERY_ACCEPT_CONTENT = ["application/json"]
    CELERY_RESULT_SERIALIZER = "json"
    CELERY_TASK_SERIALIZER = "json"
    CELERY_TIMEZONE = TIME_ZONE
    CELERY_BEAT_SCHEDULE = {}


# Do not place any settings bellow this setting.
# Define all your custom settings in the custom_settings.py
# file next to the settings.py file.
CUSTOM_SETTINGS = os.path.join(DIR, "custom_settings.py")
if os.path.exists(CUSTOM_SETTINGS):
    from .custom_settings import *

DEFAULT_META_IMAGE = os.path.join(STATIC_URL, SITE_LOGO)
if not DEBUG:
    ALLOWED_HOSTS = [META_SITE_DOMAIN]
