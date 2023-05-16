import unittest

from src.loo.adventure import Adventure


class TestJokes(unittest.TestCase):

    def test_jokes(self):
        adventure = Adventure()
        response = adventure.tell("read a joke")
        assert ";)" in response
