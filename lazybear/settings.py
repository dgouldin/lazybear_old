# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
import os
from importlib import import_module

from .conf.settings.common import *

# default conf to prod if env var not set
DJANGO_CONF = os.environ.get('DJANGO_CONF', 'prod')

import_path = 'lazybear.conf.settings.{0}'.format(DJANGO_CONF)
module = import_module(import_path)
for k in dir(module):
    locals()[k] = getattr(module, k)
