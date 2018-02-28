import unittest
from dama_game import DamaGameStart


class TestDamaGame(unittest.TestCase):

    def setUp(self):
        self.game = DamaGameStart()

    def test_initial_status(self):
        self.assertTrue(self.game.playing)

    def test_initial_turn(self):
        self.assertEqual('White', self.game.turn)

    def test_initial_board(self):
        self.assertEqual(
            self.game.board,
            'b b b b \n'
            ' b b b b\n'
            'b b b b \n'
            '        \n'
            '        \n'
            ' w w w w\n'
            'w w w w \n'
            ' w w w w\n'
        )

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

    def test_firts_move(self):
        result = [
            ['b', ' ', 'b', ' ', 'b', ' ', 'b', ' '],
            [' ', 'b', ' ', 'b', ' ', 'b', ' ', 'b'],
            ['b', ' ', 'b', ' ', 'b', ' ', 'b', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['w', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', 'w', ' ', 'w', ' ', 'w'],
            ['w', ' ', 'w', ' ', 'w', ' ', 'w', ' '],
            [' ', 'w', ' ', 'w', ' ', 'w', ' ', 'w']
        ]
        self.game.play(5, 1, 4, 0)
        self.assertEqual(result, self.game.board_status)
        self.assertEqual('Black', self.game.turn)

    def test_second_move(self):
        self.game.play(5, 1, 4, 0)
        result = [
            ['b', ' ', 'b', ' ', 'b', ' ', 'b', ' '],
            [' ', 'b', ' ', 'b', ' ', 'b', ' ', 'b'],
            [' ', ' ', 'b', ' ', 'b', ' ', 'b', ' '],
            [' ', 'b', ' ', ' ', ' ', ' ', ' ', ' '],
            ['w', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', 'w', ' ', 'w', ' ', 'w'],
            ['w', ' ', 'w', ' ', 'w', ' ', 'w', ' '],
            [' ', 'w', ' ', 'w', ' ', 'w', ' ', 'w']
        ]
        self.game.play(2, 0, 3, 1)
        self.assertEqual(result, self.game.board_status)
        self.assertEqual('White', self.game.turn)

    def test_third_move(self):
        self.game.play(5, 1, 4, 0)
        self.game.play(2, 0, 3, 1)
        result = [
            ['b', ' ', 'b', ' ', 'b', ' ', 'b', ' '],
            [' ', 'b', ' ', 'b', ' ', 'b', ' ', 'b'],
            [' ', ' ', 'b', ' ', 'b', ' ', 'b', ' '],
            [' ', 'b', ' ', ' ', ' ', ' ', ' ', ' '],
            ['w', ' ', 'w', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', 'w', ' ', 'w'],
            ['w', ' ', 'w', ' ', 'w', ' ', 'w', ' '],
            [' ', 'w', ' ', 'w', ' ', 'w', ' ', 'w']
        ]
        self.game.play(5, 3, 4, 2)
        self.assertEqual(result, self.game.board_status)
        self.assertEqual('Black', self.game.turn)


if __name__ == '__main__':
    unittest.main()
