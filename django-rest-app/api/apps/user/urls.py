#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 14:04:16 2019
@author: Daniel Mutuba
"""
from django.conf.urls import url
from api.apps.user.views import UserRegistrationView, UserLoginView


urlpatterns = [
    url(r'^signup', UserRegistrationView.as_view()),
    url(r'^signin', UserLoginView.as_view()),
]
