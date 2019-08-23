# Modules
from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized
# Model
from ..croupier import Croupier
from ..player import Player
from ..game_roullete import GameRoulette
from ..bet import (
    StraightBet,
    ColorBet,
    EvenOddBet,
    LowHighBet,
    StreetBet,
    SixLineBet,
    DoubleBet,
)
# Exceptions
from ..exceptions.out_of_cash_exception import OutOfCashException


class TestCroupier(TestCase):
    def setUp(self):
        self.player = Player(100)
        self.croupier = Croupier(self.player)
        self.game = GameRoulette()

    # Test for the croupier
    def test_player_bets_100_but_have_50_should_fail(self):
        self.croupier = Croupier(Player(50))
        with self.assertRaises(OutOfCashException):
            self.croupier.discount_money_from_player(100)

    def test_player_have_100_bets_50_will_have_50(self):
        self.croupier.discount_money_from_player(50)
        self.assertEqual(50, self.player.money)

    def test_croupier_add_a_bet(self):
        self.croupier.add_bet(StraightBet([13], 10))
        self.assertEqual(1, len(self.croupier.round.bets))

    @patch('ruleta.roulette.randint', return_value=30)
    def test_croupier_add_reward_to_player(self, mock_randint):
        self.player = Player(50)
        self.croupier = Croupier(self.player)
        self.croupier.add_bet(StraightBet([30], 25))
        self.croupier.add_bet(EvenOddBet(['even'], 10))
        self.croupier.add_bet(LowHighBet(['low'], 5))
        self.croupier.play()
        self.assertEqual(self.player.money, 905)

    def test_show_player_money(self):
        self.assertEqual(self.croupier.show_player_money(), "$100")

    @parameterized.expand([
        ([], "No bets"),
        ([StraightBet([15], 10)], "STRAIGHT_BET 15, bet $10"),
        ([StraightBet([15], 10), DoubleBet([3, 6], 20)],
            "STRAIGHT_BET 15, bet $10\nDOUBLE_BET 3 6, bet $20"),
    ])
    def test_show_placed_bets(self, bets, expected):
        for bet in bets:
            self.croupier.add_bet(bet)
        self.assertEqual(self.croupier.show_placed_bets(), expected)
