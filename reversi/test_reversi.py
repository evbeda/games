import unittest
from ReversiGame import ReversiGame


class TestReversi(unittest.TestCase):

    def setUp(self):
        self.game = ReversiGame()

    def test_initial_status(self):
        self.assertTrue(self.game.playing)
        self.assertEquals(self.game.tablero[3][3], 'B')
        self.assertEquals(self.game.tablero[3][4], 'W')
        self.assertEquals(self.game.tablero[4][3], 'W')
        self.assertEquals(self.game.tablero[4][4], 'B')

    def test_initial_next_turn_whites(self):
        self.assertEquals(
            self.game.next_turn(),
            'Turn of the whiteones',
        )

    def test_wrong_movement_empty(self):
        self.assertEquals(self.game.play(1, 1), 'Movimiento no permitido')

    def test_wrong_movement_occupied(self):
        self.assertEquals(self.game.play(3, 4), 'Movimiento no permitido')

    def test_valid_move(self):
        self.assertEquals(self.game.play(3, 5), 'Correcto')

    def test_get_directions(self):
        result = [
            [(3, 4, 'W')]
        ]
        self.assertEquals(result, self.game.get_directions(3, 5))

    def test_get_all_directions_white(self):
        self.game.tablero = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'W', 'W', 'W', 'W', 'W', ' '],
            [' ', ' ', 'W', 'B', 'B', 'B', 'W', ' '],
            [' ', ' ', 'W', 'B', ' ', 'B', 'W', ' '],
            [' ', ' ', 'W', 'B', 'B', 'B', 'W', ' '],
            [' ', ' ', 'W', 'W', 'W', 'W', 'W', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ]
        self.game.playingBlack = False
        result = [
            [(3, 3, 'B')], [(4, 3, 'B')],
            [(4, 4, 'B')], [(4, 5, 'B')],
            [(3, 5, 'B')], [(2, 5, 'B')],
            [(2, 4, 'B')], [(2, 3, 'B')]
        ]
        self.assertEquals(result, self.game.get_directions(3, 4))

    def test_get_all_directions_black(self):
        self.game.tablero = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'B', 'B', 'B', 'B', 'B', ' '],
            [' ', ' ', 'B', 'W', 'W', 'W', 'B', ' '],
            [' ', ' ', 'B', 'W', ' ', 'W', 'B', ' '],
            [' ', ' ', 'B', 'W', 'W', 'W', 'B', ' '],
            [' ', ' ', 'B', 'B', 'B', 'B', 'B', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ]
        result = [
            [(3, 3, 'W')], [(4, 3, 'W')],
            [(4, 4, 'W')], [(4, 5, 'W')],
            [(3, 5, 'W')], [(2, 5, 'W')],
            [(2, 4, 'W')], [(2, 3, 'W')]
        ]
        self.assertEquals(result, self.game.get_directions(3, 4))


if __name__ == "__main__":
    unittest.main()
