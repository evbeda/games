import unittest
from Four_number import FourNumber


class TestFourNumber(unittest.TestCase):

    def setUp(self):
        self.game = FourNumber()
        self.game.chose_number = 1234

    def initial_status(self):
        self.assertTrue(self.game.is_playing)

    def test_play_smaller_number(self):
        self.assertFalse(self.game.valid_number(399))

    def test_play_bigger_number(self):
        enter_number = self.game.valid_number(40000)
        self.assertFalse(enter_number, 'invalid number')

    def test_play_correct_number_equal(self):
        enter_number = self.game.play(1234)
        self.assertEqual(enter_number, '4B')

    def test_play_correct_number_1(self):
        enter_number = self.game.play(1240)
        self.assertEqual(enter_number, '2B')

    def test_play_correct_number_2(self):
        enter_number = self.game.play(2554)
        self.assertEqual(enter_number, '1R, 1B')

    def test_play_correct_number_3(self):
        enter_number = self.game.play(3421)
        self.assertEqual(enter_number, '4R')

    def test_play_correct_number_4(self):
        enter_number = self.game.play(5555)
        self.assertEqual(enter_number, '0 coincidence')


if __name__ == "__main__":
    unittest.main()
