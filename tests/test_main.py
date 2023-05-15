# Unit Tests which are automatically ran with Github Actions
import sys
sys.path.append('../')
from greet_main import greeting


def test_greeting():
    # greet_name = 'Dade'
    # g = greeting(greet_name)
    # assert g == 'Hello Dade'
    assert greeting('Dade') == 'Hello Dade'

