"""
Django settings for Heimdall project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_poj(nb4$tqopb^2ppd6*@$0+_+xkm!_hq#8&34l8k*f#r8y3$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
HOST = '192.168.0.151:8080'
LOGIN_URL = '/'

# Application definition

INSTALLED_APPS = [
    # Own Apps
    #'documentationmanagement.apps.DocumentationmanagementConfig',
    'main.apps.MainConfig',
    #'personalmanagement.apps.PersonalmanagementConfig',
    #'productmanagement.apps.ProductmanagementConfig',
    #'relationshipmanagement.apps.RelationshipmanagementConfig',
    'storagemanagement.apps.StoragemanagementConfig',
    #'structuremanagement.apps.StructuremanagementConfig',
    #'tools.apps.ToolsConfig',
    # Installed Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third Party Apps
    'tinymce',
    'rest_framework',
    'qr_code',
    'django_filters',
]

TINYMCE_DEFAULT_CONFIG = {
    "theme": "silver",
    "height": 500,
    "menubar": True,
    "plugins": "advlist,autolink,lists,link,image,charmap,print,preview,anchor,"
    "searchreplace,visualblocks,code,fullscreen,insertdatetime,media,table,paste,"
    "code,help,wordcount"
    "powerpaste a11ychecker tinymcespellchecker linkchecker wordcount table advtable editimage autosave advlist anchor advcode image link lists media mediaembed searchreplace visualblocks template autoresize",
    "toolbar": "undo redo | formatselect | "
    "bold italic backcolor | alignleft aligncenter "
    "alignright alignjustify | bullist numlist outdent indent | "
    "removeformat | help",
}

SERVE_QR_CODE_IMAGE_PATH = 'qr-code-image/'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework_datatables.renderers.DatatablesRenderer',
    ),
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework_datatables.pagination.DatatablesPageNumberPagination',
    'PAGE_SIZE': 50,
}

X_FRAME_OPTIONS = 'SAMEORIGIN'
ROOT_URLCONF = 'Heimdall.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR,"main/templates"),
            os.path.join(BASE_DIR,"documentationmanagement/"),
            os.path.join(BASE_DIR,"documentationmanagement/templates"),
            os.path.join(BASE_DIR,"personalmanagement/templates"),
            os.path.join(BASE_DIR,"processmanagement/templates"),
            os.path.join(BASE_DIR,"productmanagement/templates"),
            os.path.join(BASE_DIR,"programs/templates"),
            # relationshipmanagement
            os.path.join(BASE_DIR,"relationshipmanagement/templates"),
            os.path.join(BASE_DIR,"relationshipmanagement/company/templates"),
            os.path.join(BASE_DIR,"relationshipmanagement/customer/templates"),
            os.path.join(BASE_DIR,"relationshipmanagement/general/templates"),
            os.path.join(BASE_DIR,"relationshipmanagement/person/templates"),
            os.path.join(BASE_DIR,"relationshipmanagement/supplier/templates"),
            os.path.join(BASE_DIR,"relationshipmanagement/companyitem/templates"),
            # storagemanagement
            os.path.join(BASE_DIR,"storagemanagement/templates"),
            os.path.join(BASE_DIR,"storagemanagement/booking/templates"),
            os.path.join(BASE_DIR,"storagemanagement/company/templates"),
            os.path.join(BASE_DIR,"storagemanagement/companycontact/templates"),
            os.path.join(BASE_DIR,"storagemanagement/companyitem/templates"),
            os.path.join(BASE_DIR,"storagemanagement/offer/templates"),
            os.path.join(BASE_DIR,"storagemanagement/offerdata/templates"),
            os.path.join(BASE_DIR,"storagemanagement/order/templates"),
            os.path.join(BASE_DIR,"storagemanagement/orderdata/templates"),
            os.path.join(BASE_DIR,"storagemanagement/requestdata/templates"),
            os.path.join(BASE_DIR,"storagemanagement/storage/templates"),
            os.path.join(BASE_DIR,"storagemanagement/storageitem/templates"),
            # structuremanagement
            os.path.join(BASE_DIR,"structuremanagement/"),
            os.path.join(BASE_DIR,"structuremanagement/templates"),
            os.path.join(BASE_DIR,"structuremanagement/process/templates"),
            
            os.path.join(BASE_DIR,"media"),
            os.path.join(BASE_DIR,"visualisation/templates"),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'Heimdall.wsgi.application'

#AUTH_USER_MODEL = 'app_label.ModelName'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'de-de'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,"static") ,
    # documentationmanagement
    os.path.join(BASE_DIR,"documentationmanagement/direction/js"),
    os.path.join(BASE_DIR,"documentationmanagement/document/js"),
    os.path.join(BASE_DIR,"documentationmanagement/file/js"),
    os.path.join(BASE_DIR,"documentationmanagement/formular/js"),
    os.path.join(BASE_DIR,"documentationmanagement/general/js"),
    os.path.join(BASE_DIR,"documentationmanagement/manual/js"),
    os.path.join(BASE_DIR,"documentationmanagement/picture/js"),
    os.path.join(BASE_DIR,"documentationmanagement/processinstruction/js"),
    os.path.join(BASE_DIR,"documentationmanagement/protocol/js"),
    os.path.join(BASE_DIR,"documentationmanagement/safetydatasheet/js"),
    os.path.join(BASE_DIR,"documentationmanagement/technicaldatasheet/js"),
    os.path.join(BASE_DIR,"documentationmanagement/workingdescription/js"),
    os.path.join(BASE_DIR,"documentationmanagement/workinginstruction/js"),
    # relationshipmanagement
    os.path.join(BASE_DIR,"relationshipmanagement/company/js"),
    os.path.join(BASE_DIR,"relationshipmanagement/customer/js"),
    os.path.join(BASE_DIR,"relationshipmanagement/general/js"),
    os.path.join(BASE_DIR,"relationshipmanagement/person/js"),
    os.path.join(BASE_DIR,"relationshipmanagement/supplier/js"),
    os.path.join(BASE_DIR,"relationshipmanagement/ware/js"),
    # storagemanagement
    os.path.join(BASE_DIR,"storagemanagement/booking/js"),
    os.path.join(BASE_DIR,"storagemanagement/company/js"),
    os.path.join(BASE_DIR,"storagemanagement/companycontact/js"),
    os.path.join(BASE_DIR,"storagemanagement/companyitem/js"),
    os.path.join(BASE_DIR,"storagemanagement/offer/js"),
    os.path.join(BASE_DIR,"storagemanagement/offerdata/js"),
    os.path.join(BASE_DIR,"storagemanagement/order/js"),
    os.path.join(BASE_DIR,"storagemanagement/orderdata/js"),
    os.path.join(BASE_DIR,"storagemanagement/requestdata/js"),
    os.path.join(BASE_DIR,"storagemanagement/storage/js"),
    os.path.join(BASE_DIR,"storagemanagement/storageitem/js"),
    # structuremanagement
    os.path.join(BASE_DIR,"structuremanagement/device/js"),
    os.path.join(BASE_DIR,"structuremanagement/department/js"),
    os.path.join(BASE_DIR,"structuremanagement/error/js"),
    os.path.join(BASE_DIR,"structuremanagement/group/js"),
    os.path.join(BASE_DIR,"structuremanagement/maintenance/js"),
    os.path.join(BASE_DIR,"structuremanagement/position/js") ,
    os.path.join(BASE_DIR,"structuremanagement/process/js") ,
    os.path.join(BASE_DIR,"structuremanagement/section/js"),
    os.path.join(BASE_DIR,"structuremanagement/status/js"),
    #os.path.join(BASE_DIR,"CompanyStructure/static"),
    #os.path.join(BASE_DIR,"Machines/static"),
    #os.path.join(BASE_DIR,"processmanagement/static"),
    #os.path.join(BASE_DIR,"programs/static"),
    #os.path.join(BASE_DIR,"visualisation/static"),
    #os.path.join(BASE_DIR,"storage/static"),
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')
MEDIA_URL = '/media/'

REST_FRAMEWORK = {
    #'DEFAULT_FILTER_BACKENDS': ['rest_framework.filters.DjangoFilterBackend',],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.web.de'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'tim.machate@web.de'
EMAIL_HOST_USER = 'tim.machate@web.de'
EMAIL_HOST_PASSWORD = 'Ra3uCh3rma3nnCh3n'