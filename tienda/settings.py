import os
from pathlib import Path
import json
from django.utils.html import format_html
# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

####datos de configuración
ruta= os.path.dirname(os.path.abspath(__file__))
f = open('{}/conf.json'.format(ruta), 'r')
conf_string = f.read()
f.close()
conf = json.loads(conf_string)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-h*_%oy$w$sz!j*7sjl8q9^g6d_d@#&k@1@t9v$egg@t!tw4=4q'


BASE_URL=conf['base_url']
TOTAL_PAGINAS=conf['paginacion']

RUTA=conf['ruta']
RUTA2=conf['ruta2']
#envío mail
SERVER_STMP=conf['smtp']
PUERTO_SMTP= conf['smtp_puerto']
MAIL_SALIDA = conf['email']
PASSWORD_MAIL_SALIDA = conf['email_password']
WEBPAY_URL=conf['webpay_url']
WEBPAY_ID=conf['webpay_id']
WEBPAY_SECRET=conf['webpay_secret']

EMAIL_SECRET=conf['api_correo']
EMAIL_SENDER = conf['email_sender']

CMF_SECRET= conf['cmf_api']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = conf['debug']

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'perfil',
    'crispy_forms',
]

CRISPY_ALLOWED_TEMPLATE_PACKS = ['bootstrap5', 'uni_form']
CRISPY_TEMPLATE_PACK = 'bootstrap5'  # Establece el paquete de plantilla que deseas utilizar


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tienda.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),
        os.path.join(BASE_DIR, 'utilidades'),],
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

WSGI_APPLICATION = 'tienda.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': conf['bd'],
        'USER': conf['user'],
        'PASSWORD': conf['password'],
        'HOST': conf['server'],
        'PORT': conf['puerto'],
        'OPTIONS': {
          'autocommit': True,
          'sql_mode': 'STRICT_TRANS_TABLES',
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'America/Santiago'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/assets/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets'),
)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


JAZZMIN_UI_TWEAKS = {
    "theme": "cerulean",
}

JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "AutoPortal Administracion",

    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Backend AutoPortal",

    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "Backend AutoPortal",

    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "/IMG/logosf.png",
    "site_logo_classes": "img-circle",
    
    "copyright": "Desarrollado por <a href='https://www.AutoPortal.cl/' target='_blank'>AutoPortal</a>",
    "show_sidebar": True,
    "changeform_format": "horizontal_tabs",
    "user_avatar": None,

    
}