import environ
import structlog

from .base import *  # noqa

env = environ.Env()
env.read_env(str(BASE_DIR / ".env"))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY", default="django-secretkey")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
        env("IP_ADDRESS"), "example.com", "www.example.com", "localhost"
    ]


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


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "json_formatter": {
            "()": structlog.stdlib.ProcessorFormatter,
            "processor": (
                structlog.processors.JSONRenderer(
                    ensure_ascii=False,  # 日本語を読みやすくする。
                )
            )
        },
        "plain_console": {
            "()": structlog.stdlib.ProcessorFormatter,
            "processor": (
                structlog.dev.ConsoleRenderer(),
            )
        }
    },
    "handlers": {
        "console": {
            "level": "WARNING",
            "filters": ["require_debug_false"],
            "class": "logging.StreamHandler",
            "formatter": "json_formatter",
        },
        "file": {
            "level": "WARNING",
            "filters": ["require_debug_false"],
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "json_formatter",
            "filename": BASE_DIR / "logs/production.log",
            "maxBytes": 10 * 1024 * 1024,  # 10MB
            "backupCount": 10,
        },
    },
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse"
        },
    },
    "root": {
        "handlers": ["console", "file"],
        "level": "WARNING",
        "propagate": False
    },
    "loggers": {
        "django.db.backends": {
            "handlers": ["console", "file"],
            "level": "WARNING",
            "propagate": False,
        },
        "django.request": {
            "handlers": ["console", "file"],
            "level": "WARNING",
            "propagate": False,
        },
        "django.server": {
            "handlers": ["console", "file"],
            "level": "WARNING",
            "propagate": False,
        },
        "django.template": {
            "handlers": ["console", "file"],
            "level": "WARNING",
            "propagate": False,
        },
        "django": {
            "handlers": ["console", "file"],
            "level": "WARNING",
            "propagate": False,
        },
    },
}

structlog.configure(
    processors=[
        structlog.contextvars.merge_contextvars,
        structlog.stdlib.filter_by_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
    ],
    logger_factory=structlog.stdlib.LoggerFactory(),
    cache_logger_on_first_use=True,
)


try:
    from .local_settings import *  # noqa
except ImportError:
    pass
