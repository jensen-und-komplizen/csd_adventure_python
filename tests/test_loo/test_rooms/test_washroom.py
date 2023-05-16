import unittest

from src.loo.rooms.wash_room import WashRoom


class TestWashroom(unittest.TestCase):

    def test_greet(self):
        washroom = WashRoom()
        assert washroom.get_detailed_description() == "You see a coin on the floor. " + "<br/>" + "You also see an incredibly nasty sink with an undefinable substance in it. Ew!" + "<br/>" + "You notice a <mark>DoD</mark> on the door." + "</br>" + "On the other side of the room you see another <mark>door</mark>." + "</br>" + "Oh, and there's a blockchain in the corner. Interesting.."
