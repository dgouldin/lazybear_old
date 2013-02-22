# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import patterns, include, url

from .views import (dinner_group_default_reservation, dinner_group_reservation,
    thanks)

urlpatterns = patterns('',
    url(r'^$', dinner_group_default_reservation,
        name='dinner_group_default_reservation'),
    url(r'^(?P<dinner_group_id>\d+)/$', dinner_group_reservation,
        name='dinner_group_reservation'),
    url(r'^thanks/$', thanks, name='thanks'),
)
