import unittest

from src.loo.rooms.wash_room import WashRoom


class TestWashroom(unittest.TestCase):

    def test_greet(self):
        washroom = WashRoom()
        assert washroom.get_detailed_description() == """You see a <mark>coin</mark> on the floor. \n
        You also see an incredibly nasty sink with an undefinable substance in it. Ew! \n
        You notice a <mark>DoD</mark> on the door. \n
        On the other side of the room you see two doors, one <mark>door</mark> to the hallway and another one to the loo. \n
        Oh, and there's a <mark>blockchain</mark> in the corner. Interesting.."""

    def test_blockchain(self):
        washroom = WashRoom()
        assert washroom.handle_command("grab blockchain") == "Nice, now I have a blockchain in my pocket. Maybe I will become a Crpyto millionaire?!"

    def test_has_items(self):
        washroom = WashRoom()

        assert washroom.dod is not None
        assert washroom.door is not None
        assert washroom.blockchain is not None
        assert washroom.coin is not None
