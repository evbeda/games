import unittest
from .connect_four_game import ConnectFourGame


class TestConnectFourGame(unittest.TestCase):

    def setUp(self):
        self.game = ConnectFourGame()

    def test_initial_game_status(self):
        self.assertTrue(self.game.is_playing)

    def test_turn(self):
        turn_white = self.game.next_turn()
        self.assertEqual(turn_white, 'White plays')

    # fixme-connectfour-8: Woard?
    def test_initial_Woard_status(self):
        self.assertEqual(
            self.game.board,
            '       \n'
            '       \n'
            '       \n'
            '       \n'
            '       \n'
            '       \n'
        )

    def test_first_move_first_column(self):
        self.assertTrue(self.game.is_playing)
        self.game.play(0)
        self.assertEqual(
            self.game.board,
            '       \n'
            '       \n'
            '       \n'
            '       \n'
            '       \n'
            'W      \n',
        )

    def test_second_move_first_column(self):
        self.assertTrue(self.game.is_playing)
        self.game.play(0)
        self.game.play(0)
        self.assertEqual(
            self.game.board,
            '       \n'
            '       \n'
            '       \n'
            '       \n'
            'B      \n'
            'W      \n',
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
        self.assertEqual('You win', self.game.play(0))
        self.assertEqual(
            self.game.board,
            '       \n'
            '       \n'
            'W      \n'
            'WB     \n'
            'WB     \n'
            'WB     \n',
        )

    def test_win_horizontal(self):
        self.game.play(0)
        self.game.play(0)
        self.game.play(1)
        self.game.play(1)
        self.game.play(2)
        self.game.play(2)
        self.assertEqual('You win', self.game.play(3))
        self.assertEqual(
            self.game.board,
            '       \n'
            '       \n'
            '       \n'
            '       \n'
            'BBB    \n'
            'WWWW   \n',
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

        self.assertEqual('You win', self.game.play(3))

        self.assertEqual(
            self.game.board,
            '       \n'
            '       \n'
            '   W   \n'
            '  WW   \n'
            'BWWB   \n'
            'WBBB   \n',
        )

    def test_tie(self):

        self.game.board_status = [
            ['W', 'W', 'B', 'W', 'B', 'B', 'B'],
            ['B', 'B', 'W', 'B', 'B', 'W', 'W'],
            ['W', 'W', 'B', 'B', 'W', 'B', 'W'],
            ['B', 'W', 'W', 'W', 'B', 'W', 'B'],
            ['W', 'B', 'B', 'W', 'W', 'W', 'B'],
            ['W', 'B', 'W', 'B', 'B', 'B', 'W'],
        ]

        self.assertEqual('Tie', self.game.play(0))
        self.assertEqual(True, self.game.tie())
        self.assertEqual(False, self.game.is_playing)

    def test_wrong_set_1(self):
        self.assertEqual('Movement not allowed', self.game.play(-1))
        self.assertEqual(
            self.game.board,
            '       \n'
            '       \n'
            '       \n'
            '       \n'
            '       \n'
            '       \n'
        )
        self.assertEqual(True, self.game.is_playing)

    def test_wrong_set_2(self):
        self.assertEqual('Movement not allowed', self.game.play(9))
        self.assertEqual(
            self.game.board,
            '       \n'
            '       \n'
            '       \n'
            '       \n'
            '       \n'
            '       \n'
        )
        self.assertEqual(True, self.game.is_playing)

    def test_wrong_set_3(self):
        self.assertEqual('Movement not allowed', self.game.play('a'))
        self.assertEqual(
            self.game.board,
            '       \n'
            '       \n'
            '       \n'
            '       \n'
            '       \n'
            '       \n'
        )
        self.assertEqual(True, self.game.is_playing)


if __name__ == "__main__":
    unittest.main()
