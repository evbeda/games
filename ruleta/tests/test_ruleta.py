from unittest import TestCase
from parameterized import parameterized
from ..roulette import Roulette
from ..board import get_color_from_number, get_dozen_from_number, show_board


class TestRoulette(TestCase):
    # Test for the roullete
    def setUp(self):
        self.roulette = Roulette()

    def test_numbers(self):
        number = self.roulette.generate_number()
        self.assertTrue(number in list(range(0, 37)))

    def test_history(self):
        number = self.roulette.generate_number()
        last_numbers = self.roulette.get_last_numbers()
        self.assertTrue(last_numbers[-1] == number)


class TestBoard(TestCase):
    # Test for the Board
    @parameterized.expand([
        (36,), (1,), (3,), (5,), (7,), (9,), (12,), (14,), (16,), (18,),
        (19,), (21,), (23,), (25,), (27,), (30,), (32,), (34,), (36,),
    ])
    def test_get_color_red_from_last_number(self, number):
        self.assertEqual('red', get_color_from_number(number))

    @parameterized.expand([
        (2,), (4,), (6,), (8,), (10,), (11,), (13,), (15,), (17,), (20,),
        (22,), (24,), (26,), (28,), (29,), (31,), (33,), (35,),
    ])
    def test_get_color_black_from_last_number(self, number):
        self.assertEqual('black', get_color_from_number(number))

    def test_get_color_green_from_last_number(self):
        self.assertEqual('green', get_color_from_number(0))

    @parameterized.expand([
        (1, 1), (3, 1), (5, 1), (7, 1), (9, 1), (12, 1),
        (14, 2), (16, 2), (18, 2), (19, 2), (21, 2), (24, 2),
        (25, 3), (27, 3), (30, 3), (32, 3), (34, 3), (36, 3),
    ])
    def test_get_dozen_from_last_number(self, number, dozen):
        self.assertEqual(dozen, get_dozen_from_number(number))

    def test_show_numbers_board(self):
        expected_board = "+--+--+--+--+--+--+--+--+--+--+--+--+--+\n" + \
            "|00|03|06|09|12|15|18|21|24|27|30|33|36|\n" + \
            "+--+--+--+--+--+--+--+--+--+--+--+--+--+\n" + \
            "|00|02|05|08|11|14|17|20|23|26|29|32|35|\n" + \
            "+--+--+--+--+--+--+--+--+--+--+--+--+--+\n" + \
            "|00|01|04|07|10|13|16|19|22|25|28|31|34|\n" + \
            "+--+--+--+--+--+--+--+--+--+--+--+--+--+\n"
        self.assertEqual(show_board(), expected_board)
