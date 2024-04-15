import unittest

from src.loo.adventure import Adventure


class TestJokes(unittest.TestCase):

    def test_jokes(self) -> None:
        adventure = Adventure()
        response = adventure.tell("read a joke")
        assert ";)" in response

    def test_end_of_jokes(self) -> None:
        adventure = Adventure()
        for i in range(len(adventure.jokes)):
            _: str = adventure.tell("read a joke")

        response = adventure.tell("read a joke")
        assert response == "You've read them all. Go again? ;)"

    def test_reread_jokes(self) -> None:
        adventure = Adventure()
        for i in range(len(adventure.jokes)):
            _: str = adventure.tell("read a joke")

        _: str = adventure.tell("read a joke")
        response: str = adventure.tell("yes")
        assert response in adventure.jokes
        assert len(adventure.jokes) == len(adventure.jokes_temp) + 1  # 1 joke already printed

    def test_dont_reread_jokes(self) -> None:
        adventure = Adventure()
        for i in range(len(adventure.jokes)):
            _: str = adventure.tell("read a joke")

        _: str = adventure.tell("read a joke")
        response: str = adventure.tell("no")
        assert response == "Ok, suit yourself."
        assert len(adventure.jokes_temp) == 0
