import uuid

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from django.db.models import UUIDField

from jsonfield import JSONField

from picklefield.fields import PickledObjectField

import Levenshtein as lev

import words

from .text2png import render


author = 'oTree Bogota Tutorial 2018'


doc = """
This game generate a random string of <b>5 english words</b> and
Every string must be a some Levenshtein distance of
the others. Also the game render this text as an image
"""


class Constants(BaseConstants):
    name_in_url = 'real_effort2'
    players_per_group = None
    num_rounds = 1
    timeout = None
    texts_number = 3
    text_size = 5  # words
    min_distance_different_text = 10

class Subsession(BaseSubsession):

    texts = JSONField()
    images = PickledObjectField()

    def creating_session(self):
        texts = []
        while len(texts) < Constants.texts_number:
            text = words.random_text(Constants.text_size)
            distances = [lev.distance(text, t) for t in texts]
            if not texts or min(distances) > Constants.min_distance_different_text:
                texts.append(text)
        self.texts = texts
        self.images = list(map(render, texts))

    def set_payoffs(self):
        players = self.get_players()
        payoff = sum([p.current_text_idx for p in players]) / len(players)
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

    def current_image(self):
        try:
            return self.subsession.images[self.current_text_idx]
        except IndexError:
            return None

    def is_transcription_accurate(self, transcription):
        text = self.current_text()
        if lev.distance(text, transcription) <= Constants.min_distance_different_text:
            self.current_text_idx += 1
            return True
        return False
