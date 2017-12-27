#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random

PATH = os.path.abspath(os.path.dirname(__file__))

# download from https://github.com/dwyl/english-words
WORDS_PATH = os.path.join(PATH, "words_alpha.txt")

_words = None


def get_words():
    global _words
    if _words is None:
        with open(WORDS_PATH) as fp:
            _words = tuple(l.strip() for l in fp.readlines())
    return _words

def random_text(nwords):
    all_words = get_words()
    sample = random.sample(all_words, nwords)
    return " ".join(sample)
