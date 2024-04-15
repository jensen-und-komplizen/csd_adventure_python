import unittest

from src.loo.adventure import Adventure


class TestJokes(unittest.TestCase):

    def test_jokes(self):
        adventure = Adventure()
        response = adventure.tell("read a joke")
        assert ";)" in response

    def test_end_of_jokes(self):
        adventure = Adventure()
        for i in range(len(adventure.jokes)):
            res = adventure.tell("read a joke")
        
        response = adventure.tell("read a joke")
        assert response == "You've read them all ;)"
