# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django import forms
from django.contrib.auth import get_user_model

from .models import Reservation, ReservationDinner
from lazybear.utils import update_or_create

User = get_user_model()

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = (
            'party_size',
            'other_names',
            'manual_review',
            'dietary_restrictions',
            'notes',
        )

    def __init__(self, dinner_group, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)

        self.dinner_group = dinner_group
        self.dinners = list(dinner_group.dinners.all())
        choices = [(d.id, d.date.strftime('%A, %m/%d')) for d in self.dinners]

        self.fields.update({
            'first_choice': forms.ChoiceField(choices=choices,
                widget=forms.RadioSelect),
            'other_choices': forms.MultipleChoiceField(choices=choices,
                widget=forms.CheckboxSelectMultiple),
        })

    confirmation_email = forms.BooleanField(required=False)

    def save(self, user):
        reservation = super(ReservationForm, self).save(commit=False)
        reservation.user = user
        reservation.dinner_group = self.dinner_group
        reservation.save()

        # populate reservation:dinner m2ms
        first_choice = self.cleaned_data['first_choice']
        ReservationDinner.objects.create(reservation=reservation,
            first_choice=True, dinner_id=first_choice)
        for other_choice in self.cleaned_data['other_choices']:
            if other_choice == first_choice:
                continue # don't record first choice twice
            ReservationDinner.objects.create(reservation=reservation,
                dinner_id=other_choice)

        # TODO: send email if desired
        return reservation


class ReservationUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'mailing_list',
            'phone',
        )

    def save(self):
        data = self.cleaned_data.copy()
        email = data.pop('email')

        # try to identify the user via email, otherwise create a new one
        user, created = update_or_create(User.objects, email=email,
            defaults=data)
        return user

