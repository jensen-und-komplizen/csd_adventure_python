import re
import unittest

from src.loo.items.coffeemaker import CoffeeMaker


class TestCoffeeMaker(unittest.TestCase):

    def setUp(self):
        self.coffeemaker = CoffeeMaker()

    def tearDown(self):
        self.coffeemaker = None

    def test_coffeemaker_init(self):
        self.assertIsNotNone(self.coffeemaker)
        self.assertIsInstance(self.coffeemaker, CoffeeMaker)

    def test_coffeemaker_can_brew(self):
        self.assertTrue(self.coffeemaker.brew())

    def test_coffeemaker_can_display_error(self):
        self.assertEqual(self.coffeemaker.whats_wrong(), "")

    def test_coffeemaker_if_connected_to_power(self):
        self.assertFalse(self.coffeemaker.power_available)
        self.coffeemaker.connect_power()
        self.assertTrue(self.coffeemaker.power_available)

    def test_coffeemaker_can_add_coffee_beans(self):
        self.assertFalse(self.coffeemaker.coffee_in_the_machine)
        self.coffeemaker.add_coffee_beans()
        self.assertTrue(self.coffeemaker.coffee_in_the_machine)

    def test_coffeemaker_has_cup_in_the_machine(self):
        self.assertFalse(self.coffeemaker.cup_in_the_machine)
        self.coffeemaker.put_cup_in()
        self.assertTrue(self.coffeemaker.cup_in_the_machine)

    def test_coffeemaker_can_add_water(self):
        self.assertFalse(self.coffeemaker.water_in_the_machine)
        self.coffeemaker.add_water()
        self.assertTrue(self.coffeemaker.water_in_the_machine)

    def test_coffeemaker_has_available_commands(self):
        self.assertTrue(len(self.coffeemaker.list_commands()) > 0)

    def test_coffeemaker_cannot_make_coffee_without_power(self):
        self.assertFalse(self.coffeemaker.make_coffee())
        self.assertTrue(re.match(self.coffeemaker.error, "There is no power connected"))

    def test_coffeemaker_cannot_make_coffee_without_coffee(self):
        self.coffeemaker.connect_power()
        self.assertFalse(self.coffeemaker.make_coffee())
        self.assertTrue(re.match(self.coffeemaker.error, "There are no coffee beans in the machine"))

    def test_coffeemaker_cannot_make_coffee_without_a_cup(self):
        self.coffeemaker.connect_power()
        self.coffeemaker.add_coffee_beans()
        self.assertFalse(self.coffeemaker.make_coffee())
        self.assertTrue(re.match(self.coffeemaker.error, "There is no cup the machine"))

    def test_coffeemaker_cannot_make_coffee_without_water(self):
        self.coffeemaker.connect_power()
        self.coffeemaker.add_coffee_beans()
        self.coffeemaker.put_cup_in()
        self.assertFalse(self.coffeemaker.make_coffee())
        self.assertTrue(re.match(self.coffeemaker.error, "There is no water in the machine"))

    def test_coffeemaker_can_handle_add_beans_command(self):
        message = self.coffeemaker.handle("add beans")
        #self.assertTrue(self.coffeemaker.coffee_in_the_machine)
        self.assertEqual(message, "Beans have been added to the coffee machine.")
