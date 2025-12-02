from pathlib import Path
import os
import dj_database_url # Necesario si vas a usar PostgreSQL

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# =======================================================================
# 1. SEGURIDAD Y ENTORNO
# =======================================================================

# 🚨 MEJORA DE SEGURIDAD: Leer la clave secreta de la variable de entorno
SECRET_KEY = os.environ.get('SECRET_KEY', 'tu-clave-secreta-de-desarrollo-aqui')

# 🚨 CRÍTICO: DEBUG debe ser False en producción (Render)
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# 🚨 CORRECCIÓN DE DOMINIOS (ALLOWED_HOSTS)
# Añadimos el dominio de Render que causó el error y el comodín para variables de entorno
ALLOWED_HOSTS = [
    # **REEMPLAZA ESTE DOMINIO CON TU URL DE RENDER ACTUAL**
    'paec-1-fpsw.onrender.com', 
    'localhost',
    '127.0.0.1',
]

# Si DEBUG es False (Producción), permitimos el host externo de Render
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
    # AÑADE ESTO: WhiteNoise debe ir justo después de SecurityMiddleware
    'whitenoise.middleware.WhiteNoiseMiddleware', 
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'miweb.urls'

# ... (El resto de TEMPLATES, etc. se mantiene igual)

WSGI_APPLICATION = 'miweb.wsgi.application'


# =======================================================================
# 3. BASE DE DATOS (OPCIONAL: Configuración de SQLite para Desarrollo)
# =======================================================================

# Base de datos predeterminada para desarrollo local (SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 💡 MEJORA: Si usas PostgreSQL en Render, descomenta y usa esta configuración:
# DATABASE_URL = os.environ.get('DATABASE_URL')
# if DATABASE_URL:
#     DATABASES['default'] = dj_database_url.config(default=DATABASE_URL, conn_max_age=600)


# ... (LANGUAGE_CODE, TIME_ZONE, etc. se mantienen igual)

# =======================================================================
# 4. CONFIGURACIÓN DE ARCHIVOS ESTÁTICOS (CRÍTICO PARA RENDER)
# =======================================================================

# URL que usas en tus templates (ej. {% static 'css/style.css' %})
STATIC_URL = 'static/'

# Directorio donde buscar archivos estáticos adicionales (como tu carpeta 'static' global)
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Directorio donde Django recolectará TODOS los estáticos para WhiteNoise (CRÍTICO)
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Configuración adicional para que WhiteNoise comprima y optimice los archivos
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
