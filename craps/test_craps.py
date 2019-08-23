import unittest
from unittest.mock import patch
from parameterized import parameterized
from .exceptions.out_of_cash_exception import OutOfCashException
from .game import CrapsGame
from .turn import Turn
from .bet import BetCreator, PassBet
from .constants import (
    PLAYER_LOST,
    PLAYER_WON,
    GAME_OVER,
    GAME_STARTED,
    GAME_IN_PROGRESS,
    WON_MESSAGE,
    LOST_MESSAGE,
    BET_MESSAGE,
    BET_PLACED,
    INVALID_BET_TYPE,
    OUT_OF_CASH,
    CAN_NOT_LEAVE,
    PASS_BET,
    DO_NOT_PASS_BET,
    GO_COMMAND,
    NO_COMMAND,
    SHOOT_DICE_MESSAGE,
    BET_PAYED,
    INVALID_TURN_BET,
    DOUBLE_BET,
    SEVEN_BET,
    INVALID_INPUT
)


class TestCraps(unittest.TestCase):
    def setUp(self):
        self.game = CrapsGame()

    def test_craps_game_started(self):
        self.assertTrue(self.game.is_playing)
        self.assertIsInstance(self.game.turn, Turn)

    @parameterized.expand([
        (GAME_STARTED, [], 'Bets availables: PASS_BET, DO_NOT_PASS_BET, CRAPS_BET' + BET_MESSAGE),
    ])
    def test_craps_game_started_asks_for_a_bet(self, state, bets, message):
        self.game.turn.state = state
        self.game.turn.bets = bets
        self.assertEqual(self.game.next_turn(), message)

    def test_craps_game_in_progress_asks_for_a_bet(self):
        self.game.turn.state = GAME_IN_PROGRESS
        bets = 'Bets availables: '+BetCreator.list_bets(self.game.turn.state)
        self.assertEqual(self.game.next_turn(), bets+'\n'+SHOOT_DICE_MESSAGE)

    def test_craps_player_lost_aks_keep_playing(self):
        self.game.turn.state = PLAYER_LOST
        self.assertEqual(self.game.next_turn(), LOST_MESSAGE)

    def test_craps_player_won_aks_keep_playing(self):
        self.game.turn.state = PLAYER_WON
        self.assertEqual(self.game.next_turn(), WON_MESSAGE)

    @parameterized.expand([
        (PLAYER_WON, ),
        (PLAYER_LOST, ),
    ])
    def test_craps_player_wants_to_quit_allowed(self, state):
        self.game.turn.state = state
        self.assertEqual(self.game.play(NO_COMMAND), GAME_OVER)

    def test_craps_player_wants_to_quit_not_allowed(self):
        self.game.turn.state = GAME_IN_PROGRESS
        message = CAN_NOT_LEAVE + BET_MESSAGE
        self.assertEqual(self.game.play(NO_COMMAND), message)

    @parameterized.expand([
        ((2, 2),),
        ((2, 3),),
        ((4, 2),),
        ((4, 4),),
        ((5, 4),),
        ((5, 5),),
    ])
    def test_craps_play_returns_score(self, dice):
        with patch('random.sample', return_value=dice):
            self.assertEqual(self.game.play(GO_COMMAND), '\nResult:')

    def test_craps_game_input_bet_placed_message(self):
        returned_play = self.game.play(PASS_BET, 10)
        self.assertEqual(returned_play, BET_PLACED + PASS_BET)

    def test_craps_game_bet_added_to_bets_list(self):
        self.game.play(PASS_BET, 10)
        self.game.play(DO_NOT_PASS_BET, 20)
        self.assertEqual(len(self.game.turn.bets), 2)

    def test_craps_game_invalid_bet_type(self):
        returned_play = self.game.play("ASDF", 5678)
        self.assertEqual(returned_play, INVALID_BET_TYPE)

    def test_craps_not_enough_cash(self):
        turn = Turn()
        returned_play = self.game.play(PASS_BET, 9999999, turn)
        self.assertEqual(returned_play, OUT_OF_CASH)

    def test_craps_play_decrase_money(self):
        turn = Turn()
        self.game.play(DO_NOT_PASS_BET, 300, turn)
        self.assertEqual(self.game.money, 700)

    @parameterized.expand([
        (DOUBLE_BET, 2, 'GAME_STARTED'),
        (SEVEN_BET, 20, 'GAME_STARTED'),
    ])
    def test__play_catches_invalid_bet_turn_exception(self, bet, amount, turn_state):
        self.game.turn.state = turn_state
        self.assertEqual(self.game.play(bet, amount), INVALID_TURN_BET)

    def test_craps_decrease_money(self):
        self.game.decrease_money(200)
        self.assertEqual(self.game.money, 800)

    def test_craps_decrease_money_exception(self):
        with self.assertRaises(OutOfCashException):
            self.game.decrease_money(1200)

    @patch('random.sample', return_value=(1, 1))
    def test_craps_pay_bets_give_money(self, _):
        # bets 50 on winning and 100 on losing
        # 850 money remaining
        # loses (because of the patch), so wins 200
        # 1050 money remaining
        expected_money = 1050
        self.game.play(PASS_BET, 50)
        self.game.play(DO_NOT_PASS_BET, 100)
        self.game.play(GO_COMMAND)
        self.assertEqual(self.game.money, expected_money)

    @parameterized.expand([
        (PLAYER_WON, False),
        (PLAYER_LOST, False),
        (GAME_IN_PROGRESS, True)
    ])
    def test_craps_compare_turn_after_state(self, state, expected):
        self.game.turn.state = state
        first_turn = self.game.turn
        self.game.play(GO_COMMAND)
        is_same_turn = self.game.turn == first_turn
        self.assertEqual(is_same_turn, expected)

    @parameterized.expand([
        (GAME_STARTED, None, None, 1000, None, "\nPoint: -\nDice: No dices played\nMoney: 1000\n"),
        (GAME_STARTED, None, PassBet(20, None), 980, None, "\nPoint: -\nDice: No dices played\nBet:\n\tBet type: PassBet\n\tAmount bet: 20\n\tAmount payed: 0\n\tBet state: Bet in progress\nMoney: 980\n"),
        (GAME_IN_PROGRESS, 9, PassBet(20, (6, 3)), 980, None, "\nPoint: 9\nDice: (6, 3)\nBet:\n\tBet type: PassBet\n\tAmount bet: 20\n\tAmount payed: 0\n\tBet state: Bet in progress\nMoney: 980\n"),
        (PLAYER_LOST, 9, PassBet(200, (5, 2)), 800, None, "\nPoint: 9\nDice: (5, 2)\nBet:\n\tBet type: PassBet\n\tAmount bet: 200\n\tAmount payed: 0\n\tBet state: Bet in progress\nMoney: 800\n"),
        (PLAYER_WON, 6, PassBet(200, (4, 2)), 1200, 400, "\nPoint: 6\nDice: (4, 2)\nBet:\n\tBet type: PassBet\n\tAmount bet: 200\n\tAmount payed: 400\n\tBet state: Payed\nMoney: 1200\n"),
    ])
    def test_show_board(self, state, point, bet, money, amount_payed, expected):
        game = CrapsGame()
        game.turn.state = state
        game.turn.point = point
        if bet:
            game.turn.bets.append(bet)
            game.turn.dice = bet.selected_dices
            if state == PLAYER_WON:
                bet.amount_payed = amount_payed
                bet.state = BET_PAYED
        game.money = money
        boards = game.board
        self.assertEqual(boards, expected)

    def test_invalid_input(self):
        game = CrapsGame()
        self.assertEqual(game.play("something"), INVALID_INPUT)
