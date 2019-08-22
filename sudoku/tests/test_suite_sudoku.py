import unittest
from .test_sudoku_board import TestSudokuBoard
from .test_sudoku_game import TestSudokuGame
from .test_api import TestSudokuApi


def suite():
    test_suite = unittest.TestSuite()
    # SUDOKU
    test_suite.addTest(unittest.makeSuite(TestSudokuBoard))
    test_suite.addTest(unittest.makeSuite(TestSudokuGame))
    test_suite.addTest(unittest.makeSuite(TestSudokuApi))
    return test_suite