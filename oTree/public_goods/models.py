from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'public_goods'
    players_per_group = 3
    num_rounds = 1
    endowment = c(100)
    multiplier = 2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):

    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()

    def set_payoff(self):
        players = self.get_players()
        self.total_contribution = sum([player.contribution for player in players])
        self.individual_share = (
            self.total_contribution * Constants.multiplier / Constants.players_per_group)
        for player in players:
            player.payoff = Constants.endowment - player.contribution + self.individual_share


class Player(BasePlayer):

    contribution = models.CurrencyField(
        min=0, max=Constants.endowment)
