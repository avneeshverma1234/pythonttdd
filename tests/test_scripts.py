import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


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
