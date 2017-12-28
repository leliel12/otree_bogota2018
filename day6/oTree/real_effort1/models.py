from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from jsonfield import JSONField

import Levenshtein as lev

import words



author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'real_effort1'
    players_per_group = None
    num_rounds = 1
    text_size = 5
    texts_number = 100
    min_distance_different_text = 10


class Subsession(BaseSubsession):

    texts = JSONField()

    def creating_session(self):
        texts = set()
        while len(texts) < Constants.texts_number:
            text = words.random_text(Constants.text_size)
            distances = [lev.distance(text, t) for t in texts]
            if not texts or min(distances) > Constants.min_distance_different_text:
                texts.add(text)
        self.texts = list(texts)


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    current_text_idx = models.IntegerField(default=0)

    def current_text(self):
        return self.subsession.texts[self.current_text_idx]