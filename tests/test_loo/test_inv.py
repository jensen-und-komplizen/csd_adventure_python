import unittest
from src.loo.inv import Inv

class TestInv(unittest.TestCase):

    def test_inv(self):
        Inv.add_item(Inv, "fish")
        assert len(Inv.inventory_list) == 1

        

