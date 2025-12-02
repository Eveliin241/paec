from pathlib import Path
import os # Necesario para leer variables de entorno (recomendado)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# =======================================================================
# 1. SEGURIDAD Y ENTORNO
# =======================================================================

# 🚨 MEJORA DE SEGURIDAD: Usa una variable de entorno para la clave secreta
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-0)618za+vtaq#(rx$u5hccjb_x!7vhd3soa=myqwj-xzn%v&+2')

# 🚨 CRÍTICO: DEBUG debe ser False en producción (Render)
# Usamos una variable de entorno, por defecto True (para desarrollo local)
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# 🚨 CORRECCIÓN DE DOMINIOS
# Añadimos el dominio de Render que causó el error y el comodín para variables de entorno
ALLOWED_HOSTS = [
    'paec-1-fpsw.onrender.com', # <-- Dominio exacto que te dio el error
    'localhost',
    '127.0.0.1',
    # Añade aquí el dominio que tenías antes si es diferente:
    #'paec-dkyk.onrender.com', 
]

# Si el DEBUG es Falso (en Render), permite todas las URLs de Render (opcional pero robusto)
if not DEBUG:
    ALLOWED_HOSTS.append('.onrender.com')


# =======================================================================
# 2. APLICACIONES Y MIDDLEWARE (SIN CAMBIOS)
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
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Añadir el middleware de whitenoise es común para servir estáticos en Render,
    # pero no siempre es necesario si usas collectstatic. Lo dejo como opcional
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'miweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Tu DIRS está bien si tienes una carpeta 'templates' en la raíz del proyecto
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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# =======================================================================
# 3. CONFIGURACIÓN DE ARCHIVOS ESTÁTICOS (CRÍTICO PARA CSS/JS EN RENDER)
# =======================================================================

# URL para referenciar estáticos en el HTML (está bien, elimina la definición duplicada)
STATIC_URL = 'static/'

# Directorios donde buscar archivos estáticos adicionales (como tu carpeta 'static' global)
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Directorio donde Django recolectará todos los estáticos para producción (CRÍTICO)
# Render usará esta carpeta para servir tus archivos CSS/JS/Imágenes.
STATIC_ROOT = BASE_DIR / 'staticfiles'