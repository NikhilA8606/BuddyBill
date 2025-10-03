import dj_database_url
from corsheaders.defaults import default_headers

from .env import ABS_PATH, ENV_BOOL, ENV_STR, ENV_LIST

DEBUG = ENV_BOOL("DEBUG", False)
SECRET_KEY = ENV_STR("SECRET_KEY", "secret" if DEBUG else "")
ALLOWED_HOSTS = ENV_LIST("ALLOWED_HOSTS", ",", ["*"] if DEBUG else [])

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "corsheaders",
    "rest_framework",
    "rest_framework.authtoken",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "django_filters",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    "drf_yasg",
    "rest_framework_simplejwt",
    "buddybill.apps.BuddybillConfig",
    "users.apps.UsersConfig",
    "utils.apps.UtilsConfig",
    "openapi.apps.OpenAPIConfig",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "project.urls"

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
            ]
        },
    }
]

WSGI_APPLICATION = "project.wsgi.application"

DATABASES = {"default": dj_database_url.config()}
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "users.User"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"  # noqa: E501
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

# allauth settings
ACCOUNT_USER_MODEL_USERNAME_FIELD = "email"
ACCOUNT_LOGIN_METHODS = {"email"}
ACCOUNT_SIGNUP_FIELDS = ["email*", "password1*", "password2*"]
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = "none"
LOGOUT_ON_PASSWORD_CHANGE = False
LOGIN_REDIRECT_URL = "/"

REST_AUTH = {
    "SESSION_LOGIN": False,
}
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

SITE_ID = 1

# static and media
STATIC_URL = ENV_STR("STATIC_URL", "/static/")
STATIC_ROOT = ENV_STR("STATIC_ROOT", ABS_PATH("static"))
MEDIA_URL = ENV_STR("MEDIA_URL", "/media/")
MEDIA_ROOT = ABS_PATH(ENV_STR("MEDIA_ROOT", "media"))
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# email settings
SERVER_EMAIL = ENV_STR("SERVER_EMAIL", "webmaster@localhost")
DEFAULT_FROM_EMAIL = ENV_STR("DEFAULT_FROM_EMAIL", SERVER_EMAIL)

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 100,
    "COERCE_DECIMAL_TO_STRING": False,
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
}

# log to console, assume the supervisor/system runner will take care of the logs
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {"class": "logging.StreamHandler"},
        "null": {"level": "DEBUG", "class": "logging.NullHandler"},
    },
    "loggers": {
        "": {
            "handlers": ["console"],
            "level": ENV_STR("LOG_LEVEL", "INFO"),
        },
        "django.request": {
            "handlers": ["console"],
            "level": "ERROR",
            "propagate": False,
        },
        "django.security.DisallowedHost": {
            "handlers": ["null"],
            "propagate": False,
        },
    },
}

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = default_headers + ("content-disposition",)

AWS_ACCESS_KEY_ID = ENV_STR("AWS_ACCESS_KEY_ID", "")
AWS_SECRET_ACCESS_KEY = ENV_STR("AWS_SECRET_ACCESS_KEY", "")

CELERY_BROKER_URL = ENV_STR("CELERY_BROKER_URL", "amqp://localhost")
CELERY_BACKEND = ENV_STR("CELERY_BACKEND")
CELERY_ALWAYS_EAGER = ENV_BOOL("CELERY_ALWAYS_EAGER", False)

# Periodic tasks via Celery Beat
# See https://docs.celeryproject.org/en/stable/userguide/periodic-tasks.html#beat-entries
CELERY_BEAT_SCHEDULE = {}
