import pytest
import bullscows

def test_bullscows_fun():
    assert bullscows.bullscows("ропот", "полип") == (1, 2)
    assert bullscows.bullscows("ворон", "просто") == (0, 3)
    assert bullscows.bullscows("11111", "12345") == (1, 1)
    assert bullscows.bullscows("12233", "12345") == (2, 3)

@pytest.mark.parametrize('guess, secret, res', [('112233', '999999', (0, 0)),
                                              ('777777', '112233', (0, 0)),
                                              ('112222', '121212', (3, 5))], ids=range(3))
def test_again(guess, secret, res):
    assert bullscows.bullscows(guess, secret) == res

@pytest.fixture(scope='function')
def default_secret_word():
    return '112233'

def test_logic_again(default_secret_word):
    assert bullscows.bullscows('000000', default_secret_word) == (0, 0)