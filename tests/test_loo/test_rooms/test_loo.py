import unittest

from src.loo.rooms.loo import Loo


class TestLoo(unittest.TestCase):

    def test_greet(self):
        loo = Loo()
        assert loo.get_detailed_description() == f"""You see a pretty dirty <mark>door</mark>, with some nasty <mark>jokes</mark> on it. There are three pieces of <mark>toilet paper</mark> on the ground. Next to you are a <mark>coin</mark> and a few <mark>magazines</mark>. \n
        In your pocket you find a card that says you are a pathetic scrum developer, PSD"""

    def test_handle(self):
        loo = Loo()
        assert loo.handle_command("look at the door") == "It looks like the door to the washroom. Oh yes, lets flush out some bugs!"

    def test_description_not_stiff(self):
        loo = Loo()
        description = loo.get_description()
        assert "but at least you have your inventory" not in description
        assert description != ""
        assert isinstance(description, str)

    def test_handle_unknown_command(self):
        loo = Loo()
        assert loo.handle_command("unknown command") == "you wake up on the Loo.\nDid you just ask me to 'unknown command'<br /><br />404 - command not found. If you want to restart, just try to 'close eyes' or 'open your inventory' to open your inventory or try to 'look around', 'look at magazines' (better get your gloves), 'grab coin', 'look at toilet paper', 'pick up toilet paper', 'read a joke' or just 'use door to washroom' to escape the smell."