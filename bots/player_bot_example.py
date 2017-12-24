from . import views
from otree.api import Bot, SubmissionMustFail

class PlayerBot(Bot):

    cases = ['basic', 'min', 'max']

    def play_round(self):
        yield (views.Introduction)

        if self.case == 'basic':
            assert self.player.payoff == None

        if self.case == 'basic':
            if self.player.id_in_group == 1:
                for invalid_contribution in [-1, 101]:
                    yield SubmissionMustFail(
                        views.Contribute,
                        {'contribution': invalid_contribution})
        contributions = {
            'min': 0,
            'max': 100,
            'basic': 50}
        contribution = [self.case]

        yield (views.Contribute, {"contribution": contribution})
        yield (views.Results)

        if self.player.id_in_group == 1:

            if self.case == 'min':
                expected_payoff = 110
            elif self.case == 'max':
                expected_payoff = 190
            else:
                expected_payoff = 150
            assert self.player.payoff == expected_payoff
