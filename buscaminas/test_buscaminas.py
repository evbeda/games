import unittest
from buscaminas import Buscaminas


class TestBuscamina(unittest.TestCase):

    def setUp(self):
        self.game = Buscaminas()
        self.game.bombs = [(1, 1, ), (2, 4, )]

    def test_initial_status(self):
        self.assertTrue(self.game.playing)
        self.assertEqual(10, self.game.armar_tablero())

    def test_bomba_encontrada(self):
        play_result = self.game.play(1, 1)
        self.assertEqual(play_result, 'You lost')
        self.assertFalse(self.game.playing)

    def test_bomba_no_encontrada(self):
        play_result = self.game.play(1, 2)
        self.assertEqual(play_result, 'No bomb, keep going')
        self.assertTrue(self.game.playing)

    def test_gano(self):
        self.game.number_clicks = 64 - len(self.game.bombs)
        play_result = self.game.play(1, 2)
        self.assertEqual(play_result, 'You win')
        self.assertFalse(self.game.playing)


if __name__ == "__main__":
    unittest.main()
