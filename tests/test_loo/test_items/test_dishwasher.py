import unittest

from datetime import date, timedelta
from src.loo.items.dishwasher import Dishwasher
from src.loo.items.cutlery import Cutlery


class TestDishwasher(unittest.TestCase):

    def setUp(self):
        self.dishwasher = Dishwasher()

    def tearDown(self):
        self.dishwasher = None

    def test_dishwasher_init(self):
        self.assertEqual(self.dishwasher.brand, "ACME")
        self.assertEqual(self.dishwasher.model, "Superswoosh 9000XR")
        self.assertEqual(self.dishwasher.date_of_purchase, date.today())
        self.assertEqual(self.dishwasher.date_when_warranty_ends, date.today() + timedelta(days=180))
        self.assertEqual(self.dishwasher.max_number_of_plates, 12)
        self.assertEqual(self.dishwasher.current_number_of_clean_plates_loaded, 0)
        self.assertEqual(self.dishwasher.current_number_of_dirty_plates_loaded, 0)
        self.assertEqual(self.dishwasher.max_number_of_cups, 12)
        self.assertEqual(self.dishwasher.current_number_of_clean_cups_loaded, 0)
        self.assertEqual(self.dishwasher.current_number_of_dirty_cups_loaded, 0)
        self.assertEqual(self.dishwasher.max_number_of_forks, 12)
        self.assertEqual(self.dishwasher.current_number_of_clean_forks_loaded, 0)
        self.assertEqual(self.dishwasher.current_number_of_dirty_forks_loaded, 0)
        self.assertEqual(self.dishwasher.max_number_of_knives, 12)
        self.assertEqual(self.dishwasher.current_number_of_clean_knives_loaded, 0)
        self.assertEqual(self.dishwasher.current_number_of_dirty_knives_loaded, 0)
        self.assertEqual(self.dishwasher.max_number_of_spoons, 12)
        self.assertEqual(self.dishwasher.current_number_of_clean_spoons_loaded, 0)
        self.assertEqual(self.dishwasher.current_number_of_dirty_spoons_loaded, 0)
        self.assertEqual(self.dishwasher.max_number_of_teaspoons, 12)
        self.assertEqual(self.dishwasher.current_number_of_clean_teaspoons_loaded, 0)
        self.assertEqual(self.dishwasher.current_number_of_dirty_teaspoons_loaded, 0)

    def test_dishwasher_load_dirty_knives(self):
        self.assertEqual(self.dishwasher.current_number_of_dirty_knives_loaded, 0)
        self.dishwasher.load_dirty_knives(2)
        self.assertEqual(self.dishwasher.current_number_of_dirty_knives_loaded, 2)

    def test_dishwasher_could_load_dirty_knives(self):
        cutlery = Cutlery(10)
        self.assertTrue(self.dishwasher.could_load_cutlery(cutlery))

    def test_dishwasher_could_not_load_dirty_knives(self):
        cutlery = Cutlery(25)
        self.assertFalse(self.dishwasher.could_load_cutlery(cutlery))

    def test_dishwasher_is_cleaning(self):
        self.assertEqual(self.dishwasher.current_number_of_dirty_knives_loaded, 0)
        self.assertEqual(self.dishwasher.current_number_of_clean_knives_loaded, 0)
        self.dishwasher.load_dirty_knives(11)
        self.assertEqual(self.dishwasher.current_number_of_dirty_knives_loaded, 11)
        self.assertEqual(self.dishwasher.current_number_of_clean_knives_loaded, 0)
        self.dishwasher.start_cleaning_all_loaded_dirty_plates_and_cups_and_forks_and_knives_and_spoons_and_teaspoons()
        self.assertEqual(self.dishwasher.current_number_of_dirty_knives_loaded, 0)
        self.assertEqual(self.dishwasher.current_number_of_clean_knives_loaded, 11)
