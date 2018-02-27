import unittest
from guess_number_game.test_guess_number_game import TestGuessNumberGame
from reversi.test_reversi import TestReversi


def suite():
    """
        Gather all the tests from this module in a test suite.
    """
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestReversi))
    test_suite.addTest(unittest.makeSuite(TestGuessNumberGame))
    return test_suite


if __name__ == "__main__":
    unittest.main()
