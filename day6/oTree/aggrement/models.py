from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'oTree Bogota Tutorial 2018'

doc = """
A simple aggrement with gender-selection combo box.
"""


class Constants(BaseConstants):
    name_in_url = 'aggrement'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    accept_aggrement = models.BooleanField()
    gender = models.CharField(choices=[
        'Agender',
        'Androgyne',
        'Androgynes',
        'Androgynous',
        'Asexual',
        'Bigender',
        'Cis',
        'Cis Female',
        'Cis Male',
        'Cis Man',
        'Cis Woman',
        'Cisgender',
        'Cisgender Female',
        'Cisgender Male',
        'Cisgender Man',
        'Cisgender Woman',
        'F2M',
        'FTM',
        'Female to Male',
        'Female to male trans man',
        'Female to male transgender man',
        'Female to male transsexual man',
        'Gender Fluid',
        'Gender Nonconforming',
        'Gender Questioning',
        'Gender Variant',
        'Gender neutral',
        'Genderqueer',
        'Hermaphrodite',
        'Intersex',
        'Intersex man',
        'Intersex person',
        'Intersex woman',
        'M2F',
        'MTF',
        'Male to Female',
        'Male to female trans woman',
        'Male to female transgender woman',
        'Male to female transsexual woman',
        'Man',
        'Neither',
        'Neutrois',
        'Non-binary',
        'Other',
        'Pangender',
        'Polygender',
        'T* man',
        'T* woman',
        'Trans',
        'Trans Female',
        'Trans Male',
        'Trans Man',
        'Trans Person',
        'Trans*Female',
        'Trans*Male',
        'Trans*Man',
        'Trans*Person',
        'Trans*Woman',
        'Transexual',
        'Transexual Female',
        'Transexual Male',
        'Transexual Man',
        'Transexual Person',
        'Transexual Woman',
        'Transgender Female',
        'Transgender Person',
        'Transmasculine',
        'Two* person',
        'Two-spirit',
        'Two-spirit person',
        'Woman'])
