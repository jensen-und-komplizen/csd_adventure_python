import unittest

from src.demo.calc import add


class TestCalc(unittest.TestCase):

	def test_add(self):
		result = add(1, 2)
		assert result == 3


if __name__ == '__main__':
	unittest.main()
	