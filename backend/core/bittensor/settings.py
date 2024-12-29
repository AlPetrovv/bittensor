import os
from datetime import timedelta
from pathlib import Path

import environ
import openai

env = environ.Env()
env.read_env("../app_envs/django.env")
env.read_env("../app_envs/postgres.env")

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env.str("SECRET_KEY")

DEBUG = env.bool("DEBUG", default=False)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS")

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # project apps
    "apps.auth_users",
    "apps.chats",
    "apps.subnets",
    # installed apps
    "rest_framework",
    "rest_framework.authtoken",
    "djoser",
    "drf_spectacular",
    "drf_spectacular_sidecar",
    "corsheaders",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = "bittensor.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "bittensor.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("POSTGRES_HOST"),
        "PORT": "5432",
    },
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LOG_PATH = os.path.join(BASE_DIR, "files/logs/app")

if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "console": {
            "format": "===={levelname}===={asctime}====\n"
            'File "{pathname}", line {lineno}\n'
            "{message}\n",
            "style": "{",
        },
        "main_formatter": {
            "format": "===={levelname}===={asctime} - {pathname} - line {lineno}\n\t{message}",
            "style": "{",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "precision_formatter": {
            "format": "===={levelname}===={asctime} - {pathname} - line {lineno}\n\t{message}",
            "style": "{",
            "datefmt": "%Y-%m-%d %H:%M:%S,%03d",
        },
    },
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "console"},
        "subnets": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "main_formatter",
            "maxBytes": 1024 * 1024 * 5,  # 5 MB
            "backupCount": 7,
            "filename": LOG_PATH + "/subnet.log",
        },
        "chats": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "main_formatter",
            "maxBytes": 1024 * 1024 * 5,  # 5 MB
            "backupCount": 7,
            "filename": LOG_PATH + "/chats.log",
        },
        "auth_users": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "main_formatter",
            "maxBytes": 1024 * 1024 * 5,  # 5 MB
            "backupCount": 7,
            "filename": LOG_PATH + "/auth_users.log",
        },
        "django": {
            "level": "ERROR",
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "main_formatter",
            "maxBytes": 1024 * 1024 * 5,  # 5 MB
            "backupCount": 7,
            "filename": LOG_PATH + "/django.log",
        },
    },
    "loggers": {
        "subnets": {
            "handlers": ["console", "subnets"],
            "level": "DEBUG",
        },
        "chats": {
            "handlers": ["console", "chats"],
            "level": "DEBUG",
        },
        "auth_users": {
            "handlers": ["console", "auth_users"],
            "level": "DEBUG",
        },
        "django": {
            "handlers": ["console", "django"],
            "level": "ERROR",
            "propagate": True,
        },
    },
}

LANGUAGE_CODE = "en"
LANGUAGES = [
    ("en", "English"),
    ("ru", "Russian"),
]

TIME_ZONE = "UTC"

USE_I18N = True
USE_L10N = True
I18N_URLS_ENABLED = True

USE_TZ = True

LOCALE_PATHS = [
    os.path.join(BASE_DIR, "files/locale"),
]

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "files/static")
STATICFILES_DIRS = [os.path.join(BASE_DIR, "files/static_source")]

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "files/media")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "auth_users.AuthUser"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=env.int("ACCESS_TOKEN_LIFETIME")),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=env.int("REFRESH_TOKEN_LIFETIME")),
    "AUTH_HEADER_TYPES": ("JWT",),
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Bittensor API",
    "DESCRIPTION": "Bittensor API description",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "SWAGGER_UI_DIST": "SIDECAR",
    "SWAGGER_UI_FAVICON_HREF": "SIDECAR",
    "REDOC_DIST": "SIDECAR",
    "SCHEMA_PATH_PREFIX": r"/api/v[0-9]",
}

DJOSER = {
    "SET_USERNAME_RETYPE": False,
    "USERNAME_RESET_CONFIRM_RETYPE": False,
    "PASSWORD_RESET_CONFIRM_URL": False,
    "USER_CREATE_PASSWORD_RETYPE": True,
    "SEND_ACTIVATION_EMAIL": False,
}


OPENAI_API_KEY = env.str("OPENAI_API_KEY")
OPENAI_ORGANIZATION = env.str("OPENAI_ORGANIZATION")
OPENAI_PROJECT = env.str("OPENAI_PROJECT")

CLIENT = openai.Client(
    project=OPENAI_PROJECT,
    organization=OPENAI_ORGANIZATION,
)
