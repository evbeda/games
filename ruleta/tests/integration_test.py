# Modules
from unittest import TestCase
from parameterized import parameterized
from unittest.mock import patch
# Model
from ..player import Player
from ..croupier import Croupier
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
# Messages
from .. import (
    SUCCESS_MESSAGE,
    NOT_ENOUGH_CASH_MESSAGE,
    INVALID_BET_MESSAGE,
    INVALID_BET_TYPE_MESSAGE,
    BYE_MESSAGE,
    END_GAME_COMMAND,
    GO_COMMAND,
    WON_MESSAGE,
    LOST_MESSAGE
)


class IntegrationTest(TestCase):
    # Test for the game roullete
    def setUp(self):
        self.player = Player(100)
        self.croupier = Croupier(self.player)
        self.game = GameRoulette()

    def test_resolve_command_method(self):
        result = self.game.resolve_command('STRAIGHT_BET 14 100')
        self.assertEqual(('STRAIGHT_BET', [14], 100), result)

    @parameterized.expand([
        (END_GAME_COMMAND, '', '', BYE_MESSAGE),
        ('STRAIGHT_BET', '10', 15, SUCCESS_MESSAGE),
        ('STREET_BET', '1_2_3', 10, SUCCESS_MESSAGE),
        ('STRAIGHT_BET', '40', 10, INVALID_BET_MESSAGE),
        ('INVALID_BET', '10', 15, INVALID_BET_TYPE_MESSAGE),
        ('STRAIGHT_BET', '20', 200, NOT_ENOUGH_CASH_MESSAGE)
    ])
    def test_user_typing_return_message(
            self, bet_type, bet_value, amount, expected_message):
        self.assertEqual(expected_message, self.game.play(
            bet_type, bet_value, amount))

    @patch('ruleta.roulette.randint', return_value=30)
    def test_play_round_win(self, mock_randint):
        self.player = Player(50)
        self.game.croupier.add_bet(StraightBet([30], 25))
        self.assertEqual(
            WON_MESSAGE + '875 chips\nRANDOM NUMBER: 30',
            self.game.play(GO_COMMAND)
            )

    @patch('ruleta.roulette.randint', return_value=31)
    def test_play_round_lost(self, mock_randint):
        self.player = Player(50)
        self.game.croupier.add_bet(StraightBet([30], 25))
        self.assertEqual(
            LOST_MESSAGE + '\nRANDOM NUMBER: 31', self.game.play(GO_COMMAND))

    def test_next_turn(self):
        self.assertEqual(
            'STRAIGHT_BET, COLOR_BET, EVENODD_BET, LOWHIGH_BET, STREET_BET, '
            'SIXLINE_BET, DOUBLE_BET, ONEDOZEN_BET, TWODOZEN_BET, TRIO_BET, '
            'QUADRUPLE_BET\n'
            'GO,\n'
            'END_GAME',
            self.game.next_turn(),
        )

    def test_show_board(self):
        self.game.croupier.add_bet(StraightBet(['19'], 25))
        self.game.croupier.add_bet(EvenOddBet(['odd'], 10))
        self.assertEqual(
            "+--+--+--+--+--+--+--+--+--+--+--+--+--+\n" +\
            "|00|03|06|09|12|15|18|21|24|27|30|33|36|\n" +\
            "+--+--+--+--+--+--+--+--+--+--+--+--+--+\n" +\
            "|00|02|05|08|11|14|17|20|23|26|29|32|35|\n" +\
            "+--+--+--+--+--+--+--+--+--+--+--+--+--+\n" +\
            "|00|01|04|07|10|13|16|19|22|25|28|31|34|\n" +\
            "+--+--+--+--+--+--+--+--+--+--+--+--+--+\n" +\
            "Player Money: $65\n" +\
            "Placed Bets: \n" +\
            "STRAIGHT_BET 19, bet $25\n" +\
            "EVENODD_BET odd, bet $10", self.game.board)

