import unittest
from guess_number_game.test_guess_number_game import TestGuessNumberGame
from hanoi_towers.test_hanoi_towers import TestHanoiTower
from reversi.test_reversi import TestReversi
from connect_four_game.test_connect_four_game import TestConnectFourGame
from buscaminas.test_buscaminas import TestBuscamina
from test_game import TestGame
from damas.test import TestDamaGame
from tateti.test_tateti import TestTateti
from test_game_base import TestGameBase
from four_number.test_four_number import TestFourNumber
from generala.test_game import test_generala as test_game_generala
from generala.test_categories import test_categories
from generala.test_player import test_player
from generala.test_throw_class import test_throw_class
from generala.test_throw_dice import test_throw_dice
from blackjack.test_blackjack import (
    TestBets,
    TestDeck,
    TestGame as TestBlackjackGame,
    TestHands,
)
from poker.test_poker import (
    PokerTest,
    PokerGameTest,
)
from battleship.test_battleship import TestBattleship
from battleship.test_board import TestBoard
from sudoku.tests.test_suite_sudoku import suite as sudoku_suite
from craps.craps_suite import suite as craps_suite
from ruleta.tests.test_roulette_suite import suite as roulette_suite
from dungeon_raiders.tests.test_suite_dungeon import suite as dungeon_suite
from senku.test_senku import TestSenku
from ahorcado.test_ahorcado import TestAhorcado


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
    test_suite.addTest(unittest.makeSuite(TestTateti))
    test_suite.addTest(unittest.makeSuite(TestGameBase))
    test_suite.addTest(unittest.makeSuite(TestFourNumber))
    test_suite.addTest(unittest.makeSuite(test_game_generala))
    test_suite.addTest(unittest.makeSuite(test_categories))
    test_suite.addTest(unittest.makeSuite(test_player))
    test_suite.addTest(unittest.makeSuite(test_throw_class))
    test_suite.addTest(unittest.makeSuite(test_throw_dice))
    test_suite.addTest(unittest.makeSuite(TestBets))
    test_suite.addTest(unittest.makeSuite(TestDeck))
    test_suite.addTest(unittest.makeSuite(TestBlackjackGame))
    test_suite.addTest(unittest.makeSuite(TestHands))
    test_suite.addTest(unittest.makeSuite(PokerTest))
    test_suite.addTest(unittest.makeSuite(PokerGameTest))
    test_suite.addTest(unittest.makeSuite(TestBattleship))
    test_suite.addTest(unittest.makeSuite(TestBoard))
    test_suite.addTest(craps_suite())
    test_suite.addTest(sudoku_suite())
    test_suite.addTest(roulette_suite())
    test_suite.addTest(dungeon_suite())
    test_suite.addTest(unittest.makeSuite(TestSenku))
    test_suite.addTest(unittest.makeSuite(TestAhorcado))
    test_suite.addTest(unittest.makeSuite(TestHanoiTower))
    return test_suite


if __name__ == "__main__":
    alltests = unittest.TestSuite()
    alltests.addTest(suite())
    unittest.TextTestRunner().run(alltests)
