import unittest
from four_number import FourNumber


class TestFourNumber(unittest.TestCase):

    def setUp(self):
        self.game = FourNumber()
        self.game.chose_number = 1234

    def initial_status(self):
        self.assertTrue(self.game.is_playing)

    def test_play_smaller_number(self):
        self.assertEquals(self.game.same_enter_number(19), 'invalid number')
        self.assertTrue(self.game.is_playing)

    def test_play_invalid_number(self):
        self.assertEquals(self.game.same_enter_number(1210), 'invalid number')
        self.assertEquals(self.game.same_enter_number(2210), 'invalid number')
        self.assertEquals(self.game.same_enter_number(1291), 'invalid number')
        self.assertEquals(self.game.same_enter_number(8121), 'invalid number')

    def test_play_valid_number(self):
        self.assertEquals(self.game.same_enter_number(1230), 'valid number')
        self.assertEquals(self.game.same_enter_number(3210), 'valid number')
        self.assertEquals(self.game.same_enter_number(1298), 'valid number')
        self.assertEquals(self.game.same_enter_number(8145), 'valid number')

    def test_play_bigger_number(self):
        self.assertEquals(self.game.same_enter_number(40000), 'invalid number')
        self.assertTrue(self.game.is_playing)

    def test_play_correct_number_equal(self):
        self.assertEquals(self.game.play(1234), '4G, You win')
        self.assertTrue(self.game.is_playing)

    def test_play_correct_number_1(self):
        self.assertEquals(self.game.play(1240), '2G 1R')
        self.assertTrue(self.game.is_playing)

    def test_play_incorrect_number_2(self):
        self.assertEquals(self.game.same_enter_number(2554), 'invalid number')
        self.assertTrue(self.game.is_playing)

    def test_play_correct_number_3(self):
        self.assertEquals(self.game.play(3421), '4R')
        self.assertTrue(self.game.is_playing)

    def test_play_correct_number_4(self):
        self.assertEqual(self.game.play(5678), '0 coincidence')
        self.assertTrue(self.game.is_playing)

    def test_play_correct_number_5(self):
        self.assertEqual(self.game.play(345), '2R')
        self.assertTrue(self.game.is_playing)

    def test_play_correct_number_6(self):
        self.assertEqual(self.game.play(412), '3R')
        self.assertTrue(self.game.is_playing)

    def test_play_correct_number_7(self):
        self.assertEqual(self.game.play(8247), '1G 1R')
        self.assertTrue(self.game.is_playing)

    def test_play_correct_number_8(self):
        self.assertEqual(self.game.play(1267), '2G')
        self.assertTrue(self.game.is_playing)


if __name__ == "__main__":
    unittest.main()
