# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
import os
from importlib import import_module

from .conf.settings.common import *

try:
    DJANGO_CONF = os.environ['DJANGO_CONF']
except KeyError:
    raise ValueError('DJANGO_CONF environment variable must be set!')

import_path = 'lazybear.conf.settings.{0}'.format(DJANGO_CONF)
module = import_module(import_path)
for k in dir(module):
    locals()[k] = getattr(module, k)
