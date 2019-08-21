import unittest
from game import GameBattleship

from .board import Board


class TestBoard(unittest.TestCase):
    def test_inicial(self):
        board = Board()
        cont = 0
        for y in range(0, board.cols):
            for x in range(0, board.rows):
                cont += board.get_value(x, y)
        self.assertEqual(cont, 0)

    def test_insert(self):
        board = Board()
        board.set_boat(2, 3, 1, "horizontal")
        result = board.get_value(2, 3)
        self.assertEqual(result, 1)

    def test_insert_three_horizontal_ship(self):
        board = Board()
        board.set_boat(0, 7, 3, "horizontal")
        result1 = board.get_value(0, 7)
        result2 = board.get_value(0, 8)
        result3 = board.get_value(0, 9)
        self.assertEqual(result1, 31)
        self.assertEqual(result2, 31)
        self.assertEqual(result3, 31)

    def test_insert_five_vertifcal_ship(self):
        board = Board()
        board.set_boat(3, 4, 5, "vertical")
        result1 = board.get_value(3, 4)
        result2 = board.get_value(4, 4)
        result3 = board.get_value(5, 4)
        result4 = board.get_value(6, 4)
        result5 = board.get_value(7, 4)
        self.assertEqual(result1, 5)
        self.assertEqual(result2, 5)
        self.assertEqual(result3, 5)
        self.assertEqual(result4, 5)
        self.assertEqual(result5, 5)

    def test_check_position_false(self):
        board = Board()
        result = board.check_position(10, 10, 1, "horizontal")
        self.assertFalse(result)

    def test_error_position(self):
        board = Board()
        result = board.set_boat(10, 10, 1, "horizontal")
        self.assertEqual(result, False)

    def test_error_position_four_horizontal_ship(self):
        board = Board()
        result = board.set_boat(8, 7, 4, "horizontal")
        self.assertFalse(result)

    def test_error_position_five_vertical_ship(self):
        board = Board()
        result = board.set_boat(7, 7, 5, "vertical")
        self.assertFalse(result)

    def test_error_position_already_has_ship_vertical(self):
        board = Board()
        board.set_boat(3, 3, 4, "vertical")
        result = board.set_boat(4, 3, 2, "vertical")
        self.assertFalse(result)

    def test_error_position_already_has_ship_horizontal(self):
        board = Board()
        board.set_boat(2, 2, 4, "horizontal")
        result = board.set_boat(2, 3, 2, "vertical")
        self.assertFalse(result)

    def test_error_position_not_vertical_position(self):
        board = Board()
        result = board.set_boat(8, 8, 5, "vertical")
        self.assertFalse(result)

    def test_error_position_not_horizontal_position(self):
        board = Board()
        result = board.set_boat(8, 8, 5, "horizontal")
        self.assertFalse(result)

    def test_error_boat_already_set(self):
        board = Board()
        board.set_boat(0, 0, 1, "horizontal")
        board.set_boat(1, 1, 2, "horizontal")
        board.set_boat(2, 2, 3, "horizontal")
        board.set_boat(3, 3, 3, "horizontal")
        board.set_boat(4, 4, 4, "horizontal")
        board.set_boat(5, 5, 5, "horizontal")
        result1 = board.check_boat(1)
        result2 = board.check_boat(2)
        result3 = board.check_boat(3)
        result4 = board.check_boat(4)
        result5 = board.check_boat(5)
        self.assertEqual(result1, 9)
        self.assertEqual(result2, 9)
        self.assertEqual(result3, 9)
        self.assertEqual(result4, 9)
        self.assertEqual(result5, 9)

    def test_turn_hit(self):
        board = Board()
        board.set_boat(3, 3, 4, "vertical")
        result = board.shoot(4, 3)
        continue_turn = board.turn_decision_hit(result)
        self.assertTrue(continue_turn)

    def test_board_mark_shoot_hit(self):
        board = Board()
        board.mark_shoot(0, 0, True)
        board_expected = [
            ['x', 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        self.assertEqual(board.board, board_expected)

    def test_board_mark_shoot_water(self):
        board = Board()
        board.mark_shoot(0, 0, False)
        board_expected = [
            ['-', 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        self.assertEqual(board.board, board_expected)

    def test_turn_water(self):
        board = Board()
        board.set_boat(3, 3, 4, "vertical")
        result = board.shoot(1, 2)
        continue_turn = board.turn_decision_hit(result)
        self.assertFalse(continue_turn)

    def test_there_are_boats(self):
        board = Board()
        board.set_boat(1, 1, 1, "vertical")
        self.assertTrue(board.there_are_boats())
        board.shoot(1, 1)
        self.assertFalse(board.there_are_boats())


if __name__ == '__main__':
    unittest.main()
