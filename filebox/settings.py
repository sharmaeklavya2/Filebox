import os
import sys

PROJECT_NAME = 'filebox'
PROJECT_TITLE = 'Filebox'
CONF_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(CONF_DIR)
CONF_DIR_NAME = os.path.relpath(CONF_DIR, BASE_DIR)

SECRET_KEY = '!n#nyg-%_&t8q5o9rh9fh)uot(2zjj(dx48iyw#kfdsr!4_bmm'
DEBUG = True
ALLOWED_HOSTS = ['*']

X_FRAME_OPTIONS = 'DENY'

FILE_COUNT_LIM = 10
FOLDER_SIZE_LIM = 100*1024*1024

try:
	with open(os.path.join(CONF_DIR, "local", "file_count_lim.txt")) as _file_count_lim_file:
		FILE_COUNT_LIM = int(_file_count_lim_file.read().strip())
except (OSError, ValueError):
	pass
try:
	with open(os.path.join(CONF_DIR, "local", "folder_size_lim.txt")) as _folder_size_lim_file:
		FOLDER_SIZE_LIM = int(_folder_size_lim_file.read().strip())
except (OSError, ValueError):
	pass
try:
	with open(os.path.join(CONF_DIR, "local", "secret_key.txt")) as _secret_key_file:
		SECRET_KEY = _secret_key_file.read().strip()
		DEBUG = False
except OSError:
	print("Using default secret key (this is insecure)", file=sys.stderr)

# Application definition

#INSTALLED_APPS = ('django.contrib.staticfiles',)

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = CONF_DIR_NAME+'.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [os.path.join(BASE_DIR,'templates')],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
			],
		},
	},
]

WSGI_APPLICATION = CONF_DIR_NAME+'.wsgi.application'

# Database

DATABASES = {}

# Internationalization

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)

#STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
FILE_UPLOAD_TEMP_DIR = os.path.join(BASE_DIR, 'media_temp')
