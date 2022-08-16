import unittest
from .buscaminas import Buscaminas


class TestBuscamina(unittest.TestCase):

    def setUp(self):
        self.game = Buscaminas()
        self.game._board = []
        self.game.create_board(' ')
        self.game.set_value(1, 1, 'B')
        self.game.set_value(2, 4, 'B')
        self.game.set_value(1, 2, 'B')
        self.game.set_value(3, 4, 'B')
        self.game.set_value(4, 3, 'B')
        self.game.set_value(2, 1, 'B')
        self.game.set_value(5, 3, 'B')
        self.game.set_value(3, 5, 'B')
        self.game.set_value(6, 1, 'B')
        self.game.set_value(7, 2, 'B')

    def test_initial_status(self):
        self.assertTrue(self.game.is_playing)

    def test_check_lose(self):
        self.assertTrue(self.game.check_lose(2, 4))
        self.assertFalse(self.game.check_lose(1, 3))
        self.assertEqual(
            self.game.play(4, 3),
            '*********** You Lose ***********'
        )

    def test_check_win(self):
        game = Buscaminas()

        for i in range(8):
            for j in range(8):
                if game.get_value(i, j) != 'B':
                    game.play(i, j)

        self.assertEqual(
            game.play(1, 1),
            '*********** You Win ***********')
        self.assertTrue(game.check_win())

    def test_game_over(self):
        self.game.play(1, 1)
        self.assertEqual(
            '*********** Game Over ************',
            self.game.play(2, 3))
        self.assertEqual(
            '*********** Game Over ************',
            self.game.next_turn())

    def test_check_keep_playing(self):
        self.assertEqual("Keep playing", self.game.play(2, 2))

    def test_board(self):
        result = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', 'B', 'B', ' ', ' ', ' ', ' ', ' '],
            [' ', 'B', ' ', ' ', 'B', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', 'B', 'B', ' ', ' '],
            [' ', ' ', ' ', 'B', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', 'B', ' ', ' ', ' ', ' '],
            [' ', 'B', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'B', ' ', ' ', ' ', ' ', ' '],
        ]

        self.assertEqual(result, self.game._board)

    def test_two_clicks_7_7_place(self):
        self.game.play(7, 7,)

    def test_two_clicks_same_place(self):
        self.game.play(1, 3,)
        self.assertEqual('Position selected yet', self.game.play(1, 3, ))

    def test_count_bombs_in_board(self):
        self.game.play(2, 2, )
        self.assertEqual('3', self.game.get_value(2, 2))

    def test_check_invalid_movement(self):
        with self.assertRaises(Exception) as e:
            self.game.play(-1, 8)
            self.assertEqual(e.exception.message, "Movement not allowed.",)
