#!/usr/bin/env python
# -*- coding: utf-8 -*-

import uuid

from django.http import JsonResponse
from django.views.decorators.http import require_POST

from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):

    timeout_seconds = Constants.timeout

    def before_next_page(self):
        self.player.end = True


class Waiting(WaitPage):

    def after_all_players_arrive(self):
        self.subsession.set_payoffs()


class Results(Page):
    pass


page_sequence = [
    MyPage,
    Waiting,
    Results
]

# =============================================================================
# AJAX
# =============================================================================

@require_POST
def validate_transcription(request):
    player_token = request.POST["player_token"]
    transcription = request.POST["transcription"].strip()
    player = models.Player.objects.filter(
        token=player_token, end=False).get()

    data = {}
    if player.is_transcription_accurate(transcription):
        data['transcription_ok'] = True
        data['new_text'] = player.current_text()
        data['current_text_idx'] = player.current_text_idx
    else:
        data['transcription_ok'] = False

    player.save()

    return JsonResponse(data)
