import unittest
from guess_number_game.test_guess_number_game import TestGuessNumberGame
from reversi.test_reversi import TestReversi
from connect_four_game.test_connect_four_game import TestConnectFourGame


def suite():
    """
        Gather all the tests from this module in a test suite.
    """
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestReversi))
    test_suite.addTest(unittest.makeSuite(TestGuessNumberGame))
    test_suite.addTest(unittest.makeSuite(TestConnectFourGame))
    return test_suite


if __name__ == "__main__":
    unittest.main()
