import unittest
from .test_bets import (
    TestBetsRoulette,
    TestBetCreator,
)
from .test_croupier import TestCroupier
from .integration_test import IntegrationTest
from .test_ruleta import TestBoard, TestRoulette


def suite():
    test_suite = unittest.TestSuite()
    # ROULETTE
    test_suite.addTest(unittest.makeSuite(TestBetsRoulette))
    test_suite.addTest(unittest.makeSuite(TestBetCreator))
    test_suite.addTest(unittest.makeSuite(TestRoulette))
    test_suite.addTest(unittest.makeSuite(TestCroupier))
    test_suite.addTest(unittest.makeSuite(IntegrationTest))
    test_suite.addTest(unittest.makeSuite(TestBoard))

    return test_suite
