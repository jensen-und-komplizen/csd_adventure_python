import unittest

from src.loo.adventure import Adventure


class TestToiletPaper(unittest.TestCase):

    def test_pick_up(self):
        adventure = Adventure()
        response = adventure.tell("pick up toilet paper")
        assert "I am not going to pick that up" in response
        #todo: we need to assert that our inventory didn't add a new item
