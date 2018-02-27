import unittest
from tateti import Tateti


class TestTateti(unittest.TestCase):

    def test_create_tablero(self):
        tablero = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]

        tateti = Tateti()
        new_tablero = tateti.create_tablero()
        self.assertEquals(new_tablero, tablero)


if __name__ == "__main__":
    unittest.main()
