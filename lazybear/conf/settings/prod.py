# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# AWS
AWS_ACCESS_KEY_ID = '19CH43SSGM2GDWRXQB02'
AWS_SECRET_ACCESS_KEY = 'hK/xG6yq6KDulsHwvp/p+LPs7+OtkeTGDfcvR23K'
AWS_STORAGE_BUCKET_NAME = 'lazybear'

MEDIA_URL = 'http://s3.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = MEDIA_URL
