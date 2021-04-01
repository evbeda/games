import unittest
from unittest.mock import Mock
from unittest.mock import patch
from parameterized import parameterized
from ..qwixx import (
    Qwixx,
    QWIXX_STATE_START,
    QWIXX_STATE_OPTION,
    QWIXX_STATE_PLAY,
    QWIXX_TURN_WHITE,
    QWIXX_TURN_COLOR,
    OPTION_PLAY,
    OPTION_PASS,
)
from ..set_dices import SetDices
from ..score_pad import ScorePad
from ..row import Row


class TestQwixx(unittest.TestCase):
    def setUp(self):
        self.qwixx = Qwixx()

    def test_remove_dice_from_set(self):
        self.qwixx.dice_set = []

        colors = [
            'white',
            'white',
            'red',
            'yellow',
            'green',
            'blue',
        ]

        for color in colors:
            dice_mock = Mock()
            dice_mock.color = color
            self.qwixx.dice_set.append(dice_mock)

        self.qwixx.remove_dice('blue')
        self.assertNotIn('blue', [dice.color for dice in self.qwixx.dice_set])

    @parameterized.expand([
        (0, Exception),
        (6, Exception),
    ])
    def test_create_score_pad(self, n_player, expected):
        with self.assertRaises(Exception):
            self.qwixx.create_scored_pad(n_player)

    @parameterized.expand([
        (QWIXX_STATE_PLAY, QWIXX_TURN_COLOR, 2),
        (QWIXX_STATE_PLAY, '', 1),
        ('', QWIXX_TURN_COLOR, 1),
    ])
    def test_input_args(self, game_state, turn_color, expected):
        self.qwixx.game_state = game_state
        self.qwixx.turn_color = turn_color
        self.assertEqual(self.qwixx.input_args, expected)

    def test_new_game_player_count(self):
        qwixx = Qwixx()
        qwixx.create_scored_pad(2)
        self.assertEqual(len(qwixx.score_pad), 2)

    def test_new_game_player_limit(self):
        with self.assertRaises(Exception):
            Qwixx(5)

    @patch.object(ScorePad, 'mark_number_in_row')
    @patch.object(SetDices, 'get_value_of_die', return_value=2)
    def test_mark_with_white_call(self, mock_value_of_die, mock_mark_number):
        self.qwixx.score_pad = [ScorePad()]
        self.qwixx.mark_with_white(1)
        mock_mark_number.assert_called_once_with(4, 'red')

    def test_mark_with_white_error(self):
        self.qwixx.score_pad = [ScorePad()]
        msg = 'You cannot mark that row, the number must be on the right of the last mark!'
        self.qwixx.score_pad[0].rows['red'].marks.append(10)
        self.qwixx.mark_with_white(1)
        self.assertEqual(self.qwixx.mark_with_white(1), msg)

    def test_mark_with_white_error_row_is_locked(self):
        self.qwixx.score_pad = [ScorePad()]
        msg = 'It cannot be marked because the row is locked!'
        row = Row('blue')
        row.blocked_rows.append('blue')
        self.assertEqual(self.qwixx.mark_with_white(3), msg)

    @patch.object(Qwixx, "create_scored_pad")
    @patch.object(SetDices, "roll_dices")
    def test_play_players(self, mock_roll, mock_create):
        self.qwixx.play_start(5)
        mock_create.assert_called_once_with(5)
        mock_roll.assert_called_once_with()

    @parameterized.expand([
        (QWIXX_STATE_START, 'Enter number of players',),
        (QWIXX_STATE_OPTION, 'Game option:\n1) play \n2) pass',),
    ])
    def test_next_turn(self, state, expected):
        self.qwixx.game_state = state
        self.assertEqual(self.qwixx.next_turn(), expected)

    @parameterized.expand([
        (
            QWIXX_TURN_WHITE,
            'Choose in which row you want to mark the common dice\n'
            '1) red\n'
            '2) yellow\n'
            '3) blue\n'
            '4) green\n',
        ),
        (
            QWIXX_TURN_COLOR,
            'Choose a white and color die\n'
            '1-2) white die   1-4)color die',
        ),
    ])
    def test_next_turn_play(self, turn_color, expected):
        self.qwixx.game_state = QWIXX_STATE_PLAY
        self.qwixx.turn_color = turn_color
        self.assertEqual(self.qwixx.next_turn(), expected)

    @parameterized.expand([
        (2, 0, 5, 863),
        (4, 3, 5, 863),
    ])
    def test_board(self, cant_score_pad, id_player, marks, cant_letter):
        qwixx = Qwixx()
        qwixx.create_scored_pad(cant_score_pad)
        qwixx.current_player = id_player
        self.assertEqual(len(qwixx.board), cant_letter)

    @parameterized.expand([
        (Row('rojo'), 'green', 'not locked'),
        (Row('rojo'), 'rojo', 'is locked'),
    ])
    def test_is_locked(self, row, color_row, expected):
        row.blocked_rows.append(color_row)
        self.qwixx.is_locked(row)
        self.assertEqual(self.qwixx.is_locked(row), expected)

    @parameterized.expand([
        (Row('rojo'), 109),
        (Row('blue'), 109),
    ])
    def test_output_row(self, row, expected):
        self.assertEqual(len(self.qwixx.output_row(row)), expected)

    @patch.object(Qwixx, 'play_start')
    def test_play_start(self, patched_play_start):
        self.qwixx.game_state = QWIXX_STATE_START
        self.qwixx.play(4)
        patched_play_start.assert_called_once_with(4)

    @patch.object(Qwixx, 'play_option')
    def test_play_option_(self, patched_play_option):
        self.qwixx.game_state = QWIXX_STATE_OPTION
        self.qwixx.play(OPTION_PLAY)
        patched_play_option.assert_called_once_with(OPTION_PLAY)

    @parameterized.expand([
        (OPTION_PLAY, 0, 0, QWIXX_STATE_PLAY,),
        (OPTION_PASS, 0, 1, QWIXX_STATE_OPTION,),
        (OPTION_PASS, 3, 0, QWIXX_STATE_OPTION,),
    ])
    def test_play_option_play(
        self,
        selected_option,
        current_player,
        expected_current_player,
        expected_game_state,
    ):
        self.qwixx.play_start(4)
        self.qwixx.current_player = current_player
        self.qwixx.play_option(selected_option)
        self.assertEqual(
            self.qwixx.game_state,
            expected_game_state,
        )
        self.assertEqual(
            self.qwixx.current_player,
            expected_current_player,
        )

    def test_play_option_pass_with_penalty(self):
        self.qwixx.play_start(4)
        self.qwixx.turn_color = QWIXX_TURN_COLOR
        self.qwixx.play_option(OPTION_PASS)
        self.assertEqual(
            self.qwixx.score_pad[0].penalty,
            1,
        )
        self.assertTrue(self.qwixx.is_playing)

    def test_play_option_pass_with_last_penalty(self):
        self.qwixx.play_start(4)
        self.qwixx.turn_color = QWIXX_TURN_COLOR
        self.qwixx.score_pad[0].penalty = 3
        self.qwixx.play_option(OPTION_PASS)
        self.assertEqual(
            self.qwixx.score_pad[0].penalty,
            4,
        )
        self.assertFalse(self.qwixx.is_playing)

    def test_play_option_pass_without_penalty(self):
        self.qwixx.play_start(4)
        self.qwixx.turn_color = QWIXX_TURN_WHITE
        self.qwixx.play_option(OPTION_PASS)
        self.assertEqual(
            self.qwixx.score_pad[0].penalty,
            0,
        )

    def test_play_option_exception(self):
        self.assertEqual(
            self.qwixx.play_option(3),
            'Invalid Option',
        )

    @patch.object(Qwixx, 'play_turn')
    def test_play_play(self, mock_play_turn):
        self.qwixx.play_start(4)
        self.qwixx.game_state = QWIXX_STATE_PLAY
        self.qwixx.play(1)
        mock_play_turn.assert_called_once_with(1)

    @parameterized.expand([
        (QWIXX_TURN_WHITE, 1, '',),
        (QWIXX_TURN_COLOR, 1, 1,),
    ])
    @patch.object(Qwixx, 'mark_with_color')
    @patch.object(Qwixx, 'mark_with_white')
    def test_play_play_turn(
        self,
        turn_color,
        dice1,
        dice2,
        patched_mark_with_white,
        patched_mark_with_color,
    ):
        self.qwixx.turn_color = turn_color
        self.qwixx.play_turn(dice1, dice2)
        if self.qwixx.turn_color == QWIXX_TURN_WHITE:
            patched_mark_with_white.assert_called_once_with(dice1)
        else:
            patched_mark_with_color.assert_called_once_with(dice1, dice2)

    @patch.object(SetDices, 'get_value_of_die', return_value=3)
    def test_mark_with_white(self, mock_get_value_of_die):
        self.qwixx.play_start(4)
        self.qwixx.mark_with_white(1)
        self.assertEqual(self.qwixx.score_pad[0].rows['red'].marks, [6])

    @patch.object(SetDices, 'get_value_of_die', return_value=2)
    def test_mark_with_color(self, mock_get_value_of_die):
        self.qwixx.play_start(4)
        self.qwixx.mark_with_color(1, 1)
        self.assertEqual(self.qwixx.score_pad[0].rows['red'].marks, [4])

    def test_mark_with_color_error_not_can_mark(self):
        self.qwixx.score_pad = [ScorePad()]
        msg = 'You cannot mark that row, the number must be on the right of the last mark!'
        self.qwixx.score_pad[0].rows['red'].marks.append(10)
        self.assertEqual(self.qwixx.mark_with_color(1, 1), msg)

    def test_mark_with_color_error_row_is_locked(self):
        self.qwixx.score_pad = [ScorePad()]
        msg = 'It cannot be marked because the row is locked!'
        row = Row('blue')
        row.blocked_rows.append('blue')
        self.assertEqual(self.qwixx.mark_with_color(1, 3), msg)

    @patch.object(Qwixx, 'mark_with_white')
    def test_play_play_color(self, patched_mark_with_white):
        self.qwixx.play_start(4)
        self.qwixx.turn_color = QWIXX_TURN_WHITE
        self.qwixx.play_turn('red')
        patched_mark_with_white.assert_called_once_with('red')

    @parameterized.expand([
        (0, 0, QWIXX_TURN_WHITE, QWIXX_TURN_WHITE, QWIXX_TURN_WHITE,),
        (1, 0, QWIXX_TURN_WHITE, QWIXX_TURN_WHITE, QWIXX_TURN_WHITE,),
        (2, 0, QWIXX_TURN_WHITE, QWIXX_TURN_WHITE, QWIXX_TURN_WHITE,),
        (3, 0, QWIXX_TURN_WHITE, QWIXX_TURN_WHITE, QWIXX_TURN_COLOR,),
        (0, 0, QWIXX_TURN_COLOR, QWIXX_TURN_WHITE, QWIXX_TURN_WHITE,),
        (1, 1, QWIXX_TURN_WHITE, QWIXX_TURN_COLOR, QWIXX_TURN_WHITE,),
        (2, 1, QWIXX_TURN_WHITE, QWIXX_TURN_WHITE, QWIXX_TURN_WHITE,),
        (3, 1, QWIXX_TURN_WHITE, QWIXX_TURN_WHITE, QWIXX_TURN_WHITE,),
        (0, 1, QWIXX_TURN_WHITE, QWIXX_TURN_WHITE, QWIXX_TURN_COLOR,),
        (1, 1, QWIXX_TURN_COLOR, QWIXX_TURN_WHITE, QWIXX_TURN_WHITE,),
    ])
    @patch.object(SetDices, 'roll_dices')
    def test_set_next_player(
        self,
        current_player,
        current_color_player,
        turn_color,
        previous_turn_color,
        expected_next_turn_color,
        mock_roll_dice
    ):
        self.qwixx.play_start(4)
        self.qwixx.game_state = QWIXX_STATE_PLAY
        self.qwixx.current_player = current_player
        self.qwixx.previous_turn_color = previous_turn_color
        self.qwixx.current_color_player = current_color_player
        self.qwixx.turn_color = turn_color
        self.qwixx.set_next_player()
        self.assertEqual(
            self.qwixx.game_state,
            QWIXX_STATE_OPTION,
        )
        self.assertEqual(
            self.qwixx.current_player,
            (current_player + 1) % 4,
        )
        self.assertEqual(
            self.qwixx.turn_color,
            expected_next_turn_color,
        )
        mock_roll_dice.assert_called()

    @parameterized.expand([
        (['blue', 'red'], False),
        (['blue', 'red', 'yellow'], False),
        (['blue'], True),
        ([], True),
    ])
    def test_you_cant_play(self, blocked_row, expected):
        row = Row
        row.blocked_rows.clear()
        row.blocked_rows.extend(blocked_row)
        self.qwixx.you_can_play
        self.assertEqual(self.qwixx.is_playing, expected)

    def _get_id_of_players(self, players):
        return [player.id_player for player in players]

    @patch.object(ScorePad, 'calculate_score', side_effect=[50, 90, 100])
    def test_get_winners(self, mock_calculate_score):
        initial_id_player = [0, 1, 2]
        final_id_player = [2, 1, 0]
        n_players = 3
        self.qwixx.play_start(n_players)
        ranking_players = self.qwixx.get_winners()

        self.assertTrue(all(isinstance(player, ScorePad) for player in ranking_players))
        self.assertEqual(mock_calculate_score.call_count, n_players)
        self.assertEqual(self._get_id_of_players(self.qwixx.score_pad), initial_id_player)
        self.assertEqual(self._get_id_of_players(ranking_players), final_id_player)

    @patch.object(ScorePad, 'calculate_score', return_value=100)
    @patch.object(Qwixx, 'get_winners')
    def test_show_winners(self, mock_get_winners, mock_calculate_score):
        self.qwixx.play_start(1)
        mock_get_winners.return_value = [self.qwixx.score_pad[0]]
        result = self.qwixx.show_winners()
        self.assertEqual(
            result,
            'WINNERS TABLE \n'
            "------------------------------------------------------------\n"
            'PLAYER 0'.ljust(8) + ' | ' + 'SCORE 100\n'.rjust(10) +
            "------------------------------------------------------------"
        )
        self.assertEqual(mock_calculate_score.call_count, 1)
        self.assertEqual(mock_get_winners.call_count, 1)
