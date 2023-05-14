import unittest

from src.loo.colleagues.pizza_the_hut import PizzaTheHut


class TestPizzaTheHut(unittest.TestCase):

    def test_greet(self):
        pizza_the_hut = PizzaTheHut()
        assert pizza_the_hut.greet() == "Pizza The Hut is greeting you friendly: Hello dear friend! Want to have a slice of my pizza?"


if __name__ == '__main__':
    unittest.main()
