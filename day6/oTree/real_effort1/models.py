import uuid

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from django.db.models import UUIDField

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
    timeout = 60
    texts_number = 100
    text_size = 5  # words
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

    def set_payoffs(self):
        players = self.get_players()
        payoff = sum([p.current_text_idx + 1 for p in players]) / len(players)
        for p in players:
            p.payoff = payoff


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    token = UUIDField(default=uuid.uuid4, editable=False)
    end = models.BooleanField(default=False)
    current_text_idx = models.IntegerField(default=0)

    def current_text(self):
        try:
            return self.subsession.texts[self.current_text_idx]
        except IndexError:
            return None

    def is_transcription_accurate(self, transcription):
        text = self.current_text()
        if lev.distance(text, transcription) <= Constants.min_distance_different_text:
            self.current_text_idx += 1
            return True
        return False
