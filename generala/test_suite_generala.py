import unittest
from .TestCategories import TestCategories
from .TestThrowDice import TestThrowDice
from .TestPlayer import TestPlayer
from .TestGame import TestGenerala
from .test_throw_class import TestThrow


def suite():
    """
        Gather all the tests from this module in a test suite.
    """
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestCategories))
    test_suite.addTest(unittest.makeSuite(TestThrowDice))
    test_suite.addTest(unittest.makeSuite(TestPlayer))
    test_suite.addTest(unittest.makeSuite(TestGenerala))
    test_suite.addTest(unittest.makeSuite(TestThrow))
    return test_suite


if __name__ == "__main__":
    unittest.main()
