from pathlib import Path
from dotenv import load_dotenv
import os
from django.utils.translation import gettext_lazy as _


load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG")

ALLOWED_HOSTS = ["kedi.uz", "localhost", "0.0.0.0", "127.0.0.1"]


# Application definition
DJANGO_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

CUSTOM_APPS = [
    "apps.common.apps.CommonConfig",
    "apps.users.apps.UsersConfig",
    "apps.book.apps.BookConfig",

]

THIRD_PARTY_APPS = [
    "modeltranslation",
    "ckeditor",
    "ckeditor_uploader",
    "location_field.apps.DefaultConfig",
    # "captcha",
]

INSTALLED_APPS = DJANGO_APPS + CUSTOM_APPS + THIRD_PARTY_APPS

CKEDITOR_UPLOAD_PATH = "uploads/"
# CKEDITOR_BASEPATH = "/static/ckeditor/"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    # "django.middleware.locale.LocaleMiddleware",
    "core.middleware.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR, "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                'apps.book.context_processors.top_communities',
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": os.getenv("DB_ENGINE", "django.db.backends.postgresql"),
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        # "PORT": os.getenv("DB_PORT"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


LANGUAGE_CODE = "uz"
LANGUAGES = (
    ("en", _("English")),
    ("uz", _("Uzbek")),
    ("ru", _("Russian")),
)

TIME_ZONE = "Asia/Tashkent"

USE_I18N = True
USE_L10N = True
USE_TZ = True


MODELTRANSLATION_DEFAULT_LANGUAGE = "uz"

gettext = lambda s: s

MODELTRANSLATION_LANGUAGES = (
    "uz",
    "ru",
    "en",
)
MODELTRANSLATION_FALLBACK_LANGUAGES = {
    "default": (
        "uz",
        "ru",
        "en",
    ),
    "uz": (
        "ru",
        "en",
    ),
    "en": (
        "uz",
        "ru",
    ),
    "ru": (
        "uz",
        "en",
    ),
}

MODELTRANSLATION_PREPOPULATE_LANGUAGE = "en"

LOCALE_PATHS = (os.path.join(BASE_DIR, "locale"),)


# auth
AUTH_USER_MODEL = "users.User"

EMAIL_HOST = os.getenv("EMAIL_HOST", "")
EMAIL_PORT = os.getenv("EMAIL_PORT", "")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "")
EMAIL_USE_SSL = os.getenv("EMAIL_USE_SSL", "")
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", "")
EMAIL_BACKEND = os.getenv("EMAIL_BACKEND", "")


# STATIC
STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_THUMBNAIL_SIZE = (450, 300)
CKEDITOR_JQUERY_URL = "//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"
CKEDITOR_CONFIGS = {
    "default": {
        "config.versionCheck": False,
        "toolbar": "full",
        "height": 300,
        "width": 700,
    }
}

LOCATION_FIELD = {
    "map.provider": "openstreetmap",
    "search.provider": "nominatim",
}

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"
