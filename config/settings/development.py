"""Settings for development environment.
    Designed for use on a local computer and run via the
    'manage.py runserver' command.
"""
from .base import *  # pylint: disable=wildcard-import, unused-wildcard-import
from .base import env


# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/stable/ref/settings/#debug
DEBUG = env.bool('DJANGO_DEBUG', default=True)


# django-cors-middleware
# ------------------------------------------------------------------------------
CORS_ORIGIN_ALLOW_ALL = True


# CACHES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/stable/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}


# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/stable/ref/settings/#email-host
EMAIL_HOST = 'localhost'
# https://docs.djangoproject.com/en/stable/ref/settings/#email-port
EMAIL_PORT = 1025


# django-debug-toolbar
# ------------------------------------------------------------------------------
# https://django-debug-toolbar.readthedocs.io/en/stable/installation.html#prerequisites
INSTALLED_APPS += [
    'debug_toolbar',
    'django_extensions',
]
# https://django-debug-toolbar.readthedocs.io/en/stable/installation.html#middleware
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
# https://django-debug-toolbar.readthedocs.io/en/stable/configuration.html#debug-toolbar-config
DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}
# https://django-debug-toolbar.readthedocs.io/en/stable/installation.html#internal-ips
INTERNAL_IPS = ['127.0.0.1', '10.0.2.2']
