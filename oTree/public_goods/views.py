from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random


class MyPage(Page):

    form_model = models.Player
    #~ form_fields = ["contribution"]

    def get_form_fields(self):
        return ["contribution"]


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoff()


class Results(Page):

    def vars_for_template(self):
        average = (
            sum([p.contribution for p in self.group.get_players()]) /
            Constants.players_per_group)
        return {"average": average}



page_sequence = [
    MyPage,
    ResultsWaitPage,
    Results
]
