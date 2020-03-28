#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 19:10:16 2019
@author: Daniel Mutuba
"""

from django.conf.urls import url
from api.apps.profiles.views import UserProfileView


urlpatterns = [
    url(r'^profile', UserProfileView.as_view()),
]
