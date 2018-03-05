import unittest
from tateti import Tateti


class TestTateti(unittest.TestCase):

    def setUp(self):
        self.tateti = Tateti()

    def test_initial_playing(self):
        self.assertTrue(self.tateti.is_playing)

    def test_piezas_play_0(self):
        self.tateti.play(0, 1)
        self.assertEquals(
            str(self.tateti.tablero),
            "[[0, 'X', 0], [0, 0, 0], [0, 0, 0]]",
        )

    def test_piezas_play_1(self):
        self.tateti.play(2, 1)
        self.assertEquals(
            str(self.tateti.tablero),
            "[[0, 0, 0], [0, 0, 0], [0, 'X', 0]]",
        )
        self.tateti.play(0, 0)
        self.assertEquals(
            str(self.tateti.tablero),
            "[['O', 0, 0], [0, 0, 0], [0, 'X', 0]]",
        )

    def test_play_negative_exception(self):
        self.assertEqual(self.tateti.play(-1, 1), "Movement not allowed.",)

    def test_play_negative_exception_2(self):
        self.assertEqual(self.tateti.play(-1, -1), "Movement not allowed.",)

    def test_play_negative_exception_3(self):
        self.assertEqual(self.tateti.play(1, -1), "Movement not allowed.",)

    def test_play_caracter_invalid(self):
        self.assertEqual(self.tateti.play('a', 'b'), "Movement not allowed.",)

    def test_next_O(self):
        self.assertEqual(self.tateti.next_turn(), "Plays O")

    def test_next_X(self):
        self.tateti.play(1, 1)
        self.assertEqual(self.tateti.next_turn(), "Plays X")

    def test_repeat_movement(self):
        self.tateti.play(2, 1)
        self.assertEquals(
            str(self.tateti.tablero),
            "[[0, 0, 0], [0, 0, 0], [0, 'X', 0]]",
        )
        with self.assertRaises(Exception) as e:
            self.tateti.play(2, 1)
            self.assertEqual(e.exception.message, "Movement not allowed.",)

    def test_win_horizontal(self):
        self.tateti.play(0, 0)
        self.tateti.play(1, 0)
        self.tateti.play(0, 1)
        self.tateti.play(2, 1)
        self.tateti.play(0, 2)
        self.assertEqual(self.tateti.next_turn(), "X wins")

    def test_tie(self):
        self.tateti.play(0, 0)
        self.tateti.play(0, 1)
        self.tateti.play(0, 2)
        self.tateti.play(1, 2)
        self.tateti.play(1, 1)
        self.tateti.play(2, 2)
        self.tateti.play(1, 0)
        self.tateti.play(2, 0)
        self.tateti.play(2, 1)
        self.assertEqual(self.tateti.next_turn(), "It's a TIE!")

    def test_win_vertical(self):
        self.tateti.play(0, 0)
        self.tateti.play(1, 1)
        self.tateti.play(1, 0)
        self.tateti.play(0, 2)
        self.tateti.play(2, 0)
        self.assertEqual(self.tateti.next_turn(), "X wins")

    def test_position_taken(self):
        self.tateti.play(0, 0)
        self.assertEqual(self.tateti.play(0, 0), "Position already taken. Please, choose another one.")

    def test_win_diagon_des(self):
        self.tateti.play(0, 0)
        self.tateti.play(0, 1)
        self.tateti.play(1, 1)
        self.tateti.play(0, 2)
        self.tateti.play(2, 2)
        self.assertEqual(self.tateti.next_turn(), "X wins")

    def test_win_diagon_asc(self):
            self.tateti.play(0, 2)
            self.tateti.play(0, 1)
            self.tateti.play(1, 1)
            self.tateti.play(0, 0)
            self.tateti.play(2, 0)
            self.assertEqual(self.tateti.next_turn(), "X wins")

    def test_win_vertical_2(self):
            self.tateti.play(0, 0)
            self.tateti.play(0, 1)
            self.tateti.play(1, 0)
            self.tateti.play(1, 1)
            self.tateti.play(2, 0)
            self.assertEqual(self.tateti.next_turn(), "X wins")


if __name__ == "__main__":
    unittest.main()
