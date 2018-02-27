import unittest
from ReversiGame import ReversiGame
from tablero_reversi import TableroReversi


class TestReversi(unittest.TestCase):

    def setUp(self):
        self.game = ReversiGame()

    def test_initial_status(self):
        self.assertTrue(self.game.playing)

    def test_initial_next_turn_whites(self):
        self.assertEquals(
            self.game.next_turn(),
            'Turn of the whiteones',
        )

    def test_initial_play_white(self):
        self.assertEquals(
            self.game.next_turn(),
            'Turn of the whiteones',
        )

    def test_initial_tablero(self):
        for column in xrange(1, 8):
            for row in xrange(1, 8):
                if (column == 4 and row == 4) or (column == 5 and row == 5):
                    self.assertEqual(
                        self.game.tablero.matrix_tablero[column][row], 1)
                elif (column == 4 and row == 5) or (column == 5 and row == 4):
                    self.assertEqual(
                        self.game.tablero.matrix_tablero[column][row], 2)
                else:
                    self.assertEqual(
                        self.game.tablero.matrix_tablero[column][row], 0)

#    @unittest.skip
#    def test_initial_play_white(self):
#        colum = 5
#        row = 3
#        self.assertEqual(self.game.play(colum, row), 1)

    def test_validate_empty_position(self):
        self.assertTrue(self.game.validate_empty(1, 1))

#    def test_validate_enemy_position(self):
#        self.assertTrue(self.game.validate_enemy_position(5, 3))
    if __name__ == "__main__":
        unittest.main()
