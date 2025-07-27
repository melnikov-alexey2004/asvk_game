import pytest

from src.MergeRequirements import bullscows

class TestLogic:

    @pytest.mark.parametrize('guess, secret, res', [('123', '123', (3, 3)),
                                                    ('000', '010', (2, 2)),
                                                    ('321', '123', (1, 3)),
                                                    ('4321', '1234', (0, 4)),
                                                    ('654321', '123456', (0, 6))],
                             ids=range(5))
    def test_parametrized(self, guess, secret, res):
        assert bullscows.bullscows(guess, secret) == res

    def test_again_some_cases(self):
        assert bullscows.bullscows('666666', '000000') == (0, 0)
        assert bullscows.bullscows('112233', '123456') == (1, 3)