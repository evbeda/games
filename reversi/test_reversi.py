import unittest
from ReversiGame import ReversiGame


class TestReversi(unittest.TestCase):

    def setUp(self):
        self.game = ReversiGame()

    def test_initial_status(self):
        self.assertTrue(self.game.is_playing)
        self.assertEquals(self.game.get_value(3, 3), 'B')
        self.assertEquals(self.game.get_value(3, 4), 'W')
        self.assertEquals(self.game.get_value(4, 4), 'B')
        self.assertEquals(self.game.get_value(4, 3), 'W')

    def test_initial_next_turn_whites(self):
        self.assertEquals(
            self.game.next_turn(),
            'White',
        )

    def test_wrong_movement_empty(self):
        self.assertEquals(self.game.play(1, 1), 'No possibilities. Try again.')

    def test_no_posibilities(self):
        self.assertEquals(self.game.play(7, 7), 'No possibilities. Try again.')

    def test_wrong_movement_occupied(self):
        self.assertEquals(self.game.play(3, 4),
                          'Movement not allowed. Try again.')

    def test_get_directions(self):
        result = [
            [(3, 4, 'W')]
        ]
        self.game.change_turn()
        self.assertEquals(result, self.game.find_possibility_pieces(3, 5))

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
            [(3, 5, 'B')], [(3, 4, 'B')]
        ]
        self.assertEquals(result, self.game.find_possibility_pieces(2, 5))
        result = [
            [(3, 3, 'B')], [(3, 4, 'B')]
        ]
        self.assertEquals(result, self.game.find_possibility_pieces(2, 3))

    def test_find_possibilities_limits_min(self):
        self.assertEquals([], self.game.find_possibility_pieces(0, 0))

    def test_find_possibilities_limits_max(self):
        self.assertEquals([], self.game.find_possibility_pieces(7, 7))

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
            [(3, 3, 'B')], [(3, 5, 'B')],
            [(2, 4, 'B')], [(4, 4, 'B')],
            [(2, 5, 'B')], [(2, 3, 'B')],
            [(4, 3, 'B')], [(4, 5, 'B')]
        ]
        self.assertEquals(result, self.game.find_possibility_pieces(3, 4))

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
            [(3, 3, 'W')], [(3, 5, 'W')],
            [(2, 4, 'W')], [(4, 4, 'W')],
            [(2, 5, 'W')], [(2, 3, 'W')],
            [(4, 3, 'W')], [(4, 5, 'W')]
        ]
        self.assertEquals(result, self.game.find_possibility_pieces(3, 4))

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
        self.assertEquals(result, self.game.get_board)

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
        self.assertEquals(result, self.game.get_board)
        self.assertEquals(
            self.game.next_turn(),
            'White',
        )

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

        self.assertEquals(result, self.game.board)

    def test_play_finish(self):
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

        self.assertEquals(
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

        self.assertEquals(result, self.game.get_board)

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
        self.assertEquals(self.game.play(0, 0),
                          'No possible moves, turn changes')

        self.assertEquals(self.game.next_turn(), 'Black')

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
        self.assertEquals(self.game.play(0, 0),
                          'Game over!')


if __name__ == "__main__":
    unittest.main()
