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

    def test_initial_board_status(self):
        result = [
                 ['E', 'E', 'E', 'E'],
                 ['E', 'E', 'E', 'E'],
                 ['E', 'E', 'E', 'E'],
                 ['E', 'E', 'E', 'E'],
        ]
        self.assertEqual(result, self.game.board_status)

    def test_first_move_first_column(self):
        result = [
            ['E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E'],
            ['W', 'E', 'E', 'E'],
        ]
        self.assertEqual(result, self.game.play(0))
        self.assertTrue(self.game.playing)

    def test_second_move_first_column(self):
        self.game.play(0)
        result = [
                 ['E', 'E', 'E', 'E'],
                 ['E', 'E', 'E', 'E'],
                 ['B', 'E', 'E', 'E'],
                 ['W', 'E', 'E', 'E']
        ]
        self.assertTrue(self.game.playing)
        self.assertEqual(result, self.game.play(0))

    def test_full_column(self):
        self.game.play(0)
        self.game.play(0)
        self.game.play(0)
        self.game.play(0)
        self.assertTrue(self.game.playing)
        self.assertEqual('Full column', self.game.play(0))


if __name__ == "__main__":
    unittest.main()
