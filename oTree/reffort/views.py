from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

from django.http import JsonResponse

class MyPage(Page):

    timeout_seconds = 100000000000000000
    def vars_for_template(self):
        return {"ct": self.player.current_text()}


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.subsession.set_payoff()


class Results(Page):
    pass


page_sequence = [
    MyPage,
    ResultsWaitPage,
    Results
]


def validate_transcription(request):
    player_id = int(request.POST["player_id"])
    transcription = request.POST["transcription"].strip()
    player = models.Player.objects.filter(id=player_id).get()

    data = {}
    if player.is_transcription_accurate(transcription):
        data["transcription_ok"] = True
        data["new_text"] = player.current_image()
        data["current_text_idx"] = player.current_text_idx
    else:
        data["transcription_ok"] = False

    player.save()
    return JsonResponse(data)
