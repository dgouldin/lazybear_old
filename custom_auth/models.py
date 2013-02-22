# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone = models.CharField(max_length=255)
    mailing_list = models.BooleanField(default=False)

    def __unicode__(self):
        return ' '.join((self.first_name, self.last_name))
