from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import math, random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'mpennies'
    players_per_group = 2
    num_rounds = 4
    stakes = c(100)
    even_inc = 1 if num_rounds % 2 == 0 else 0
    half_way = math.ceil(num_rounds / 2) + even_inc


class Subsession(BaseSubsession):

    def creating_session(self):
        if self.round_number == 1:
            paying_round = random.randint(1, Constants.num_rounds)
            self.session.vars["paying_round"]  = paying_round
        elif self.round_number == Constants.half_way:
            matrix = self.get_group_matrix()
            for row in matrix:
                row.reverse()
            self.set_group_matrix(matrix)
        elif self.round_number > Constants.half_way:
            self.group_like_round(Constants.half_way)


class Group(BaseGroup):

    def set_payoff(self):
        matcher = self.get_player_by_role("Matcher")
        mismatcher = self.get_player_by_role("Mismatcher")
        #~ if matcher.tails == mismatcher.tails:
            #~ matcher.is_winner = True
            #~ mismatcher.is_winner = False
        #~ else:
            #~ matcher.is_winner = False
            #~ mismatcher.is_winner = True
        matcher.is_winner = matcher.tails == mismatcher.tails
        mismatcher.is_winner = not matcher.is_winner

        pround = self.session.vars["paying_round"]
        for player in [matcher, mismatcher]:
            if self.subsession.round_number == pround and player.is_winner:
                player.payoff = Constants.stakes
            else:
                player.payoff = c(0)



class Player(BasePlayer):

    tails = models.BooleanField(choices=[
        (True, "Tails"), (False, "Heads")])
    is_winner = models.BooleanField()

    def role(self):
        if self.id_in_group == 1:
            return "Mismatcher"
        return "Matcher"
