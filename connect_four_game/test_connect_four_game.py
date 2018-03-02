import unittest
from connect_four_game import ConnectFourGame


class TestConnectFourGame(unittest.TestCase):

    def setUp(self):
        self.game = ConnectFourGame()

    def test_initial_game_status(self):
        self.assertTrue(self.game.playing)

    def test_turno(self):
        turn_white = self.game.playingW(1)
        self.assertEqual(turn_white, 'White plays')

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
        self.assertTrue(self.game.playing)
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
        self.assertTrue(self.game.playing)
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
        self.assertTrue(self.game.playing)
        self.assertEqual('Full column', self.game.play(0))

    def test_win_vertical(self):
        self.game.play(0)
        self.game.play(1)
        self.game.play(0)
        self.game.play(1)
        self.game.play(0)
        self.game.play(1)
        self.assertEquals('You win', self.game.play(0))
        self.game.play(0)
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
        self.game.play(3)
        self.game.play(3)
        self.assertEquals('You win', self.game.play(4))
        self.assertEqual(
            self.game.board,
            'EEEEEEE\n'
            'EEEEEEE\n'
            'EEEEEEE\n'
            'EEEEEEE\n'
            'BBBBEEE\n'
            'WWWWBEE\n',
        )

    def test_win_diagonalD(self):
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
        self.game.play(3)
#        self.assertEquals('You win', self.game.play(3))
        self.assertEqual(
            self.game.board,
            'EEEEEEE\n'
            'EEEEEEE\n'
            'EEEWEEE\n'
            'EEWWEEE\n'
            'BWWBEEE\n'
            'WBBBEEE\n',
        )


if __name__ == "__main__":
    unittest.main()
