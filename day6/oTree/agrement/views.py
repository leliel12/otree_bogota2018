from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_model = models.Player
    form_fields = ["gender", "accept_agreement"]

    def accept_agreement_error_message(self, value):
        if not value:
            return "You must accept!!!"

    def before_next_page(self):
        self.participant.vars["gender"] = self.player.gender


page_sequence = [
    MyPage,
]
