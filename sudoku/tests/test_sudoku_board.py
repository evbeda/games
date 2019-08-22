import unittest
from parameterized import parameterized
from ..board import Board
from .. import (
    NOT_MODIFIABLE,
    REPEATED_ON_COLUMN,
    REPEATED_ON_ROW,
    REPEATED_ON_REGION,
    EXAMPLE_BOARD,
    FINISHED_EXAMPLE_BOARD,
    EXAMPLE_SHOWN_BOARD,
)


class TestSudokuBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board(EXAMPLE_BOARD)
        self.finished_board = Board(FINISHED_EXAMPLE_BOARD)

    def test_existing_numbers_are_not_modifiable(self):
        self.assertFalse(self.board.is_modifiable('A', 2))

    @parameterized.expand([
        ('a', 3),
        ('b', 7),
        ('c', 6),
        ('d', 5),
        ('f', 1),
        ('g', 4),
        ('h', 2),
        ('i', 9)
    ])
    def test_validate_insert_illegal_value_in_row(self, row, value):
        self.assertFalse(self.board.validate_row(row, value))

    @parameterized.expand([
        ('a', 1),
        ('b', 2),
        ('c', 5),
        ('d', 4),
        ('e', 3),
        ('f', 8),
        ('g', 7),
        ('h', 9),
        ('i', 6)
    ])
    def test_validate_insert_legal_value_in_row(self, row, value):
        self.assertTrue(self.board.validate_row(row, value))

    @parameterized.expand([
        (1, 1),
        (2, 3),
        (3, 2),
        (4, 6),
        (5, 9),
        (6, 6),
        (7, 8),
        (8, 4),
        (9, 7)
    ])
    def test_validate_insert_illegal_value_in_column(self, column, value):
        self.assertFalse(self.board.validate_column(column, value))

    @parameterized.expand([
        (1, 9),
        (2, 8),
        (3, 5),
        (4, 7),
        (5, 4),
        (6, 3),
        (7, 6),
        (8, 5),
        (9, 1)
    ])
    def test_validate_insert_legal_value_in_column(self, column, value):
        self.assertTrue(self.board.validate_column(column, value))

    @parameterized.expand([
        ('a', 1, 6),
        ('b', 4, 9),
        ('c', 8, 8),
        ('d', 1, 9),
        ('e', 4, 6),
        ('f', 9, 8),
        ('g', 2, 3),
        ('h', 4, 6),
        ('i', 7, 8)
    ])
    def test_validate_insert_illegal_value_in_region(self, row, column, value):
        self.assertFalse(self.board.validate_region(row, column, value))

    @parameterized.expand([
        ('a', 1, 1),
        ('b', 4, 1),
        ('c', 8, 1),
        ('d', 1, 8),
        ('e', 4, 7),
        ('f', 9, 1),
        ('g', 2, 4),
        ('h', 4, 1),
        ('i', 7, 4)
    ])
    def test_validate_insert_legal_value_in_region(self, row, column, value):
        self.assertTrue(self.board.validate_region(row, column, value))

    @parameterized.expand([
        ('a', 1, [" ", "6", " ", "5", "3", "7", " ", "4", " "]),
        ('b', 5, ["3", " ", " ", " ", "9", " ", " ", " ", "6"]),
        ('c', 8, ["8", " ", "4", " ", " ", " ", "3", " ", "7"]),
        ('d', 2, [" ", "9", " ", " ", " ", " ", "7", "1", "3"]),
        ('e', 4, [" ", "5", "1", " ", " ", " ", "6", "2", " "]),
        ('f', 9, ["2", "3", "8", " ", " ", " ", " ", "4", " "]),
        ('g', 3, ["3", " ", "6", " ", " ", " ", "1", " ", "2"]),
        ('h', 6, ["4", " ", " ", " ", "6", " ", " ", " ", "9"]),
        ('i', 7, [" ", "1", " ", "5", "2", "3", " ", "8", " "])
    ])
    def test_get_region(self, row, column, region):
        self.assertEqual(self.board.get_region(row, column), region)

    @parameterized.expand([
        (('a', 1), 2),
        (('b', 8), 6),
        (('c', 3), 8),
        (('d', 4), 7),
        (('e', 5), 4),
        (('f', 6), 8),
        (('g', 7), 7),
        (('h', 2), 8),
        (('i', 9), 6),
        (('e', 1), 8),
        (('g', 2), 5),
        (('e', 9), 1),
        (('a', 5), 7),
    ])
    def test_place_number_legally(self, coordinates, value):
        row, column = coordinates
        self.board.place(coordinates, value)
        self.assertEqual(self.board.board[row][column - 1]['val'], str(value))

    @parameterized.expand([
        (('a', 1), 3, REPEATED_ON_ROW),
        (('b', 8), 4, REPEATED_ON_COLUMN),
        (('c', 3), 7, REPEATED_ON_ROW),
        (('g', 2), 2, REPEATED_ON_REGION),
        (('f', 9), 8, REPEATED_ON_COLUMN),
        (('b', 8), 8, REPEATED_ON_REGION),
    ])
    def test_place_number_illegally(
            self, coordinates, value, message):

        row, column = coordinates
        with self.assertRaises(Exception) as raised:
            self.board.place(coordinates, value)
        self.assertIn(message, str(raised.exception))
        self.assertEqual(self.board.board[row][column - 1]['val'], ' ')

    @parameterized.expand([
        (('a', 2), 6),
        (('b', 5), 9),
        (('c', 9), 7),
        (('d', 2), 9),
        (('f', 3), 3),
        (('g', 8), 1),
        (('h', 7), 5),
    ])
    def test_place_number_already_set(self, coordinates, value):
        row, column = coordinates
        original_value = self.board.board[row][column - 1]['val']
        with self.assertRaises(Exception) as raised:
            self.board.place(coordinates, value)
        self.assertIn(NOT_MODIFIABLE, str(raised.exception))
        self.assertEqual(
            self.board.board[row][column - 1]['val'],
            original_value)

    @parameterized.expand([
        (('a', 1), 3, REPEATED_ON_ROW),
        (('b', 8), 4, REPEATED_ON_COLUMN),
        (('e', 1), 9, REPEATED_ON_REGION),
        (('a', 2), 1, NOT_MODIFIABLE),
    ])
    def test_validate_invalid_number(
            self, coordinates, value, message):
        with self.assertRaises(Exception) as raised:
            self.board.validate_number(coordinates, value)
        self.assertIn(message, str(raised.exception))

    def test_is_finished_for_an_unfinished_board(self):
        self.assertFalse(self.board.is_finished())

    def test_is_finished_for_a_finished_board(self):
        self.assertTrue(self.finished_board.is_finished())

    def test_board(self):
        self.assertEqual(EXAMPLE_SHOWN_BOARD, self.board.show_board())
