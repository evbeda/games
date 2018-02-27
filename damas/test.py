import unittest
from dama_game import DamaGameStart


class TestDamaGame(unittest.TestCase):

    def setUp(self):
        self.game = DamaGameStart()

    def test_initial_status(self):
        self.assertTrue(self.game.playing)

    def test_initial_board_status(self):
        result = [
            ['b', ' ', 'b', ' ', 'b', ' ', 'b', ' '],
            [' ', 'b', ' ', 'b', ' ', 'b', ' ', 'b'],
            ['b', ' ', 'b', ' ', 'b', ' ', 'b', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', 'w', ' ', 'w', ' ', 'w', ' ', 'w'],
            ['w', ' ', 'w', ' ', 'w', ' ', 'w', ' '],
            [' ', 'w', ' ', 'w', ' ', 'w', ' ', 'w']
        ]
        self.assertEqual(result, self.game.board_status)


if __name__ == '__main__':
    unittest.main()
