import unittest
from .ReversiGame import ReversiGame


class TestReversi(unittest.TestCase):

    def setUp(self):
        self.game = ReversiGame()

    def test_initial_status(self):
        self.assertTrue(self.game.is_playing)
        self.assertEqual(self.game.get_value(3, 3), 'B')
        self.assertEqual(self.game.get_value(3, 4), 'W')
        self.assertEqual(self.game.get_value(4, 4), 'B')
        self.assertEqual(self.game.get_value(4, 3), 'W')

    def test_initial_next_turn_whites(self):
        self.assertEqual(
            self.game.next_turn(),
            'White',
        )

    def test_wrong_movement_empty(self):
        self.assertEqual(self.game.play(1, 1), 'No possibilities. Try again.')

    def test_no_posibilities(self):
        self.assertEqual(self.game.play(7, 7), 'No possibilities. Try again.')

    def test_wrong_movement_occupied(self):
        self.assertEqual(self.game.play(3, 4),
                          'Movement not allowed. Try again.')

    def test_get_directions(self):
        result = [
            {'value': 'W', 'x': 3, 'y': 4},
        ]
        self.game.change_turn()
        self.assertEqual(result, self.game.find_possibility_pieces(3, 5))

    def test_get_directions_black(self):
        self.game.set_board([
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', 'B', 'B', 'B', ' ', ' '],
            [' ', ' ', ' ', 'W', 'B', 'W', ' ', ' '],
            [' ', ' ', ' ', ' ', 'B', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ])

        result = [
            {'value': 'B', 'x': 3, 'y': 4},
            {'value': 'B', 'x': 3, 'y': 5},
        ]
        self.assertEqual(result, self.game.find_possibility_pieces(2, 5))
        result = [
            {'value': 'B', 'x': 3, 'y': 3},
            {'value': 'B', 'x': 3, 'y': 4},
        ]
        self.assertEqual(result, self.game.find_possibility_pieces(2, 3))

    def test_find_possibilities_limits_min(self):
        self.assertEqual([], self.game.find_possibility_pieces(0, 0))

    def test_find_possibilities_limits_max(self):
        self.assertEqual([], self.game.find_possibility_pieces(7, 7))

    def test_get_all_directions_white(self):
        self.game.set_board([
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'W', 'W', 'W', 'W', 'W', ' '],
            [' ', ' ', 'W', 'B', 'B', 'B', 'W', ' '],
            [' ', ' ', 'W', 'B', ' ', 'B', 'W', ' '],
            [' ', ' ', 'W', 'B', 'B', 'B', 'W', ' '],
            [' ', ' ', 'W', 'W', 'W', 'W', 'W', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ])

        result = [
            {'y': 3, 'x': 2, 'value': 'B'},
            {'y': 4, 'x': 2, 'value': 'B'},
            {'y': 5, 'x': 2, 'value': 'B'},
            {'y': 3, 'x': 3, 'value': 'B'},
            {'y': 5, 'x': 3, 'value': 'B'},
            {'y': 3, 'x': 4, 'value': 'B'},
            {'y': 4, 'x': 4, 'value': 'B'},
            {'y': 5, 'x': 4, 'value': 'B'}
        ]
        self.assertEqual(result, self.game.find_possibility_pieces(3, 4))

    def test_get_all_none_directions_white(self):
        self.game.set_board([
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'B', 'B', 'B', 'B', 'B', ' '],
            [' ', ' ', 'B', 'B', 'B', 'B', 'B', ' '],
            [' ', ' ', 'B', 'B', ' ', 'B', 'B', ' '],
            [' ', ' ', 'B', 'B', 'B', 'B', 'B', ' '],
            [' ', ' ', 'B', 'B', 'B', 'B', 'B', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ])

        result = [
        ]
        self.assertEqual(result, self.game.find_possibility_pieces(3, 4))

    def test_get_all_x2_directions_white(self):
        self.game.set_board([
            [' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            [' ', ' ', 'B', 'B', 'B', 'B', 'B', ' '],
            [' ', ' ', 'W', 'B', 'B', 'B', 'W', ' '],
            [' ', 'W', 'B', 'B', ' ', 'B', 'B', 'W'],
            [' ', ' ', 'W', 'B', 'B', 'B', 'W', ' '],
            [' ', ' ', 'B', 'W', 'B', 'W', 'B', ' '],
            [' ', 'W', ' ', ' ', 'W', ' ', ' ', 'W'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ])

        result = [
            {'y': 3, 'x': 2, 'value': 'B'},
            {'y': 2, 'x': 1, 'value': 'B'},
            {'y': 4, 'x': 2, 'value': 'B'},
            {'y': 4, 'x': 1, 'value': 'B'},
            {'y': 5, 'x': 2, 'value': 'B'},
            {'y': 6, 'x': 1, 'value': 'B'},
            {'y': 3, 'x': 3, 'value': 'B'},
            {'y': 2, 'x': 3, 'value': 'B'},
            {'y': 5, 'x': 3, 'value': 'B'},
            {'y': 6, 'x': 3, 'value': 'B'},
            {'y': 3, 'x': 4, 'value': 'B'},
            {'y': 2, 'x': 5, 'value': 'B'},
            {'y': 4, 'x': 4, 'value': 'B'},
            {'y': 4, 'x': 5, 'value': 'B'},
            {'y': 5, 'x': 4, 'value': 'B'},
            {'y': 6, 'x': 5, 'value': 'B'},
        ]
        self.assertEqual(result, self.game.find_possibility_pieces(3, 4))

    def test_get_all_directions_black(self):
        self.game.set_board([
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'B', 'B', 'B', 'B', 'B', ' '],
            [' ', ' ', 'B', 'W', 'W', 'W', 'B', ' '],
            [' ', ' ', 'B', 'W', ' ', 'W', 'B', ' '],
            [' ', ' ', 'B', 'W', 'W', 'W', 'B', ' '],
            [' ', ' ', 'B', 'B', 'B', 'B', 'B', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ])
        self.game.change_turn()
        result = [
            {'y': 3, 'x': 2, 'value': 'W'},
            {'y': 4, 'x': 2, 'value': 'W'},
            {'y': 5, 'x': 2, 'value': 'W'},
            {'y': 3, 'x': 3, 'value': 'W'},
            {'y': 5, 'x': 3, 'value': 'W'},
            {'y': 3, 'x': 4, 'value': 'W'},
            {'y': 4, 'x': 4, 'value': 'W'},
            {'y': 5, 'x': 4, 'value': 'W'},
        ]
        self.assertEqual(result, self.game.find_possibility_pieces(3, 4))

    def test_no_possibles(self):
        self.game.set_board([
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'B', 'B', 'B', 'B', ' ', ' '],
            [' ', ' ', 'B', 'W', 'W', 'W', ' ', ' '],
            [' ', ' ', 'B', 'W', ' ', 'W', ' ', ' '],
            [' ', ' ', 'B', 'W', 'W', ' ', ' ', ' '],
            [' ', ' ', 'B', 'B', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ])
        self.assertEqual(self.game.play(6, 6), 'No possibilities. Try again.')

    def test_reverse_possibles(self):
        self.game.set_board([
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'B', 'B', 'B', 'B', 'B', ' '],
            [' ', ' ', 'B', 'W', 'W', 'W', 'B', ' '],
            [' ', ' ', 'B', 'W', ' ', 'W', 'B', ' '],
            [' ', ' ', 'B', 'W', 'W', 'W', 'B', ' '],
            [' ', ' ', 'B', 'B', 'B', 'B', 'B', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ])
        self.game.change_turn()
        possibles = self.game.find_possibility_pieces(3, 4)

        self.game.reverse_possibles(possibles)
        result = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'B', 'B', 'B', 'B', 'B', ' '],
            [' ', ' ', 'B', 'B', 'B', 'B', 'B', ' '],
            [' ', ' ', 'B', 'B', ' ', 'B', 'B', ' '],
            [' ', ' ', 'B', 'B', 'B', 'B', 'B', ' '],
            [' ', ' ', 'B', 'B', 'B', 'B', 'B', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ]
        self.assertEqual(result, self.game.get_board)

    def test_play_valid(self):
        self.game.set_board([
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'B', 'B', 'B', 'B', 'B', ' '],
            [' ', ' ', 'B', 'W', 'W', 'W', 'B', ' '],
            [' ', ' ', 'B', 'W', ' ', 'W', 'B', ' '],
            [' ', ' ', 'B', 'W', 'W', 'W', 'B', ' '],
            [' ', ' ', 'B', 'B', 'B', 'B', 'B', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ])
        self.game.change_turn()
        self.game.play(3, 4)
        result = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'B', 'B', 'B', 'B', 'B', ' '],
            [' ', ' ', 'B', 'B', 'B', 'B', 'B', ' '],
            [' ', ' ', 'B', 'B', 'B', 'B', 'B', ' '],
            [' ', ' ', 'B', 'B', 'B', 'B', 'B', ' '],
            [' ', ' ', 'B', 'B', 'B', 'B', 'B', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ]
        self.assertEqual(result, self.game.get_board)
        self.assertEqual(
            self.game.next_turn(),
            'White',
        )

    def test_play_invalid_moves(self):
        self.game.set_board([
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'B', 'B', 'B', 'B', 'B', ' '],
            [' ', ' ', 'B', 'W', 'W', 'W', 'B', ' '],
            [' ', ' ', 'B', 'W', ' ', 'W', 'B', ' '],
            [' ', ' ', 'B', 'W', 'W', 'W', 'B', ' '],
            [' ', ' ', 'B', 'B', 'B', 'B', 'B', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ])
        self.assertEqual(self.game.validate(9, 10), 'Values must be between 0 and 7')

    def test_graphic_board(self):
        self.game.set_board([
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'B', 'B', 'B', 'B', 'B', ' '],
            [' ', ' ', 'B', 'W', 'W', 'W', 'B', ' '],
            [' ', ' ', 'B', 'W', ' ', 'W', 'B', ' '],
            [' ', ' ', 'B', 'W', 'W', 'W', 'B', ' '],
            [' ', ' ', 'B', 'B', 'B', 'B', 'B', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ])
        result = (
            '  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |\n'
            '--+---+---+---+---+---+---+---+---+\n'
            '0 |   |   |   |   |   |   |   |   |\n'
            '--+---+---+---+---+---+---+---+---+\n'
            '1 |   |   | B | B | B | B | B |   |\n'
            '--+---+---+---+---+---+---+---+---+\n'
            '2 |   |   | B | W | W | W | B |   |\n'
            '--+---+---+---+---+---+---+---+---+\n'
            '3 |   |   | B | W |   | W | B |   |\n'
            '--+---+---+---+---+---+---+---+---+\n'
            '4 |   |   | B | W | W | W | B |   |\n'
            '--+---+---+---+---+---+---+---+---+\n'
            '5 |   |   | B | B | B | B | B |   |\n'
            '--+---+---+---+---+---+---+---+---+\n'
            '6 |   |   |   |   |   |   |   |   |\n'
            '--+---+---+---+---+---+---+---+---+\n'
            '7 |   |   |   |   |   |   |   |   |\n'
            '--+---+---+---+---+---+---+---+---+\n'
        )

        self.assertEqual(result, self.game.board)

    def test_play_finish_white_wins(self):
        self.game.set_board([
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'B', 'B', 'B', 'B', 'B', 'W'],
            ['W', 'W', 'B', 'W', 'W', 'W', 'B', 'W'],
            ['W', 'W', 'B', 'W', 'W', 'W', 'B', 'W'],
            ['W', 'W', 'B', 'W', 'W', 'W', 'B', 'W'],
            ['W', ' ', 'W', 'B', 'B', 'B', 'B', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
        ])

        self.game.change_turn()
        self.assertEqual(
            self.game.play(5, 1),
            'Whites win 47 to 17',
        )

        result = [
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'B', 'B', 'B', 'B', 'B', 'W'],
            ['W', 'W', 'B', 'W', 'W', 'W', 'B', 'W'],
            ['W', 'W', 'B', 'W', 'W', 'W', 'B', 'W'],
            ['W', 'W', 'B', 'W', 'W', 'W', 'B', 'W'],
            ['W', 'B', 'B', 'B', 'B', 'B', 'B', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
        ]

        self.assertEqual(result, self.game.get_board)
    
    def test_play_finish_tie(self):
        self.game.set_board([
            ['W', 'W', 'W', 'B', 'B', 'B', 'B', 'B'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'B'],
            ['W', 'W', 'W', 'B', 'B', 'W', 'W', 'B'],
            ['B', 'W', 'W', 'B', 'B', 'B', 'W', 'W'],
            ['B', 'W', 'W', 'B', 'B', 'B', 'W', 'B'],
            ['B', ' ', 'B', 'W', 'W', 'W', 'W', 'B'],
            ['B', 'W', 'B', 'B', 'W', 'B', 'B', 'B'],
            ['B', 'W', 'B', 'B', 'B', 'W', 'B', 'B'],
        ])
        self.assertEqual(
            self.game.play(5, 1),
            "It's a tie! --- Whites: 32; Blacks: 32",
        )

        result = [
            ['W', 'W', 'W', 'B', 'B', 'B', 'B', 'B'],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'B'],
            ['W', 'W', 'W', 'B', 'B', 'W', 'W', 'B'],
            ['B', 'W', 'W', 'B', 'B', 'B', 'W', 'W'],
            ['B', 'W', 'W', 'B', 'B', 'B', 'W', 'B'],
            ['B', 'W', 'W', 'W', 'W', 'W', 'W', 'B'],
            ['B', 'W', 'B', 'B', 'W', 'B', 'B', 'B'],
            ['B', 'W', 'B', 'B', 'B', 'W', 'B', 'B'],
        ]
        self.assertEqual(result, self.game.get_board)
    
    def test_play_finish_black_wins(self):
        self.game.set_board([
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'W', 'W', 'W', 'W', 'W', 'B'],
            ['B', 'B', 'W', 'B', 'B', 'B', 'W', 'B'],
            ['B', 'B', 'W', 'B', 'B', 'B', 'W', 'B'],
            ['B', 'B', 'W', 'B', 'B', 'B', 'W', 'B'],
            ['B', ' ', 'B', 'W', 'W', 'W', 'W', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
        ])
        self.assertEqual(
            self.game.play(5, 1),
            'Blacks win 47 to 17',
        )

        result = [
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'W', 'W', 'W', 'W', 'W', 'B'],
            ['B', 'B', 'W', 'B', 'B', 'B', 'W', 'B'],
            ['B', 'B', 'W', 'B', 'B', 'B', 'W', 'B'],
            ['B', 'B', 'W', 'B', 'B', 'B', 'W', 'B'],
            ['B', 'W', 'W', 'W', 'W', 'W', 'W', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
            ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
        ]

        self.assertEqual(result, self.game.get_board)


    def test_change_turn_if_no_possibility(self):
        self.game.set_board([
            [' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            [' ', 'W', 'B', 'B', 'B', 'B', 'B', 'W'],
            [' ', 'W', 'B', 'W', 'W', 'W', 'B', 'W'],
            [' ', 'W', 'B', 'W', 'W', 'W', 'B', 'W'],
            [' ', 'W', 'B', 'W', 'W', 'W', 'B', 'W'],
            [' ', 'W', 'W', 'B', 'B', 'B', 'B', 'W'],
            [' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            [' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
        ])
        self.assertEqual(self.game.play(0, 0),
                          'No possible moves, turn changes')

        self.assertEqual(self.game.next_turn(), 'Black')

    def test_no_one_can_play(self):
        self.game.set_board([
            [' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            [' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            [' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            [' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            [' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            [' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            [' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
            [' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
        ])
        self.assertEqual(self.game.play(0, 0),
                          'Game over!')
    
    def test_has_piece_to_change(self):
        self.game.set_board([
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'B', 'B', 'B', 'B', 'B', ' '],
            [' ', ' ', 'B', 'W', 'W', 'W', 'B', ' '],
            [' ', ' ', 'B', 'W', ' ', 'W', 'B', ' '],
            [' ', ' ', 'B', 'W', 'W', 'W', 'B', ' '],
            [' ', ' ', 'B', 'B', 'B', 'B', 'B', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ])
        self.assertEqual(self.game.has_piece_to_change(4, 2, 'B'), True)



if __name__ == "__main__":
    unittest.main()
