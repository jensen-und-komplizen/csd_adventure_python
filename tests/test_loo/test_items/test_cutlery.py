import unittest

from src.loo.items.cutlery import Cutlery


class TestCutlery(unittest.TestCase):

    def test_cutlery_init(self):
        cutlery = Cutlery(0)
        self.assertIsNotNone(cutlery)

    def test_knives_calculation(self):
        cutlery = Cutlery(2)
        self.assertEqual(cutlery.the_total_amount_of_knives_that_are_in_the_kitchen_disregarding_their_state, 2)
