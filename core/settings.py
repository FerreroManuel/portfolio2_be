import os
import environ

from pathlib import Path


env = environ.Env()
environ.Env.read_env()


SITE_NAME = 'Manuel Ferrero'

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = os.environ.get("DEBUG") == "True"


ALLOWED_HOSTS = []


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
    "portfolio",
    "contact",
]

CSRF_TRUSTED_ORIGINS = ['http://localhost:4200','https://*.127.0.0.1']

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
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
        "DIRS": [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = "core.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]

LANGUAGE_CODE = "es-AR"

TIME_ZONE = "America/Argentina/Buenos_Aires"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Media files settings
PUBLIC_MEDIA_LOCATION = 'assets/media'

MEDIA_URL = f'https://www.manuelferrero.com.ar/{PUBLIC_MEDIA_LOCATION}/'

# Django-Storages settings
DEFAULT_FILE_STORAGE = 'storages.backends.ftp.FTPStorage'

FTP_STORAGE_LOCATION = os.environ.get('FTP_STORAGE_LOCATION')

# CORS settings
CORS_ALLOW_ALL_ORIGINS = True

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEFAULT_FROM_EMAIL = 'no-responder@manuelferrero.com.ar'

DEFAULT_CONTACT_EMAIL = 'contacto@manuelferrero.com.ar'



#! =============================== PRODUCTION SETTINGS ===============================
if not DEBUG:
    ALLOWED_HOSTS = [
        'https://www.manuelferrero.com.ar',
        'https://ferreromanuel.pythonanywhere.com',
    ]

    CSRF_TRUSTED_ORIGINS = ALLOWED_HOSTS

    # Email settings
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

    EMAIL_HOST = 'smtp.manuelferrero.com.ar'

    EMAIL_HOST_USER = 'no-responder@manuelferrero.com.ar'

    EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")

    EMAIL_PORT = 587

    EMAIL_USE_TLS = True

    EMAIL_TIMEOUT = 300 # Sec

    DEFAULT_FROM_EMAIL = 'No responder | MF! <no-responder@manuelferrero.com.ar>'

    DEFAULT_CONTACT_EMAIL = 'Contacto | MF! <contacto@manuelferrero.com.ar>'

    # CORS Policy
    CORS_ALLOW_ALL_ORIGINS = False
    
    CORS_ALLOWED_ORIGINS = []

    # Session & CSRF cookies
    SESSION_COOKIE_SECURE = True
    
    SECURE_BROWSER_XSS_FILTER = True
    
    SECURE_CONTENT_TYPE_NOSNIFF = True
    
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    
    SECURE_HSTS_SECONDS = 31536000
    
    SECURE_REDIRECT_EXEMPT = []
    
    SECURE_SSL_REDIRECT = True
    
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
