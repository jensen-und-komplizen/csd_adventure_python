
from datetime import date, timedelta


class Dishwasher:

    brand = None
    model = None
    date_of_purchase = None
    date_when_warranty_ends = None

    max_number_of_plates = 12
    current_number_of_clean_plates_loaded = 0
    current_number_of_dirty_plates_loaded = 0

    max_number_of_cups = 12
    current_number_of_clean_cups_loaded = 0
    current_number_of_dirty_cups_loaded = 0

    max_number_of_forks = 12
    current_number_of_clean_forks_loaded = 0
    current_number_of_dirty_forks_loaded = 0

    max_number_of_knives = 12
    current_number_of_clean_knives_loaded = 0
    current_number_of_dirty_knives_loaded = 0

    max_number_of_spoons = 12
    current_number_of_clean_spoons_loaded = 0
    current_number_of_dirty_spoons_loaded = 0

    max_number_of_teaspoons = 12
    current_number_of_clean_teaspoons_loaded = 0
    current_number_of_dirty_teaspoons_loaded = 0

    def load_dirty_knives(self, number_of_dirty_knives):
        self.current_number_of_dirty_knives_loaded += number_of_dirty_knives
        return self.current_number_of_dirty_knives_loaded

    def could_load_cutlery(self, cutlery):
        self.current_number_of_dirty_knives_loaded += cutlery.the_total_amount_of_knives_that_are_in_the_kitchen_disregarding_their_state
        return self.current_number_of_dirty_knives_loaded <= self.max_number_of_knives

    def __init__(self):
        self.brand = "ACME"
        self.model = "Superswoosh 9000XR"
        self.date_of_purchase = date.today()

        # always add 180 days of warranty
        self.date_when_warranty_ends = self.date_of_purchase + timedelta(days=180)

    def start_cleaning_all_loaded_dirty_plates_and_cups_and_forks_and_knives_and_spoons_and_teaspoons(self):
        self.current_number_of_clean_plates_loaded = self.current_number_of_dirty_plates_loaded
        self.current_number_of_dirty_plates_loaded = 0

        self.current_number_of_clean_cups_loaded = self.current_number_of_dirty_cups_loaded
        self.current_number_of_dirty_cups_loaded = 0

        self.current_number_of_clean_forks_loaded = self.current_number_of_dirty_forks_loaded
        self.current_number_of_dirty_forks_loaded = 0

        self.current_number_of_clean_knives_loaded = self.current_number_of_dirty_knives_loaded
        self.current_number_of_dirty_knives_loaded = 0

        self.current_number_of_clean_spoons_loaded = self.current_number_of_dirty_spoons_loaded
        self.current_number_of_dirty_spoons_loaded = 0

        self.current_number_of_clean_teaspoons_loaded = self.current_number_of_dirty_teaspoons_loaded
        self.current_number_of_dirty_teaspoons_loaded = 0
