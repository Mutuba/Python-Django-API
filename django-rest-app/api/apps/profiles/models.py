#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
import uuid
from django.db import models
from api.apps.user.models import User


class UserProfile(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=50, unique=False)
    last_name = models.CharField(max_length=50, unique=False)
    phone_number = models.CharField(
        max_length=10, unique=True, null=False, blank=False)
    age = models.PositiveIntegerField(null=False, blank=False)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.user.email

    class Meta:
        '''
        to set table name in database
        '''
        db_table = "profile"
        ordering = (
            'last_name', 'first_name')


...

# python manage.py startapp accounts
# class MyModel(models.Model):
#     ...

#     MONTH_CHOICES = [(str(i), calendar.month_name[i]) for i in range(1, 13)]

#     month = models.CharField(max_length=9, choices=MONTH_CHOICES, default=1)


# class MyModel(models.Model):
#     class Month(models.TextChoices):
#         JAN = "JANUARY"
#         FEB = "FEBRUARY"
#         MAR = "MAR"
#         # (...)

#     month = models.CharField(
#         max_length=2,
#         choices=Month.choices,
#         default=Month.JAN
#     )


# class MyModel(models.Model):

#     JAN = "JANUARY"
#     FEB = "FEBRUARY"
#     MAR = "MAR"
#     # (...)

#     MONTH = (
#         (JAN, "January"),
#         (FEB, "February"),
#         (MAR, "March")
#     )
#     month = models.CharField(
#         max_length=3,
#         choices=MONTH,
#         default=MONTH.JAN,
#     )

# minty_vanilla_cones = IceCream.objects.filter(
# scoops__contained_by=[MINT, VANILLA])
