# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf import settings
from django.db import models

class DinnerGroup(models.Model):
    cost = models.DecimalField(decimal_places=2, max_digits=6)
    reservations_open = models.DateTimeField()
    reservations_close = models.DateTimeField()

    def __unicode__(self):
        return 'Dinner Group: {0} to {1}'.format(
            self.reservations_open,
            self.reservations_close,
        )

class Dinner(models.Model):
    date = models.DateField()
    dinner_group = models.ForeignKey(DinnerGroup, related_name='dinners')

    def __unicode__(self):
        return 'Dinner: {0}'.format(self.date)

class Reservation(models.Model):
    MIN_PARTY_SIZE = 1
    MAX_PARTY_SIZE = 6

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reservations')
    dinner_group = models.ForeignKey(DinnerGroup, related_name='reservations')
    party_size = models.IntegerField(
        choices=[(i, i) for i in range(MIN_PARTY_SIZE, MAX_PARTY_SIZE + 1)])
    other_names = models.CharField(max_length=1024)
    manual_review = models.BooleanField(default=False)
    dietary_restrictions = models.TextField(blank=True)
    notes = models.TextField(blank=True)

    class Meta:
        unique_together = (
            ('user', 'dinner_group'),
        )

    def __unicode__(self):
        return 'Reservation by User {0} for Dinner Group {1}'.format(
            self.user_id,
            self.dinner_group_id,
        )

class ReservationDinner(models.Model):
    reservation = models.ForeignKey(Reservation)
    dinner = models.ForeignKey(Dinner)
    first_choice = models.BooleanField(default=False)

    class Meta:
        unique_together = (
            ('reservation', 'dinner'),
        )

    def __unicode__(self):
        return 'Reservation {0} chooses Dinner {1}'.format(
            self.reservation_id,
            self.dinner_id,
        )
