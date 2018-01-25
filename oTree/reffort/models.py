from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import os
import random
import string

import Levenshtein as lev

from jsonfield import JSONField

from picklefield.fields import PickledObjectField

from . import text2png

PATH = os.path.abspath(os.path.dirname(__file__))

WORDS_PATH = os.path.join(PATH, "words_alpha.txt")

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'reffort'
    players_per_group = None
    num_rounds = 1

    timeout = 10
    words_number = 5
    texts_number = 100
    min_distance_different_text = 10

    words = [w.strip() for w in open(WORDS_PATH).readlines()]


class Subsession(BaseSubsession):

    texts = JSONField()
    images = PickledObjectField()

    #~ def random_string(self, numbers, letters, spaces):
        #~ numbers = [random.choice(string.digits) for _ in range(numbers)]
        #~ letters = [random.choice(string.ascii_uppercase) for _ in range(letters)]
        #~ spaces = [" "] * spaces
        #~ rstring = numbers + letters + spaces
        #~ random.shuffle(rstring)
        #~ return " ".join("".join(rstring).strip().split())

    def creating_session(self):
        for p in self.players:
            texts, imgs = [], []
            while len(texts) < Constants.texts_number:
                text = " ".join(
                    random.sample(Constants.words, Constants.words_number))
                distances = [lev.distance(text, t) for t in texts]
                if not texts or min(distances) > Constants.min_distance_different_text:
                    img = text2png.render(text)
                    texts.append(text)
                    imgs.append(img)
            p.texts = texts
            p.images = imgs

    def set_payoff(self):
        """This implement a tournament"""
        from collections import Counter
        players = self.get_players()
        cnt = Counter({p: p.current_text_idx for p in players})
        for p, payoff in cnt.most_common(3):
            p.payoff = c(payoff)



class Group(BaseGroup):
    pass


class Player(BasePlayer):

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
