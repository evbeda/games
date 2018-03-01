import unittest
from guess_number_game.test_guess_number_game import TestGuessNumberGame
from reversi.test_reversi import TestReversi
from connect_four_game.test_connect_four_game import TestConnectFourGame
from buscaminas.test_buscaminas import TestBuscamina
from test_game import TestGame
from damas.test import TestDamaGame


def suite():
    """
        Gather all the tests from this module in a test suite.
    """
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestReversi))
    test_suite.addTest(unittest.makeSuite(TestGuessNumberGame))
    test_suite.addTest(unittest.makeSuite(TestConnectFourGame))
    test_suite.addTest(unittest.makeSuite(TestBuscamina))
    test_suite.addTest(unittest.makeSuite(TestGame))
    test_suite.addTest(unittest.makeSuite(TestDamaGame))

    return test_suite


if __name__ == "__main__":
    unittest.main()
