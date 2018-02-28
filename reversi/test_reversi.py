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

    def test_wrong_movement(self):
        self.assertEquals(self.game.play(1, 1), 'Movimiento no permitido')


if __name__ == "__main__":
        unittest.main()
