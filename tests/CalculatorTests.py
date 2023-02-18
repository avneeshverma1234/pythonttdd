import unittest

from src.Calcular import Calculator


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator();

    def test_add_is_successful(self):
        self.assertEqual(self.calculator.add(2,2), 4,"Return value should be 4")

    def test_subtract_is_successful(self):
        self.assertEqual(self.calculator.subtract(5,4),1, "Result should be 1")

if __name__ == '__main__':
    try:
        from teamcity import is_running_under_teamcity
        from teamcity.unittestpy import TeamcityTestRunner

        if is_running_under_teamcity():
            runner = TeamcityTestRunner()
        else:
            runner = unittest.TextTestRunner()
    except ModuleNotFoundError:
        runner = unittest.TextTestRunner()
    unittest.main(testRunner=runner)
