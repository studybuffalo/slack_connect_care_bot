"""Base settings to build other settings files upon."""
import environ


# SETUP
# ------------------------------------------------------------------------------
# Setup directory references
ROOT_DIR = environ.Path(__file__) - 3
APPS_DIR = ROOT_DIR.path('ccb')

# Setup environment variable references
env = environ.Env()
env.read_env(str(ROOT_DIR.path('config', 'settings', 'ccb.env')))


# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/stable/ref/settings/#debug
DEBUG = env.bool('DJANGO_DEBUG', default=True)
# https://docs.djangoproject.com/en/stable/ref/settings/#secret-key
SECRET_KEY = env('DJANGO_SECRET_KEY', default='llyJzPogLi0gjBrvU0q6yJkwIDJsgLOre2JZMzsIPSlrq5mGbuesgOYvCJLyFWAh')
# https://docs.djangoproject.com/en/stable/ref/settings/#allowed-hosts
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['127.0.0.1', 'localhost'])


# GENERAL
# ------------------------------------------------------------------------------
TIME_ZONE = 'UTC'
# https://docs.djangoproject.com/en/stable/ref/settings/#language-code
LANGUAGE_CODE = 'en-CA'
LANGUAGES = [
    ('en-CA', 'English'),
]
# https://docs.djangoproject.com/en/stable/ref/settings/#site-id
SITE_ID = 1
# https://docs.djangoproject.com/en/stable/ref/settings/#use-i18n
USE_I18N = True
# https://docs.djangoproject.com/en/stable/ref/settings/#use-l10n
USE_L10N = True
# https://docs.djangoproject.com/en/stable/ref/settings/#use-tz
USE_TZ = True


# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/stable/ref/settings/#databases
DATABASES = {
    'default': env.db('DJANGO_DB_URL', default='postgres:///ccb'),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True


# URLS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/stable/ref/settings/#root-urlconf
ROOT_URLCONF = 'config.urls'
# https://docs.djangoproject.com/en/stable/ref/settings/#wsgi-application
WSGI_APPLICATION = 'config.wsgi.application'


# APPS
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
]
THIRD_PARTY_APPS = [
    'allauth',
    'allauth.account',
    'corsheaders',
]
LOCAL_APPS = [
    'ccb.slack_app.apps.SlackAppConfig',
    'ccb.users.apps.UsersConfig',
]

# https://docs.djangoproject.com/en/stable/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


# AUTHENTICATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/stable/ref/settings/#auth-user-model
AUTH_USER_MODEL = 'users.User'
# https://docs.djangoproject.com/en/stable/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL = 'admin'
# https://docs.djangoproject.com/en/stable/ref/settings/#login-url
LOGIN_URL = 'account_login'
LOGOUT_URL = 'account_logout'


# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/stable/ref/settings/#password-hashers
PASSWORD_HASHERS = [
    # https://docs.djangoproject.com/en/stable/topics/auth/passwords/#using-argon2-with-django
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
]
# https://docs.djangoproject.com/en/stable/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# AUTHENTICATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/stable/ref/settings/#authentication-backends
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]


# MIDDLEWARE
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/stable/ref/settings/#middleware
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# STATIC
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/stable/ref/settings/#static-root
STATIC_ROOT = str(ROOT_DIR('staticfiles'))
# https://docs.djangoproject.com/en/stable/ref/settings/#static-url
STATIC_URL = '/static/'
# https://docs.djangoproject.com/en/stable/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [
    str(APPS_DIR.path('static')),
]
# https://docs.djangoproject.com/en/stable/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]


# MEDIA
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/stable/ref/settings/#media-root
MEDIA_ROOT = str(APPS_DIR('media'))
# https://docs.djangoproject.com/en/stable/ref/settings/#media-url
MEDIA_URL = '/media/'


# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/stable/ref/settings/#templates
TEMPLATES = [
    {
        # https://docs.djangoproject.com/en/stable/ref/settings/#std:setting-TEMPLATES-BACKEND
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # https://docs.djangoproject.com/en/stable/ref/settings/#template-dirs
        'DIRS': [
            str(APPS_DIR.path('templates')),
        ],
        'OPTIONS': {
            # https://docs.djangoproject.com/en/stable/ref/settings/#template-debug
            'debug': DEBUG,
            # https://docs.djangoproject.com/en/stable/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/stable/ref/templates/api/#loader-types
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            # https://docs.djangoproject.com/en/stable/ref/settings/#template-context-processors
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# FIXTURES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/stable/ref/settings/#fixture-dirs
FIXTURE_DIRS = (
    str(APPS_DIR.path('fixtures')),
)


# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/stable/ref/settings/#email-backend
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')
# https://docs.djangoproject.com/en/stable/ref/settings/#default-from-email
DEFAULT_FROM_EMAIL = env(
    'DJANGO_DEFAULT_FROM_EMAIL',
    default='Connect Care Bot <noreply@connectcarebot.io>'
)
# https://docs.djangoproject.com/en/stable/ref/settings/#server-email
SERVER_EMAIL = env('DJANGO_SERVER_EMAIL', default=DEFAULT_FROM_EMAIL)
# https://docs.djangoproject.com/en/2.2/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = env('DJANGO_EMAIL_SUBJECT_PREFIX', default='[Connect Care Bot] ')


# ADMIN
# ------------------------------------------------------------------------------
# Django Admin URL path.
ADMIN_URL = env('DJANGO_ADMIN_URL', default='admin/')
# https://docs.djangoproject.com/en/stable/ref/settings/#admins
ADMINS = []
# https://docs.djangoproject.com/en/stable/ref/settings/#managers
MANAGERS = ADMINS


# django-allauth
# ------------------------------------------------------------------------------
# https://django-allauth.readthedocs.io/en/stable/configuration.html
def get_user_display(user):
    """Returns user display string."""
    return user.name


ACCOUNT_ALLOW_REGISTRATION = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_ADAPTER = 'users.adapters.AccountAdapter'
ACCOUNT_USER_DISPLAY = get_user_display
