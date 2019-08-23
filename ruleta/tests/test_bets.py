# Modules
from unittest import TestCase
from parameterized import parameterized

# Model classes
from ..bet import (
    BetCreator,
    StraightBet,
    ColorBet,
    EvenOddBet,
    LowHighBet,
    StreetBet,
    SixLineBet,
    DoubleBet,
    OneDozenBet,
    TwoDozenBet,
    TrioBet,
    QuadrupleBet
)

# Exceptions
from ..exceptions.invalid_bet_exception import InvalidBetException
from ..exceptions.invalid_bet_type_exception import InvalidBetTypeException

# Const
bet_scenario = [
    # tipo de apuesta, tipo_input, amount, prize, number chosen, won/lose
    (StraightBet, ['36'], 25, 875, 36, True),
    (ColorBet, ['Red'], 300, 600, 36, True),
    (ColorBet, ['Black'], 300, 600, 29, True),
    (ColorBet, ['Red'], 300, 0, 29, False),
    (ColorBet, ['Black'], 300, 0, 36, False),
    (EvenOddBet, ['ODD'], 30, 0, 36, False),
    (StraightBet, ['36'], 25, 0, 35, False),
    (ColorBet, ['Red'], 300, 0, 35, False),
    (EvenOddBet, ['ODD'], 30, 60, 35, True),
    (StreetBet, [13, 14, 15], 10, 110, 14, True),
    (StreetBet, [13, 14, 15], 10, 0, 10, False),
    (SixLineBet, [1, 4], 30, 150, 6, True),
    (SixLineBet, [1, 4], 30, 0, 8, False),
    (DoubleBet, [1, 2], 50, 850, 2, True),
    (DoubleBet, [0, 2], 50, 0, 5, False),
    (OneDozenBet, [1], 10, 20, 3, True),
    (OneDozenBet, [1], 10, 0, 23, False),
    (TwoDozenBet, [1, 2], 10, 15, 3, True),
    (TwoDozenBet, [2, 3], 10, 15, 18, True),
    (TwoDozenBet, [2, 3], 10, 0, 2, False),
    (TrioBet, [0, 2, 3], 10, 110, 2, True),
    (TrioBet, [0, 1, 2], 10, 110, 2, True),
    (TrioBet, [0, 2, 3], 10, 0, 5, False),
    (TrioBet, [0, 1, 2], 10, 0, 5, False),
    (QuadrupleBet, [1, 2, 4, 5], 10, 80, 2, True),
    (QuadrupleBet, [1, 2, 4, 5], 10, 0, 10, False),
]

RED_CORRECT_VALUES = \
    [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

BLACK_CORRECT_VALUES = \
    [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

LIST_OF_BETS = \
    'STRAIGHT_BET, COLOR_BET, EVENODD_BET, ' + \
    'LOWHIGH_BET, STREET_BET, SIXLINE_BET, ' + \
    'DOUBLE_BET, ONEDOZEN_BET, TWODOZEN_BET, ' + \
    'TRIO_BET, QUADRUPLE_BET'


class TestBetsRoulette(TestCase):
    # Test for the bets
    @parameterized.expand([
        (StraightBet, ['40'], 17),
        (ColorBet, ['Reds'], 300),
        (ColorBet, ['Blacks'], 300),
        (EvenOddBet, ['ODDs'], 30),
        (LowHighBet, ['Lower'], 11),
        (StreetBet, ['1', '2', '4'], 100),
        (SixLineBet, ['12', '13'], 10),
        (DoubleBet, [0, 36], 100),
        (DoubleBet, [0, 0], 50),
        (DoubleBet, ['19', '18'], 50),
        (DoubleBet, [5, 7], 50),
        (OneDozenBet, ['4'], 50),
        (TwoDozenBet, ['1', '1'], 50),
        (TwoDozenBet, ['1'], 50),
        (TwoDozenBet, [1, 4], 50),
        (TrioBet, ['0', '1', '3'], 50),
        (TrioBet, [0, 1], 50),
        (TrioBet, [0, 1, 4], 50),
        (TrioBet, [1, 2, 3], 50),
        (QuadrupleBet, ['1', '3', '2', '6'], 10),
        (QuadrupleBet, [0, 1, 2, 3], 10),
        (QuadrupleBet, [1, 2, 7, 8], 10),
        (QuadrupleBet, [1, 2, 7, 9], 10),
        (QuadrupleBet, [1, 2, 3], 10),
        (QuadrupleBet, [1, 2, 4, 5, 7], 10)
    ])
    def test_invalid_bets(self, bet, bet_value, ammount):
        with self.assertRaises(InvalidBetException):
            bet(bet_value, ammount)

    # Test for the bets
    @parameterized.expand([
        (StraightBet, [30], [30]),
        (ColorBet, ['Red'], RED_CORRECT_VALUES),
        (ColorBet, ['black'], BLACK_CORRECT_VALUES),
        (EvenOddBet, ['ODD'], [x for x in range(1, 37) if x % 2 == 1]),
        (EvenOddBet, ['EvEN'], [x for x in range(1, 37) if x % 2 == 0]),
        (LowHighBet, ['Low'], [x for x in range(1, 19)]),
        (LowHighBet, ['high'], [x for x in range(19, 37)]),
        (StreetBet, [1, 2, 3], [1, 2, 3]),
        (SixLineBet, [25, 28], [25, 26, 27, 28, 29, 30]),
        (DoubleBet, [2, 5], [2, 5]),
        (DoubleBet, [33, 36], [33, 36]),
        (DoubleBet, [1, 2], [1, 2]),
        (DoubleBet, [0, 3], [0, 3]),
        (DoubleBet, [4, 7], [4, 7]),
        (OneDozenBet, [1], [x for x in range(1, 13)]),
        (OneDozenBet, [2], [x for x in range(13, 25)]),
        (OneDozenBet, [3], [x for x in range(25, 37)]),
        (TwoDozenBet, [1, 2], [x for x in range(1, 25)]),
        (TwoDozenBet, [2, 3], [x for x in range(13, 37)]),
        (TwoDozenBet, [1, 3], [x for x in range(1, 13)] +
            [x for x in range(25, 37)]),
        (TrioBet, [0, 1, 2], [0, 1, 2]),
        (TrioBet, [0, 2, 3], [0, 2, 3]),
        (TrioBet, [2, 3, 0], [0, 2, 3]),
        (QuadrupleBet, [1, 2, 4, 5], [1, 2, 4, 5]),
        (QuadrupleBet, [1, 2, 5, 4], [1, 2, 4, 5])
    ])
    def test_valid_bets(self, bet, bet_value, expected_target_numbers):
        bet = bet(bet_value, 10)
        self.assertEqual(bet.target_numbers, expected_target_numbers)

    @parameterized.expand(bet_scenario)
    def test_is_winner(
            self, bet, bet_value, ammount, award, chosen_number, expect_winner
            ):
        bet_type = bet(bet_value, ammount)
        self.assertEqual(bet_type.is_winner(chosen_number), expect_winner)

    @parameterized.expand(bet_scenario)
    def test_win_bet(
        self,
        bet,
        bet_value,
        ammount,
        award,
        chosen_number,
        expected_winner,
    ):
        bet_type = bet(bet_value, ammount)
        self.assertEqual(
            bet_type.calculate_award(chosen_number),
            award,
        )


class TestBetCreator(TestCase):
    # Tests for the bet creator
    @parameterized.expand([
        ('STRAIGHT_BET', '15', 17, StraightBet),
        ('COLOR_BET', 'Red', 300, ColorBet),
        ('EVENODD_BET', 'ODD', 30, EvenOddBet),
        ('LOWHIGH_BET', 'Low', 11, LowHighBet),
        ('STREET_BET', '16_17_18', 100, StreetBet),
        ('SIXLINE_BET', '16_19', 10, SixLineBet),
        ('DOUBLE_BET', '23_24', 30, DoubleBet),
        ('ONEDOZEN_BET', '1', 20, OneDozenBet),
        ('TWODOZEN_BET', '1_2', 20, TwoDozenBet),
        ('TRIO_BET', '0_2_3', 20, TrioBet),
        ('QUADRUPLE_BET', '1_2_4_5', 20, QuadrupleBet)
    ])
    def test_bet_creator(
            self, bet_type, bet_values, amount, expected_instance):
        bet = BetCreator.create(bet_type, bet_values, amount)
        self.assertIsInstance(bet, expected_instance)

    def test_invalid_type_bet(self):
        with self.assertRaises(InvalidBetTypeException):
            BetCreator.validate_bet_type('INVALID_BET')

    @parameterized.expand([
        (StraightBet([15], 10), "STRAIGHT_BET 15, bet $10"),
        (DoubleBet([3, 6], 20), "DOUBLE_BET 3 6, bet $20"),
        (ColorBet(['red'], 15), "COLOR_BET red, bet $15"),
        (EvenOddBet(['odd'], 30), "EVENODD_BET odd, bet $30"),
        (LowHighBet(['high'], 25), "LOWHIGH_BET high, bet $25"),
        (StreetBet([1, 2, 3], 35), "STREET_BET 1 2 3, bet $35"),
        (SixLineBet([1, 4], 40), "SIXLINE_BET 1 2 3 4 5 6, bet $40"),
        (OneDozenBet([1], 30), "ONEDOZEN_BET 1 dozen, bet $30"),
        (TwoDozenBet([2, 3], 40), "TWODOZEN_BET 2 3 dozens, bet $40"),
        (TrioBet([1, 2, 0], 5), "TRIO_BET 0 1 2, bet $5"),
        (QuadrupleBet([7, 8, 10, 11], 50), "QUADRUPLE_BET 7 8 10 11, bet $50")
    ])
    def test_bet_to_string(self, bet, expected):
        self.assertEqual(str(bet), expected)

    def test_list_of_bets(self):
        self.assertEqual(LIST_OF_BETS, BetCreator.list_bets())

    @parameterized.expand([
        (ColorBet(['red'], 5), 'red'),
        (ColorBet(['black'], 5), 'black')
    ])
    def test_get_color(self, bet, expected):
        self.assertEqual(bet.get_color(), expected)

    @parameterized.expand([
        (EvenOddBet(['even'], 5), 'even'),
        (EvenOddBet(['odd'], 5), 'odd')
    ])
    def test_get_odd_or_even(self, bet, expected):
        self.assertEqual(bet.get_odd_or_even(), expected)

    @parameterized.expand([
        (LowHighBet(['low'], 5), 'low'),
        (LowHighBet(['high'], 5), 'high')
    ])
    def test_get_low_or_high(self, bet, expected):
        self.assertEqual(bet.get_low_or_high(), expected)

    @parameterized.expand([
        (OneDozenBet([1], 5), 1),
        (OneDozenBet([2], 5), 2),
        (OneDozenBet([3], 5), 3),
    ])
    def test_get_dozen(self, bet, expected):
        self.assertEqual(bet.get_dozen(), expected)

    @parameterized.expand([
        (TwoDozenBet([1, 2], 5), [1, 2]),
        (TwoDozenBet([2, 3], 5), [2, 3]),
        (TwoDozenBet([1, 3], 5), [1, 3]),
    ])
    def test_get_dozens(self, bet, expected):
        self.assertEqual(bet.get_dozens(), expected)
