# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib import admin
from .models import Dinner, DinnerGroup, Reservation, ReservationDinner

class DinnerInline(admin.TabularInline):
    model = Dinner

class DinnerGroupAdmin(admin.ModelAdmin):
    model = DinnerGroup

    inlines = (
        DinnerInline,
    )

class ReservationDinnerInline(admin.TabularInline):
    model = ReservationDinner

class ReservationAdmin(admin.ModelAdmin):
    model = Reservation
    raw_id_fields = ('dinner_group',)

    inlines = (
        ReservationDinnerInline,
    )

admin.site.register(DinnerGroup, DinnerGroupAdmin)
admin.site.register(Reservation, ReservationAdmin)
