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
        self.assertEquals(result, self.game.find_white_pieces(3, 5))

    def test_get_multiple_directions(self):
        self.game.tablero = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', 'B', 'B', 'B', ' ', ' '],
            [' ', ' ', ' ', 'W', 'B', 'W', ' ', ' '],
            [' ', ' ', ' ', ' ', 'B', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ]
        self.game.playingBlack = False
        result = [
            [(3, 5, 'B')], [(3, 4, 'B')]
        ]
        self.assertEquals(result, self.game.find_black_pieces(2, 5))


if __name__ == "__main__":
    unittest.main()
