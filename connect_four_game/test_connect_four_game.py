import unittest
from connect_four_game import ConnectFourGame


class TestConnectFourGame(unittest.TestCase):

    def setUp(self):
        self.game = ConnectFourGame()

    def test_initial_game_status(self):
        self.assertTrue(self.game.is_playing)

    # fixme-connectfour-2: Spanish?
    def test_turno(self):
        turn_white = self.game.next_turn()
        self.assertEqual(turn_white, 'White plays')

    # fixme-connectfour-8: Woard?
    def test_initial_Woard_status(self):
        self.assertEqual(
            self.game.board,
            'EEEEEEE\n'
            'EEEEEEE\n'
            'EEEEEEE\n'
            'EEEEEEE\n'
            'EEEEEEE\n'
            'EEEEEEE\n'
        )

    def test_first_move_first_column(self):
        self.assertTrue(self.game.is_playing)
        self.game.play(0)
        self.assertEqual(
            self.game.board,
            'EEEEEEE\n'
            'EEEEEEE\n'
            'EEEEEEE\n'
            'EEEEEEE\n'
            'EEEEEEE\n'
            'WEEEEEE\n',
        )

    def test_second_move_first_column(self):
        self.assertTrue(self.game.is_playing)
        self.game.play(0)
        self.game.play(0)
        self.assertEqual(
            self.game.board,
            'EEEEEEE\n'
            'EEEEEEE\n'
            'EEEEEEE\n'
            'EEEEEEE\n'
            'BEEEEEE\n'
            'WEEEEEE\n',
        )

    def test_full_column(self):
        self.game.play(0)
        self.game.play(0)
        self.game.play(0)
        self.game.play(0)
        self.game.play(0)
        self.game.play(0)
        self.assertTrue(self.game.is_playing)
        self.assertEqual('Full column', self.game.play(0))

    def test_win_vertical(self):
        self.game.play(0)
        self.game.play(1)
        self.game.play(0)
        self.game.play(1)
        self.game.play(0)
        self.game.play(1)
        self.assertEquals('You win', self.game.play(0))
        self.assertEqual(
            self.game.board,
            'EEEEEEE\n'
            'EEEEEEE\n'
            'WEEEEEE\n'
            'WBEEEEE\n'
            'WBEEEEE\n'
            'WBEEEEE\n',
        )

    def test_win_horizontal(self):
        self.game.play(0)
        self.game.play(0)
        self.game.play(1)
        self.game.play(1)
        self.game.play(2)
        self.game.play(2)
        self.assertEquals('You win', self.game.play(3))
        self.assertEqual(
            self.game.board,
            'EEEEEEE\n'
            'EEEEEEE\n'
            'EEEEEEE\n'
            'EEEEEEE\n'
            'BBBEEEE\n'
            'WWWWEEE\n',
        )

    # fixme-connectfour-10: test name unclear
    def test_win_diagonalD(self):
        # fixme-connectfour-9: Remove white spaces
        self.game.play(0)

        self.game.play(1)

        self.game.play(1)

        self.game.play(2)

        self.game.play(2)

        self.game.play(3)

        self.game.play(2)

        self.game.play(3)

        self.game.play(3)

        self.game.play(0)

        self.assertEquals('You win', self.game.play(3))

        self.assertEqual(
            self.game.board,
            'EEEEEEE\n'
            'EEEEEEE\n'
            'EEEWEEE\n'
            'EEWWEEE\n'
            'BWWBEEE\n'
            'WBBBEEE\n',
        )

    # fixme-connectfour-2: Spanish?
    def test_empate(self):

        self.game.board_status = [
            ['W', 'W', 'B', 'W', 'B', 'B', 'B'],
            ['B', 'B', 'W', 'B', 'B', 'W', 'W'],
            ['W', 'W', 'B', 'B', 'W', 'B', 'W'],
            ['B', 'W', 'W', 'W', 'B', 'W', 'B'],
            ['W', 'B', 'B', 'W', 'W', 'W', 'B'],
            ['W', 'B', 'W', 'B', 'B', 'B', 'W'],
        ]

        self.assertEqual('Empate', self.game.play(0))
        self.assertEqual(True, self.game.empate())
        self.assertEqual(False, self.game.is_playing)

    def test_wrong_set_1(self):
        self.assertEqual('Movimiento no permitido', self.game.play(-1))
        self.assertEqual(
            self.game.board,
            'EEEEEEE\n'
            'EEEEEEE\n'
            'EEEEEEE\n'
            'EEEEEEE\n'
            'EEEEEEE\n'
            'EEEEEEE\n'
        )
        self.assertEqual(True, self.game.is_playing)

    def test_wrong_set_2(self):
        self.assertEqual('Movimiento no permitido', self.game.play(9))
        self.assertEqual(
            self.game.board,
            'EEEEEEE\n'
            'EEEEEEE\n'
            'EEEEEEE\n'
            'EEEEEEE\n'
            'EEEEEEE\n'
            'EEEEEEE\n'
        )
        self.assertEqual(True, self.game.is_playing)

    def test_wrong_set_3(self):
        self.assertEqual('Movimiento no permitido', self.game.play('a'))
        self.assertEqual(
            self.game.board,
            'EEEEEEE\n'
            'EEEEEEE\n'
            'EEEEEEE\n'
            'EEEEEEE\n'
            'EEEEEEE\n'
            'EEEEEEE\n'
        )
        self.assertEqual(True, self.game.is_playing)


if __name__ == "__main__":
    unittest.main()
