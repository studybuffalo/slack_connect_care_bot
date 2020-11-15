es (155 sloc) 6.85 KB
"""Settings for the production server."""
import logging

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.redis import RedisIntegration

from ccb import __version__

from .base import *  # pylint: disable=wildcard-import, unused-wildcard-import
from .base import env


# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/stable/ref/settings/#csrf-cookie-httponly
CSRF_COOKIE_HTTPONLY = env.bool('DJANGO_CSRF_COOKIE_HTTPONLY', default=True)
# https://docs.djangoproject.com/en/stable/ref/settings/#csrf-cookie-secure
CSRF_COOKIE_SECURE = env.bool('DJANGO_CSRF_COOKIE_SECURE', default=True)
# https://docs.djangoproject.com/en/stable/ref/settings/#secure-browser-xss-filter
SECURE_BROWSER_XSS_FILTER = env.bool('DJANGO_SECURE_BROWSER_XSS_FILTER', default=True)
# https://docs.djangoproject.com/en/stable/ref/middleware/#x-content-type-options-nosniff
SECURE_CONTENT_TYPE_NOSNIFF = env.bool('DJANGO_SECURE_CONTENT_TYPE_NOSNIFF', default=True)
# https://docs.djangoproject.com/en/stable/ref/settings/#secure-hsts-include-subdomains
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool('DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS', default=True)
# https://docs.djangoproject.com/en/stable/ref/settings/#secure-hsts-preload
SECURE_HSTS_PRELOAD = env.bool('DJANGO_SECURE_HSTS_PRELOAD', default=True)
# https://docs.djangoproject.com/en/stable/ref/settings/#secure-hsts-seconds
SECURE_HSTS_SECONDS = env.int('DJANGO_SECURE_HSTS_SECONDS', default=60)
# https://docs.djangoproject.com/en/stable/ref/settings/#secure-proxy-ssl-header
SECURE_PROXY_SSL_HEADER = None  # Site not served through proxy at this time
# https://docs.djangoproject.com/en/stable/ref/settings/#secure-ssl-redirect
SECURE_SSL_REDIRECT = env.bool('DJANGO_SECURE_SSL_REDIRECT', default=True)
# https://docs.djangoproject.com/en/stable/ref/settings/#session-cookie-httponly
SESSION_COOKIE_HTTPONLY = env.bool('DJANGO_SESSION_COOKIE_HTTPONLY', default=True)
# https://docs.djangoproject.com/en/stable/ref/settings/#session-cookie-secure
SESSION_COOKIE_SECURE = env.bool('DJANGO_SESSION_COOKIE_SECURE', default=True)
# https://docs.djangoproject.com/en/stable/ref/settings/#x-frame-options
X_FRAME_OPTIONS = env('DJANGO_X_FRAME_OPTIONS', default='DENY')


# django-cors-headers
# ------------------------------------------------------------------------------
CORS_ORIGIN_WHITELIST = env.list(
    'CORS_ORIGIN_WHITELIST',
    default=['http://127.0.0.1:8000', 'http://localhost:8000']
)


# DATABASES
# ------------------------------------------------------------------------------
DATABASES['default']['CONN_MAX_AGE'] = env.int('DJANGO_DB_CONN_MAX_AGE', default=60)


# CACHES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/stable/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f'{env("REDIS_URL", default="redis://127.0.0.1:6379")}/{0}',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            # Mimicing memcache behavior.
            # http://niwinz.github.io/django-redis/latest/#_memcached_exceptions_behavior
            'IGNORE_EXCEPTIONS': True,
        }
    }
}


# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/stable/ref/settings/#templates
TEMPLATES[0]['OPTIONS']['loaders'] = [
    (
        'django.template.loaders.cached.Loader',
        [
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        ]
    ),
]


# Sentry
# ------------------------------------------------------------------------------
# Compile release version
BETA_RELEASE = '-beta' if env('DJANGO_SENTRY_RELEASE_BETA', default=False) else ''
RELEASE = 'ccb@{}{}'.format(__version__, BETA_RELEASE)

# Initialize Sentry
SENTRY_DSN = env('DJANGO_SENTRY_DSN')

sentry_sdk.init(
    dsn=SENTRY_DSN,
    release=RELEASE,
    integrations=[DjangoIntegration(), RedisIntegration()],
)

# Configure logging details
LOGGING_CONFIG = None
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': env.int('DJANGO_SENTRY_LOG_LEVEL'),
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console', ],
            'propagate': False,
        },
        'django.security.DisallowedHost': {
            'level': 'ERROR',
            'handlers': ['console', ],
            'propagate': False,
        },
    },
})
