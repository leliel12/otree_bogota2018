from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):

    def vars_for_template(self):
        return {
            "text": self.player.current_text()}


class Results(Page):
    pass


page_sequence = [
    MyPage,
    Results
]
