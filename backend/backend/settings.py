# ========================================================================
from pathlib import Path
import os
import json
from utility.methods import post_message_to_terminal, post_error_to_terminal
from utility.constants import *

# ========================================================================
BASE_DIR = Path(__file__).resolve().parent
PARENT_DIR = BASE_DIR.parent

# ========================================================================

try:
    with open(os.path.join(PARENT_DIR, C_SECRET, C_SYSTEM), "r") as fp:
        C_TYPE = fp.readline()
    with open(os.path.join(PARENT_DIR, C_SECRET, C_SECRET_FILE_NAME), "r") as fp:
        file = json.load(fp)
        SECRET_KEY = file[C_TYPE][C_SECRET_KEY]
        DEBUG = file[C_TYPE][C_DEBUG]
        ALLOWED_HOSTS = file[C_TYPE][C_ALLOWED_HOSTS]
        CURRENCY_CONV_KEY = file[C_TYPE][C_CURRENCY_CONV_KEY]
        if C_TYPE == C_DEV:
            DATABASES = {
                C_DEFAULT: {
                    C_ENGINE: "django.db.backends.sqlite3",
                    C_NAME: os.path.join(
                        PARENT_DIR, C_TEMPFILES, C_SQLITE_DB, "medical.dev.sqlite.db"
                    ),
                }
            }
        else:
            DATABASES = {
                C_DEFAULT: {
                    C_ENGINE: file[C_TYPE][C_DATABASES][C_ENGINE],
                    C_NAME: file[C_TYPE][C_DATABASES][C_NAME],
                    C_USER: file[C_TYPE][C_DATABASES][C_USER],
                    C_PASSWORD: file[C_TYPE][C_DATABASES][C_PASSWORD],
                    C_HOST: file[C_TYPE][C_DATABASES][C_HOST],
                    C_PORT: file[C_TYPE][C_DATABASES][C_PORT],
                }
            }
            DATABASES[C_DEFAULT]["OPTIONS"] = {
                "init_command": "SET sql_mode='STRICT_TRANS_TABLES'"
            }
        del file
except KeyError as e:
    post_error_to_terminal(str(e))
    exit(1)

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # ========================================================================
    "rest_framework",
    "rest_framework_swagger",
    "drf_yasg",
    # ========================================================================
    "app_master",
    "app_cdn",
    "app_transaction",
    # ========================================================================
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

ROOT_URLCONF = "backend.urls"

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

WSGI_APPLICATION = "backend.wsgi.application"

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

DEBUG_TOOLBAR_PANELS = [
    "debug_toolbar.panels.timer.TimerPanel",
    "debug_toolbar.panels.headers.HeadersPanel",
    "debug_toolbar.panels.request.RequestPanel",
    "debug_toolbar.panels.sql.SQLPanel",
    "debug_toolbar.panels.cache.CachePanel",
    "debug_toolbar.panels.profiling.ProfilingPanel",
    "template_timings_panel.panels.TemplateTimings.TemplateTimings",
]
