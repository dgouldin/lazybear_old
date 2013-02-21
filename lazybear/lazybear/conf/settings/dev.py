# -*- coding: utf-8 -*-
from __future__ import unicode_literals

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'lazybear',
        'USER': 'lazybear',
        'PASSWORD': 'lazybear',
        'HOST': '',
        'PORT': '',
    }
}

MEDIA_URL = '/media/'
STATIC_URL = '/static/'
