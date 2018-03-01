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

    def test_firts_move(self):
        self.game.play(5, 1, 4, 0)
        self.assertEqual(
            self.game.board,
            'b b b b \n'
            ' b b b b\n'
            'b b b b \n'
            '        \n'
            'w       \n'
            '   w w w\n'
            'w w w w \n'
            ' w w w w\n',
        )
        self.assertEqual('Black', self.game.turn)

    def test_second_move(self):
        self.game.play(5, 1, 4, 0)
        self.game.play(2, 0, 3, 1)
        self.assertEqual(
            self.game.board,
            'b b b b \n'
            ' b b b b\n'
            '  b b b \n'
            ' b      \n'
            'w       \n'
            '   w w w\n'
            'w w w w \n'
            ' w w w w\n',
        )
        self.assertEqual('White', self.game.turn)

    def test_third_move(self):
        self.game.play(5, 1, 4, 0)
        self.game.play(2, 0, 3, 1)
        self.assertEqual(
            self.game.board,
            'b b b b \n'
            ' b b b b\n'
            '  b b b \n'
            ' b      \n'
            'w       \n'
            '   w w w\n'
            'w w w w \n'
            ' w w w w\n',
        )
        self.game.play(5, 3, 4, 2)
        self.assertEqual(
            self.game.board,
            'b b b b \n'
            ' b b b b\n'
            '  b b b \n'
            ' b      \n'
            'w w     \n'
            '     w w\n'
            'w w w w \n'
            ' w w w w\n'
        )
        self.assertEqual('Black', self.game.turn)

    def test_check_initial_position_inside_board(self):
        self.assertEqual(self.game.play(-1, -1, 6, 6),
                         "This position is outside our board")

    def test_check_final_position_inside_board(self):
        self.assertEqual(self.game.play(1, 1, 9, 8),
                         "This position is outside our board")

    def test_wrong_choise(self):
        self.assertEqual(
            self.game.play(4, 4, 3, 5), 'No white piece here to move !')
        self.assertEqual('White', self.game.turn)

    # def test_action_move(self):
    #     self.game.play(5, 1, 4, 0)
    #     self.game.play(2, 0, 3, 1)
    #     self.game.play(5, 3, 4, 2)
    #     self.game.play(3, 1, 5, 3)
    #     self.assertEqual(
    #         self.game.board,
    #         'b b b b \n'
    #         ' b b b b\n'
    #         '  b b b \n'
    #         '        \n'
    #         'w       \n'
    #         '   b w w\n'
    #         'w w w w \n'
    #         ' w w w w\n'
    #     )
    #     self.assertEqual('White', self.game.turn)


if __name__ == '__main__':
    unittest.main()
