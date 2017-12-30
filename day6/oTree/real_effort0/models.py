import uuid
import random
import string

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from django.db.models import UUIDField

from jsonfield import JSONField

import Levenshtein as lev

author = 'Your name here'

doc = """
Your app description
"""

class Constants(BaseConstants):
    name_in_url = 'real_effort0'
    players_per_group = None
    random_string_conf = {"numbers": 5, "letters": 15, "spaces": 5}
    num_rounds = 1
    timeout = 60
    texts_number = 100
    text_size = 5  # words
    min_distance_different_text = 10

class Subsession(BaseSubsession):

    texts = JSONField()

    def random_string(self, numbers, letters, spaces):
        numbers = [random.choice(string.digits) for _ in range(numbers)]
        letters = [random.choice(string.ascii_uppercase) for _ in range(letters)]
        spaces = [" "] * spaces
        rstring = numbers + letters + spaces
        random.shuffle(rstring)
        return " ".join("".join(rstring).strip().split())

    def creating_session(self):
        texts = []
        while len(texts) < Constants.texts_number:
            text = self.random_string(**Constants.random_string_conf)
            distances = [lev.distance(text, t) for t in texts]
            if not texts or min(distances) > Constants.min_distance_different_text:
                texts.append(text)
        self.texts = texts

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

    def is_transcription_accurate(self, transcription):
        text = self.current_text()
        if lev.distance(text, transcription) <= Constants.min_distance_different_text:
            self.current_text_idx += 1
            return True
        return False
