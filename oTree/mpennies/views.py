from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Choice(Page):

    form_model = models.Player
    form_fields = ["tails"]

    def vars_for_template(self):
        return {
            "history": self.player.in_previous_rounds()}


class ResultWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoff()


class Results(Page):

    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds

    def vars_for_template(self):
        return {
            "total_payoff": self.player.participant.payoff,
            "paying_round": self.session.vars["paying_round"],
            "history": self.player.in_all_rounds()}



page_sequence = [
    Choice, ResultWaitPage, Results
]
