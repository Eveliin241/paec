from pathlib import Path
import os
import dj_database_url # Necesario si vas a usar PostgreSQL

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# =======================================================================
# 1. SEGURIDAD Y ENTORNO
# =======================================================================

# 🚨 CRÍTICO: Leer la clave secreta de la variable de entorno
SECRET_KEY = os.environ.get('SECRET_KEY', 'tu-clave-secreta-de-desarrollo-aqui')

# 🚨 CRÍTICO: DEBUG debe ser False en producción (Render)
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# 🚨 CORRECCIÓN DE DOMINIOS (ALLOWED_HOSTS)
ALLOWED_HOSTS = [
    # Usamos el dominio exacto que causó el error: paec-g60x.onrender.com
    'paec-g60x.onrender.com', 
    'localhost',
    '127.0.0.1',
]

# Si DEBUG es False (Producción), agregamos la variable de entorno de Render
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
    'inicio',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # AÑADIDO: WhiteNoise debe ir justo después de SecurityMiddleware para servir estáticos
    'whitenoise.middleware.WhiteNoiseMiddleware', 
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'miweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

# Configuración por defecto: SQLite (para desarrollo local)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 💡 Configuración de PostgreSQL (Recomendado para Render)
# Usa la variable de entorno DATABASE_URL proporcionada por Render.
DATABASE_URL = os.environ.get('DATABASE_URL')
if DATABASE_URL:
    DATABASES['default'] = dj_database_url.config(default=DATABASE_URL, conn_max_age=600)


# =======================================================================
# 4. CONFIGURACIÓN GENERAL Y ESTÁTICOS
# =======================================================================

LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# 🚨 CONFIGURACIÓN DE ARCHIVOS ESTÁTICOS (CRÍTICO PARA RENDER)
STATIC_URL = 'static/'

# Directorios donde buscar archivos estáticos adicionales (como tu carpeta 'static' global)
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Directorio donde Django recolectará TODOS los estáticos para WhiteNoise (CRÍTICO)
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Configuración para que WhiteNoise comprima y optimice los archivos
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# =======================================================================
# FIN DEL ARCHIVO
# =======================================================================