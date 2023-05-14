# simple unit test
import sys
sys.path.append('../')

# simple unit test
# from great_main import greeting
from greet_main import greeting


def test_greeting():
    # greet_name = 'Dade'
    # g = greeting(greet_name)
    # assert g == 'Hello Dade'
    assert greeting('Dade') == 'Hello Dade'

