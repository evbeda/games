
import unittest
from game_base import GameWithBoard


class TestGameBase(unittest.TestCase):

    def setUp(self):
        self.game_with_board = GameWithBoard()

    def test_board_creation(self):
        self.game_with_board.cols = 8
        self.game_with_board.rows = 8
        result = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ]
        self.game_with_board.create_board(' ')
        self.assertEquals(result, self.game_with_board.get_board)

    def test_set_get_value(self):
        self.game_with_board.cols = 3
        self.game_with_board.rows = 3
        self.game_with_board.create_board(' ')
        self.game_with_board.set_value(1, 1, 'P')
        self.assertEquals('P', self.game_with_board.get_value(1, 1))

    def test_out_board_max(self):
        self.game_with_board.cols = 3
        self.game_with_board.rows = 3
        self.game_with_board.create_board(' ')
        self.assertFalse(self.game_with_board.in_board(3, 3))

    def test_in_board_min(self):
        self.game_with_board.cols = 3
        self.game_with_board.rows = 3
        self.game_with_board.create_board(' ')
        self.assertTrue(self.game_with_board.in_board(0, 0))

    def test_in_board_max(self):
        self.game_with_board.cols = 3
        self.game_with_board.rows = 3
        self.game_with_board.create_board(' ')
        self.assertTrue(self.game_with_board.in_board(2, 2))


if __name__ == "__main__":
    unittest.main()
