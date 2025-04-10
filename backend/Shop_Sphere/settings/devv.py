from .common import *

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = [
    "http://localhost:5173",  # React frontend
    "http://127.0.0.1:5173",
]
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]


CELERY_BROKER_URL = "redis://redis:6379/1"

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}

DEBUG = True

DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": lambda request: True}

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "shop_sphere",
        "USER": "odd",
        "PASSWORD": "MyPassword",
        "HOST": "postgres",
    }
}


DEFAULT_FROM_EMAIL = "your_sender_email"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com" # your host address
EMAIL_HOST_USER = "your_sender_email"
EMAIL_HOST_PASSWORD = "your app password if host is google"
EMAIL_PORT = 587
EMAIL_USE_TLS = True

RAZOR_KEY_ID = "your razor_key_id"
RAZOR_KEY_SECRET = "your razor_key_secert"

if DEBUG:
    INTERNAL_IPS = ["127.0.0.1"]

SECRET_KEY = "your SECRET_KEY" # copy from common.py
