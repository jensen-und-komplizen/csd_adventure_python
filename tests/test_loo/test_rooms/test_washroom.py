import unittest

from src.loo.rooms.wash_room import WashRoom


class TestWashroom(unittest.TestCase):

    def test_greet(self):
        washroom = WashRoom()
        assert washroom.get_detailed_description() == "You see an incredibly nasty sink with an undefinable substance in it. Ew!" + "<br/>" + "You notice a DoD on the door." + "</br>" + "On the other side of the room you see another door." + "</br>" + "Oh, and there's a blockchain in the corner. Interesting.."
