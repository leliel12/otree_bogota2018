#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^validate_transcription/$',
        views.validate_transcription, name='validate_transcription'),
]
