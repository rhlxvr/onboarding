"""
Django-Einstellungen für das Onboarding-Projekt.

Erstellt mit 'django-admin startproject' unter Verwendung von Django 4.0.

Für weitere Informationen zu dieser Datei, siehe
https://docs.djangoproject.com/en/4.0/topics/settings/

Für die vollständige Liste der Einstellungen und ihrer Werte, siehe
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os.path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Schnellstart-Entwicklungseinstellungen - ungeeignet für die Produktion
# Siehe https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SICHERHEITSWARNUNG: Halte den geheimen Schlüssel in der Produktion geheim!
SECRET_KEY = 'django-insecure-%qn98yoj@=xfw!o9w@90x=si%26v5d=l+jz(4&fjt=rtzfw#$1'

# SICHERHEITSWARNUNG: Schalte debug nicht in der Produktion ein!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Anwendungsdefinition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ob_app.apps.OnboardingAppConfig',
    'django_extensions',
    'ob_app.templatetags.search',
    'crispy_forms',
    'crispy_bootstrap4',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'onboarding.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

# Statische Dateien (CSS, JavaScript, Bilder)
STATIC_URL = '/static/'
STATIC_ROOT = ''
STATICFILES_DIRS = (os.path.join('static'),)

# WSGI-Anwendung
WSGI_APPLICATION = 'onboarding.wsgi.application'

# Datenbankkonfiguration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Passwortvalidierung
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

# Internationalisierung
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Einstellungen für Crispy Forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"

# Login-Einstellungen
LOGIN_REDIRECT_URL = '/home'
LOGIN_URL = '/login'

# Standardmäßiger Primärschlüssel-Feldtyp
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
