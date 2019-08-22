import unittest
from .test_bets import TestBets
from .test_craps import TestCraps
from .test_turn import TestTurn


def suite():
    test_suite = unittest.TestSuite()
    # SUDOKU
    test_suite.addTest(unittest.makeSuite(TestBets))
    test_suite.addTest(unittest.makeSuite(TestCraps))
    test_suite.addTest(unittest.makeSuite(TestTurn))
    return test_suite
