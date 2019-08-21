import unittest
from .dama_game import DamaGameStart


class TestDamaGame(unittest.TestCase):

    def setUp(self):
        self.game = DamaGameStart()

    def test_initial_status(self):
        self.assertTrue(self.game._playing)

    def test_initial_turn(self):
        self.assertEqual('White', self.game.player_one)

    def test_initial_board(self):
        self.assertEqual(
            self.game.board,
            ' 01234567\n'
            '0b b b b \n'
            '1 b b b b\n'
            '2b b b b \n'
            '3        \n'
            '4        \n'
            '5 w w w w\n'
            '6w w w w \n'
            '7 w w w w\n'
        )

    def test_initial__board(self):
        self.assertEqual(
            self.game.board,
            ' 01234567\n'
            '0b b b b \n'
            '1 b b b b\n'
            '2b b b b \n'
            '3        \n'
            '4        \n'
            '5 w w w w\n'
            '6w w w w \n'
            '7 w w w w\n'
        )

    def test_firts_move(self):
        self.game.play(5, 1, 4, 0)
        self.assertEqual(
            self.game.board,
            ' 01234567\n'
            '0b b b b \n'
            '1 b b b b\n'
            '2b b b b \n'
            '3        \n'
            '4w       \n'
            '5   w w w\n'
            '6w w w w \n'
            '7 w w w w\n',
        )
        self.assertEqual(self.game.player_two, self.game._turn)

    def test_second_move(self):
        self.game.play(5, 1, 4, 0)
        self.game.play(2, 0, 3, 1)
        self.assertEqual(
            self.game.board,
            ' 01234567\n'
            '0b b b b \n'
            '1 b b b b\n'
            '2  b b b \n'
            '3 b      \n'
            '4w       \n'
            '5   w w w\n'
            '6w w w w \n'
            '7 w w w w\n',
        )
        self.assertEqual(self.game.player_one, self.game._turn)

    def test_third_move(self):
        self.game.play(5, 1, 4, 0)
        self.game.play(2, 0, 3, 1)
        self.assertEqual(
            self.game.board,
            ' 01234567\n'
            '0b b b b \n'
            '1 b b b b\n'
            '2  b b b \n'
            '3 b      \n'
            '4w       \n'
            '5   w w w\n'
            '6w w w w \n'
            '7 w w w w\n',
        )
        self.game.play(5, 3, 4, 2)
        self.assertEqual(
            self.game.board,
            ' 01234567\n'
            '0b b b b \n'
            '1 b b b b\n'
            '2  b b b \n'
            '3 b      \n'
            '4w w     \n'
            '5     w w\n'
            '6w w w w \n'
            '7 w w w w\n'
        )
        self.assertEqual(self.game.player_two, self.game._turn)

    def test_check_initial_position_inside_board(self):
        self.assertEqual(self.game.play(-1, -1, 6, 6),
                         "This position is outside our board")

    def test_check_final_position_inside_board(self):
        self.assertEqual(self.game.play(1, 1, 9, 8),
                         "This position is outside our board")

    def test_wrong_choise(self):
        self.assertEqual(
            self.game.play(4, 4, 3, 5), 'No white piece here to move !')
        self.assertEqual(self.game.player_one, self.game._turn)

    def test_unreachable_place(self):
        self.assertEqual(
            self.game.play(7, 7, 5, 5), 'you cant reach that place!')
        self.assertEqual(self.game.player_one, self.game._turn)

    def test_is_dama_white(self):
        self.game._board = [
            ['b', ' ', ' ', ' ', 'b', ' ', 'b', ' '],
            [' ', 'w', ' ', 'b', ' ', 'b', ' ', 'b'],
            ['b', ' ', 'b', ' ', 'b', ' ', 'b', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', 'w', ' ', 'w', ' ', 'w', ' ', 'w'],
            ['w', ' ', 'w', ' ', 'w', ' ', 'w', ' '],
            [' ', 'w', ' ', 'w', ' ', 'w', ' ', 'w']]
        self.assertEqual(
            self.game.play(1, 1, 0, 2), 'you became a dama!')
        self.assertEqual(
            self.game._board[0][2], 'W')

    def test_is_dama_black(self):
        self.game._turn = self.game.player_two
        self.game._board = [
            ['b', ' ', ' ', ' ', 'b', ' ', 'b', ' '],
            [' ', 'w', ' ', 'b', ' ', 'b', ' ', 'b'],
            ['b', ' ', 'b', ' ', 'b', ' ', 'b', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', 'w', ' ', 'w', ' ', 'w', ' ', 'w'],
            ['w', ' ', 'b', ' ', 'w', ' ', 'w', ' '],
            [' ', 'w', ' ', ' ', ' ', 'w', ' ', 'w']]
        self.assertEqual(
            self.game.play(6, 2, 7, 3), 'you became a dama!')
        self.assertEqual(self.game._board[7][3], 'B')

    def test_eat_move_white(self):
        self.game._board = [
            ['b', ' ', ' ', ' ', 'b', ' ', 'b', ' '],
            [' ', 'w', ' ', 'b', ' ', 'b', ' ', 'b'],
            ['b', ' ', ' ', ' ', 'b', ' ', 'b', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'b', ' ', ' ', ' ', ' ', ' '],
            [' ', 'w', ' ', 'w', ' ', 'w', ' ', 'w'],
            ['w', ' ', 'b', ' ', 'w', ' ', 'w', ' '],
            [' ', 'w', ' ', ' ', ' ', 'w', ' ', 'w']]
        self.assertEqual(self.game.play(5, 1, 3, 3), None)
        self.assertEqual(self.game._board[4][2], ' ')

    def test_eat_move_black(self):
        self.game._turn = self.game.player_two
        self.game._board = [
            ['b', ' ', ' ', ' ', 'b', ' ', 'b', ' '],
            [' ', 'w', ' ', 'b', ' ', 'b', ' ', 'b'],
            ['b', ' ', ' ', ' ', 'w', ' ', 'b', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'b', ' ', ' ', ' ', ' ', ' '],
            [' ', 'w', ' ', 'w', ' ', 'w', ' ', 'w'],
            ['w', ' ', 'b', ' ', 'w', ' ', 'w', ' '],
            [' ', 'w', ' ', ' ', ' ', 'w', ' ', 'w']]
        self.assertEqual(self.game.play(1, 3, 3, 5), None)
        self.assertEqual(self.game._board[2][4], ' ')

    def test_win_white(self):
        self.game._board = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', 'w', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'b', ' ', ' ', ' ', ' ', ' '],
            [' ', 'w', ' ', ' ', ' ', 'w', ' ', 'w'],
            [' ', ' ', ' ', ' ', ' ', ' ', 'w', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'w']]
        self.assertEqual(self.game.play(5, 1, 3, 3), None)
        self.assertFalse(self.game._playing)

    def test_win_black(self):
        self.game._turn = self.game.player_two
        self.game._board = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'b', ' ', ' ', ' ', ' ', ' '],
            [' ', 'w', ' ', ' ', ' ', 'b', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', 'b', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
        self.assertEqual(self.game.play(4, 2, 6, 0), None)
        self.assertFalse(self.game._playing)

    def test_out_of_index(self):
        self.game.play(5, 1, 4, 2)
        self.game.play(2, 2, 3, 3)
        self.game.play(5, 3, 4, 4)
        self.game.play(3, 3, 5, 0)
        self.game.play(4, 4, 3, 3)
        self.game.play(2, 4, 4, 2)
        self.game.play(5, 5, 4, 4)
        self.game.play(4, 2, 5, 3)
        self.game.play(6, 4, 4, 2)
        self.game.play(2, 6, 3, 5)
        self.game.play(4, 4, 2, 7)
        self.game.play(1, 1, 2, 2)
        self.game.play(4, 2, 3, 3)
        self.game.play(2, 2, 4, 4)
        self.game.play(6, 2, 5, 3)
        self.game.play(4, 4, 6, 1)
        self.game.play(5, 7, 4, 6)
        self.game.play(2, 0, 3, 1)
        self.game.play(4, 6, 3, 5)
        self.game.play(3, 1, 4, 2)
        self.game.play(3, 5, 2, 4)
        self.game.play(4, 2, 5, 3)
        self.game.play(6, 0, 5, 1)
        self.game.play(5, 3, 6, 4)
        self.game.play(7, 5, 5, 2)
        self.game.play(6, 1, 7, 2)
        self.game.play(7, 1, 6, 2)
        self.game.play(1, 3, 3, 5)
        self.game.play(6, 6, 5, 5)
        self.game.play(1, 5, 2, 4)
        self.game.play(2, 7, 1, 6)
        self.game.play(5, 0, 6, 1)
        self.game.play(5, 5, 4, 4)
        self.game.play(2, 4, 3, 3)
        self.game.play(7, 7, 6, 6)
        self.game.play(3, 3, 5, 6)
        self.game.play(6, 6, 5, 5)
        self.game.play(5, 6, 6, 5)
        self.game.play(6, 2, 5, 3)
        self.game.play(6, 5, 7, 4)
        self.game.play(5, 5, 4, 4)
        self.game.play(0, 0, 1, 1)
        self.game.play(5, 3, 4, 2)
        self.game.play(3, 5, 5, 3)
        self.game.play(4, 2, 3, 3)
        self.game.play(1, 1, 2, 2)
        self.game.play(5, 1, 4, 2)
        self.game.play(2, 2, 4, 4)
        self.game.play(4, 2, 3, 3)
        self.game.play(4, 4, 5, 5)
        self.game.play(3, 3, 2, 4)
        self.assertEqual(self.game.play(7, 2, 6, 3), None)


if __name__ == '__main__':
    unittest.main()
