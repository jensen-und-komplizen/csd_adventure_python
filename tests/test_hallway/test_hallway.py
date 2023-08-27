import unittest
from src.loo.rooms.hallway import Hallway
from src.loo.rooms.loo import Loo


class TestHallway(unittest.TestCase):

    def test_description(self):
        hallway = Hallway()
        assert hallway.get_description() == "You enter a hallway that looks dark."

    def test_detailed_description(self):
        hallway = Hallway()
        assertion = "On the other side of the hall you see a door leading to a team room." + "</br>" + \
                    "There is a door to the washroom."
        assert hallway.get_detailed_description() == assertion

    def test_get_help(self):
        hallway = Hallway()
        assertion = "try to 'look around' or 'use door to washroom'. Might help."
        assert True
