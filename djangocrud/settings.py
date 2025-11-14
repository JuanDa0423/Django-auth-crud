from pathlib import Path
import os
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key')

DEBUG = os.environ.get("DEBUG", "False") == "True"


ALLOWED_HOSTS = ['.onrender.com', 'localhost', '127.0.0.1']

RENDER_EXTERNAL_HOSTNAME = os.environ.get("RENDER_EXTERNAL_HOSTNAME")
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tasks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # WhiteNoise debe ir aquí
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangocrud.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djangocrud.wsgi.application'

# ---------------------------
# DATABASE
# ---------------------------

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',  # fallback seguro
        conn_max_age=600
    )
}

# ---------------------------
# STATIC FILES
# ---------------------------

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]  # si usas carpeta static/

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_STORAGE = (
    'whitenoise.storage.CompressedManifestStaticFilesStorage'
)

# ---------------------------
# AUTH
# ---------------------------

LOGIN_URL = '/signin/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
