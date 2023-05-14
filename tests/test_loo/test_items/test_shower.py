import unittest

from src.loo.items.shower import Shower


class TestShower(unittest.TestCase):

    def setUp(self):
        self.shower = Shower()

    def tearDown(self):
        self.shower = None

    def test_shower_init(self):
        self.assertEqual(self.shower.get_condition(), Shower.CONDITION_NEW)
        self.assertFalse(self.shower.turned_on)

    def test_shower_init_with_condition(self):
        shower = Shower(Shower.CONDITION_NEW)
        self.assertEqual(shower.get_condition(), Shower.CONDITION_NEW)
        shower = Shower(Shower.CONDITION_USED)
        self.assertEqual(shower.get_condition(), Shower.CONDITION_USED)
        shower = Shower(Shower.CONDITION_DEFECT)
        self.assertEqual(shower.get_condition(), Shower.CONDITION_DEFECT)

    def test_shower_set_condition(self):
        self.assertEqual(self.shower.get_condition(), Shower.CONDITION_NEW)
        self.shower.set_condition("Blubb")
        self.assertEqual(self.shower.get_condition(), "Blubb")

    def test_shower_get_condition(self):
        self.assertEqual(self.shower.get_condition(), Shower.CONDITION_NEW)

    def test_shower_can_be_turned_on(self):
        self.assertFalse(self.shower.turned_on)
        self.shower.turn_on()
        self.assertTrue(self.shower.turned_on)

    def test_shower_can_be_turned_off(self):
        self.assertFalse(self.shower.turned_on)
        self.shower.turn_on()
        self.assertTrue(self.shower.turned_on)
        self.shower.turn_off()
        self.assertFalse(self.shower.turned_on)

    def test_shower_is_turned_on(self):
        self.assertEqual(self.shower.is_turned_on(), False)

    def test_shower_is_turned_off(self):
        self.assertEqual(self.shower.is_turned_off(), not self.shower.turned_on)
