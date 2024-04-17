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

    def test_handle_unknown_command(self):
        hallway = Hallway()
        assert hallway.handle_command("unknown command") == "you wake up on the Loo.\nDid you just ask me to 'unknown command'<br /><br />404 - command not found. If you want to restart, just try to 'close eyes' or 'open your inventory' to open your inventory or try to 'look around' or 'use door to washroom'. Might help."
