# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from datetime import datetime

from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect

from .forms import ReservationForm, ReservationUserForm
from .models import DinnerGroup

def dinner_group_default_reservation(request):
    now = datetime.now()
    try:
        dinner_group = DinnerGroup.objects.filter(
            reservations_open__lte=now,
            reservations_close__gt=now,
        )[0]
    except IndexError:
        raise Http404

    return redirect(dinner_group_reservation, dinner_group.id)

def dinner_group_reservation(request, dinner_group_id):
    now = datetime.now()
    dinner_group = get_object_or_404(DinnerGroup,
        pk=dinner_group_id,
        reservations_open__lte=now,
        reservations_close__gt=now,
    )

    if request.method == 'POST':
        form = ReservationForm(dinner_group, data=request.POST)
        user_form = ReservationUserForm(data=request.POST)
        if form.is_valid() and user_form.is_valid():
            user = user_form.save()
            reservation = form.save(user)
            return redirect(thanks)
    else:
        form = ReservationForm(dinner_group)
        user_form = ReservationUserForm()

    return render(request, 'dinners/dinner_group_reservation.html', {
        'form': form,
        'user_form': user_form,
    })

def thanks(request):
    return render(request, 'dinners/thanks.html')

