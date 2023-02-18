import unittest

from src.Calcula import Calculator


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator();

    def test_something(self):
        self.assertEqual(self.calculator.add(2,2), 4,"Return value should be 4")


if __name__ == '__main__':
    unittest.main()
