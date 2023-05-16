import unittest

from src.loo.rooms.loo import Loo


class TestLoo(unittest.TestCase):

    def test_greet(self):
        loo = Loo()
        assert loo.get_detailed_description() == f"""You see a pretty dirty <mark>door</mark>, with some nasty <mark>jokes</mark> on it. There are three pieces of <mark>toilet paper</mark> on the ground. Next to you are a <mark>coin</mark> and a few <mark>magazines</mark>. \n
        In your pocket you find a card that says you are a pathetic scrum developer, PSD"""
