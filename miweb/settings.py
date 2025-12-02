from pathlib import Path
import os
import dj_database_url # Necesario si vas a usar PostgreSQL

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# =======================================================================
# 1. SEGURIDAD Y ENTORNO
# =======================================================================

SECRET_KEY = os.environ.get('SECRET_KEY', 'tu-clave-secreta-de-desarrollo-aqui')
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# 🚨 CORRECCIÓN DE DOMINIOS (ALLOWED_HOSTS)
ALLOWED_HOSTS = [
    'paec-g60x.onrender.com', # Dominio que causa el error DisallowedHost
    'localhost',
    '127.0.0.1',
]

if not DEBUG:
    RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
    if RENDER_EXTERNAL_HOSTNAME:
        ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# =======================================================================
# 2. APLICACIONES Y MIDDLEWARE
# =======================================================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'inicio', # ¡Tu aplicación debe estar aquí!
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', 
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'miweb.urls'

# 🚨 SECCIÓN CORREGIDA: TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # DIRS para plantillas globales (opcional)
        'DIRS': [BASE_DIR / 'templates'], 
        # CRÍTICO: 'APP_DIRS: True' le dice a Django que busque en inicio/templates/
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

# =======================================================================
# 3. BASE DE DATOS
# =======================================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# (Lógica de PostgreSQL sin descomentar)

# =======================================================================
# 4. CONFIGURACIÓN GENERAL Y ESTÁTICOS
# =======================================================================

LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}