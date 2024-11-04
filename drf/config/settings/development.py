from .base import *  # noqa


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY", default="django-secretkey")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": env.get_value(
            "DATABASE_ENGINE", default="django.db.backends.postgresql"
        ),
        "NAME": env.get_value(
            "DATABASE_DB", default="postgres"
        ),
        "USER": env.get_value(
            "DATABASE_USER", default="postgres"
        ),
        "PASSWORD": env.get_value(
            "DATABASE_PASSWORD", default="postgres"
        ),
        "HOST": env.get_value(
            "DATABASE_HOST", default="localhost"
        ),
        "PORT": env.get_value(
            "DATABASE_PORT", default="5432"
        ),
        "OPTIONS": {
            "options": f"-c search_path={env.get_value('DATABASE_SCHEMA', default='public')}"
        },
    }
}


try:
    from .local_settings import *  # noqa
except ImportError:
    pass
