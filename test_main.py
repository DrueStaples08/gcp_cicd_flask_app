# simple unit test
from greet_main import greeting

def test_greeting():
    greet_name = 'Dade'
    g = greeting(greet_name)
    assert g == 'Hello Dade'
