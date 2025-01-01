import environ
import structlog

from .base import *  # noqa

env = environ.Env()
env.read_env(str(BASE_DIR /  "postgres" / ".env.dev"))


# Quick-start development settings - unsuitable for production

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY", default="django-secretkey")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS += ["silk",]

MIDDLEWARE += ["silk.middleware.SilkyMiddleware",]


# Database

DATABASES = {
    "default": {
        "ENGINE": env("DATABASE_ENGINE", default="django.db.backends.postgresql"),
        "NAME": env("POSTGRES_DB", default="postgres"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("POSTGRES_HOST", default="postgres"),
        "PORT": env("POSTGRES_PORT", default="5432"),
        "OPTIONS": {"options": f"-c search_path={env('POSTGRES_SCHEMA', default='public')}"},
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
            "level": "DEBUG",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
            "formatter": "json_formatter",
        },
        "file": {
            "level": "DEBUG",
            "filters": ["require_debug_true"],
            "class": "logging.FileHandler",
            "formatter": "json_formatter",
            "filename": BASE_DIR / "logs/debug.log",
        },
    },
    "filters": {
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue"
        },
    },
    "root": {
        "handlers": ["console", "file"],
        "level": "NOTSET",
        "propagate": False
    },
    "loggers": {
        "django.db.backends": {
            "handlers": ["console", "file"],
            "level": "DEBUG",
            "propagate": False,
        },
        "django.request": {
            "handlers": ["console", "file"],
            "level": "DEBUG",
            "propagate": False,
        },
        "django.server": {
            "handlers": ["console", "file"],
            "level": "DEBUG",
            "propagate": False,
        },
        "django.template": {
            "handlers": ["console", "file"],
            "level": "DEBUG",
            "propagate": False,
        },
        "django": {
            "handlers": ["console", "file"],
            "level": "DEBUG",
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
