import unittest
from buscaminas import Buscaminas


class TestBuscamina(unittest.TestCase):

    def setUp(self):
        self.game = Buscaminas()
        self.game.bombs = [(1, 1, ), (2, 4, )]

    def test_initial_status(self):
        self.assertTrue(self.game.playing)


if __name__ == "__main__":
    unittest.main()
