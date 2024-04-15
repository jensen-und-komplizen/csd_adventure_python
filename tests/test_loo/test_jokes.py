import unittest

from parameterized import parameterized

from src.loo.adventure import Adventure


class TestJokes(unittest.TestCase):

    @parameterized.expand(
        [
            "read a joke",
            "read joke",
            "joke",
            "look at joke",
        ]
    )
    def test_jokes(self, command: str):
        adventure = Adventure()
        response = adventure.tell(command)
        assert ";)" in response

    def test_jokes_fails(self):
        adventure = Adventure()
        response = adventure.tell("tell me a joke")
        assert "404" in response

    @parameterized.expand(
        [
            "read a joke",
            "read joke",
            "joke",
            "look at joke",
        ]
    )
    def test_end_of_jokes(self, command):
        adventure = Adventure()
        for i in range(len(adventure.jokes)):
            _ = adventure.tell(command)
        
        response = adventure.tell(command)
        assert response == "You've read them all ;)"
