# -*- coding: utf-8 -*-
import sys,os
from os.path import join

ROOT = os.path.abspath(os.path.dirname(__file__))
# ! It is a good idea not to edit this and edit local_settings.py instead
# ! (copy local_settings.py.default to local_settings.py first)
# ! Especially if you want to update from version control system in future, because
# ! local_settings.py is not under version control

DEBUG = True
PRODUCTION = True
TEMPLATE_DEBUG = DEBUG

DATABASE_ENGINE = 'sqlite3'        # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'ado_mssql'.
DATABASE_NAME = join(ROOT, 'base.db')       # Or path to database file if using sqlite3.
DATABASE_USER = ''               # Not used with sqlite3.
DATABASE_PASSWORD = ''           # Not used with sqlite3.
DATABASE_HOST = ''               # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''               # Set to empty string for default. Not used with sqlite3.

# Absolute path to the directory that holds media.
# MEDIA_ROOT = '/var/www/opentodo_media'
MEDIA_ROOT = join(ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT.
# Note that this should have a trailing slash if it has a path component
# MEDIA_URL = 'http://media.myhost.ru' or MEDIA_URL = 'http://myhost.ru/media/'

MEDIA_URL = '/media/'
if not PRODUCTION:
    MEDIA_URL = 'http://localhost/media/opentodo/'

ADMIN_MEDIA_PREFIX = '/media/admin/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

SEND_EMAILS = False       # make it True and edit settings bellow if you want to receive emails
EMAIL_HOST = ''           # smtp.myhost.com
EMAIL_HOST_USER = ''      # user123
EMAIL_HOST_PASSWORD = ''  # qwerty
EMAIL_ADDRESS_FROM = ''   # noreply@myhost.com
if DEBUG:
    EMAIL_FAIL_SILENTLY = False
else:
    EMAIL_FAIL_SILENTLY = True

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'ih^s_r3qgx!8-7aj%7^tqg#mj&zpdmchbbc=+*9=y#cm&v(ga)'

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL= '/'

sys.path.append(ROOT)
sys.path.append(ROOT + '/apps')

TEMPLATE_DIRS = (
    ROOT + '/templates'
)

TIME_ZONE = 'Europe/Moscow'
LANGUAGE_CODE = 'ru'

SITE_ID = 1
USE_I18N = True

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'todo.middleware.Custom403Middleware',
)
FILE_CHARSET = 'utf-8'

SESSION_SAVE_EVERY_REQUEST = False

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'context_processors.host',
    'context_processors.my_media_url',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'todo',
    'beautils',
    'superadmin',
)

# add handy tools from python-django-extensions if available
try:
    import django_extensions
    INSTALLED_APPS = INSTALLED_APPS + ('django_extensions',)
except ImportError:
    pass

##################################################################################
# You can create local_settings.py to override the settings.
# It is recomended to put all your custom settings (database, path, etc.) there
# if you want to update from Subversion in future.
##################################################################################
try:
    from local_settings import *
except ImportError:
    pass