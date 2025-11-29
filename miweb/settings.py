from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# ==============================================
# SECURITY
# ==============================================
SECRET_KEY = 'django-insecure-0)618za+vtaq#(rx$u5hccjb_x!7vhd3soa=myqwj-xzn%v&+2'
DEBUG = True
ALLOWED_HOSTS = ['paec-djoi.onrender.com', '127.0.0.1', 'localhost']

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# ==============================================
# INSTALLED APPS
# ==============================================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'inicio',
]

# ==============================================
# MIDDLEWARE
# ==============================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'miweb.urls'

# ==============================================
# TEMPLATES
# ==============================================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # rutas adicionales si tienes templates fuera de apps
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'miweb.wsgi.application'

# ==============================================
# DATABASE
# ==============================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ==============================================
# INTERNATIONALIZATION
# ==============================================
LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ==============================================
# STATIC FILES
# ==============================================
STATIC_URL = '/static/'  # la barra inicial es importante
STATIC_ROOT = BASE_DIR / 'staticfiles'  # carpeta donde collectstatic pone los archivos
# STATICFILES_DIRS = []  # solo necesario si tienes carpetas de static fuera de apps

# ==============================================
# DEFAULT AUTO FIELD
# ==============================================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
