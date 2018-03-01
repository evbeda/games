import unittest
from buscaminas import Buscaminas


class TestBuscamina(unittest.TestCase):

    def setUp(self):
        self.game = Buscaminas()
        self.game.bombs = [
            (1, 1, ), (2, 4, ), (1, 2, ),
            (3, 4, ), (4, 3, ), (2, 1, ),
            (5, 3, ), (3, 5, ), (6, 1, ),
            (7, 2, ),
        ]
        self.game.generate_board()

    def test_initial_status(self):
        self.game.bombs = []
        self.assertTrue(self.game.playing)
        self.assertEqual(10, self.game.generate_bombs())

    def test_bomba_encontrada(self):
        play_result = self.game.play(1, 1)
        self.assertEqual(play_result, 'You lost')
        self.assertFalse(self.game.playing)

    def test_bomba_no_encontrada(self):
        play_result = self.game.play(2, 3)
        self.assertEqual(play_result, 'No bomb, keep going')
        self.assertTrue(self.game.playing)

    def test_gano(self):
        self.game.number_clicks = 64 - len(self.game.bombs)
        play_result = self.game.play(1, 3)
        self.assertEqual(play_result, 'You win')
        self.assertFalse(self.game.playing)

    def test_board(self):
        result = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', 'B', 'B', ' ', ' ', ' ', ' ', ' '],
            [' ', 'B', ' ', ' ', 'B', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', 'B', 'B', ' ', ' '],
            [' ', ' ', ' ', 'B', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', 'B', ' ', ' ', ' ', ' '],
            [' ', 'B', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'B', ' ', ' ', ' ', ' ', ' '],
        ]

        self.assertEqual(result, self.game.check_board())

    def test_click(self):
        result = [
            (0, 0, ), (0, 1, ), (0, 2, ),
            (0, 3, ), (0, 4, ), (0, 5, ),
            (0, 6, ), (1, 0, ), (1, 1, ),
            (1, 2, ), (1, 3, ), (1, 4, ),
            (1, 5, ), (1, 6, ), (2, 0, ),
            (2, 1, ), (2, 2, ), (2, 3, ),
            (2, 4, ), (2, 5, ), (2, 6, ),
            (3, 0, ), (3, 1, ), (3, 2, ),
            (3, 3, ), (3, 4, ), (3, 5, ),
            (3, 6, ), (4, 0, ), (4, 1, ),
            (4, 2, ), (4, 3, ), (4, 4, ),
            (4, 5, ), (4, 6, ), (5, 0, ),
            (5, 1, ), (5, 2, ), (5, 3, ),
            (5, 4, ), (5, 5, ), (5, 6, ),
            (6, 0, ), (6, 1, ), (6, 2, ),
            (6, 3, ), (6, 4, ), (6, 5, ),
            (6, 6, ),
        ]
        self.assertEqual(result, self.game.possible_clicks())

    def test_two_clicks_same_place(self):
        self.game.play(1, 3,)
        self.assertEqual('esa posicion ya fue seleccionada', self.game.play(1, 3, ))

    def test_multiple_clicks(self):
        self.game.play(2, 2, )
        result = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', 'B', 'B', ' ', ' ', ' ', ' ', ' '],
            [' ', 'B', '3', ' ', 'B', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', 'B', 'B', ' ', ' '],
            [' ', ' ', ' ', 'B', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', 'B', ' ', ' ', ' ', ' '],
            [' ', 'B', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'B', ' ', ' ', ' ', ' ', ' '],
        ]
        print '-------- RESULT'
        print result
        print '--------- BOARD'
        print self.game.check_board()
        self.assertEquals(result, self.game.check_board())

    def test_wrong_movement(self):
        play_result = self.game.play(-1, 8)
        self.assertEqual(play_result, 'Movimiento no permitido')


if __name__ == "__main__":
    unittest.main()
