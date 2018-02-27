import unittest
from tateti import Tateti


class TestTateti(unittest.TestCase):

    def setUp(self):
        self.tateti = Tateti()

    def test_piezas_set_0(self):
        self.tateti.set(0, 1)
        self.assertEquals(
            self.tateti.board,
             "[[0, 'X', 0], [0, 0, 0], [0, 0, 0]]",
        )

    def test_piezas_set_1(self):
        self.tateti.set(2, 1)
        self.assertEquals(
            self.tateti.board,
             "[[0, 0, 0], [0, 0, 0], [0, 'X', 0]]",
        )
        self.tateti.set(0, 0)
        self.assertEquals(
            self.tateti.board,
             "[['O', 0, 0], [0, 0, 0], [0, 'X', 0]]",
        )

    def test_set_negative_exception(self):
        with self.assertRaises(Exception) as e:
            self.tateti.set(-1, 1)
            self.assertEqual(e.exception.message, "Movmiento no permitido.",)

    def test_set_negative_exception_2(self):
        with self.assertRaises(Exception) as e:
            self.tateti.set(-1, -1)
            self.assertEqual(e.exception.message, "Movmiento no permitido.",)

    def test_set_negative_exception_3(self):
        with self.assertRaises(Exception) as e:
            self.tateti.set(1, -1)
            self.assertEqual(e.exception.message, "Movmiento no permitido.",)

    def test_set_caracter_invalid(self):
        with self.assertRaises(Exception) as e:
            self.tateti.set('a', 'b')
            self.assertEqual(e.exception.message, "Movmiento no permitido.",)




if __name__ == "__main__":
    unittest.main()
