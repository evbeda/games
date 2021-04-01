import unittest
from unittest.mock import patch
from parameterized import parameterized
from ..scrabble import Scrabble
from ..game import Game
# from ..player import Player
# from ..tile import Tile


class TestScrabble(unittest.TestCase):

    def setUp(self):
        self.scrabble = Scrabble()

    @patch.object(Game, 'print_scores')
    @patch.object(Game, 'print_board')
    def test_board(self, print_board_patched, print_scores_patched):
        self.scrabble.game = Game(["Pedro"])
        self.scrabble.board
        print_board_patched.assert_called()
        print_scores_patched.assert_called()

    @parameterized.expand([
        ('create_game', 1),
        ('play_word', 4),
        ('ask_challenge', 1),
        ('in_challenge', 1),
        ('select_action', 1),
    ])
    def test_input_arg_count(self, state, args):
        # Create game: Number of players
        self.scrabble.game_state = state
        self.assertEqual(self.scrabble.input_args, args)

    def test_input_arg_count_for_input_players(self):
        # Players names: one for each player
        self.scrabble.game_state = 'input_players'
        self.scrabble.input_player_args = 3
        self.assertEqual(self.scrabble.input_args, 3)

    def test_play_create_game(self):
        self.scrabble.play(3)
        self.assertEqual(self.scrabble.input_player_args, 3)
        self.assertEqual(self.scrabble.game_state, 'input_players')

    def test_play_create_game_invalid(self):
        player_count = 5
        resp = self.scrabble.play(player_count)
        self.assertEqual(self.scrabble.input_player_args, 0)
        self.assertEqual(resp, 'The number of players is wrong, please enter the number again')
        self.assertEqual(self.scrabble.game_state, 'create_game')

    def test_play_setup_players(self):
        player_names = ["Pedro", "Ricardo"]
        self.scrabble.game_state = 'input_players'
        self.scrabble.input_player_args = len(player_names)
        self.scrabble.play(player_names)
        self.assertIsNotNone(self.scrabble.game)
        self.assertEqual(self.scrabble.game_state, 'select_action')

    @patch.object(Game, 'change_player_tiles')
    def test_play_change_tiles(self, change_tiles_patched):
        player_names = ["Pedro", "Ricardo"]
        self.scrabble.game = Game(player_names)
        self.scrabble.game_state = 'change_letters'
        tiles = ('a', 'b', 'c')
        self.scrabble.change_letters = len(tiles)
        self.scrabble.play(*tiles)
        self.assertEqual(self.scrabble.game_state, 'changed_letters')
        change_tiles_patched.assert_called_with(tiles)

    @patch.object(Game, 'place_word')
    def test_play_add_word(self, play_word_patched):
        player_names = ["Pedro", "Ricardo"]
        self.scrabble.game = Game(player_names)
        self.scrabble.game_state = 'play_word'
        self.scrabble.play('5', '7', 'h', 'word')
        self.assertEqual(self.scrabble.game_state, 'ask_challenge')
        play_word_patched.assert_called_with(7, 5, True, 'word')

    def test_play_action_pass(self):
        self.scrabble.game_state = 'select_action'
        self.scrabble.play('pass')
        self.assertEqual(self.scrabble.game_state, 'skip_turn')

    def test_play_action_play_word(self):
        self.scrabble.game_state = 'select_action'
        self.scrabble.play('play')
        self.assertEqual(self.scrabble.game_state, 'play_word')

    def test_play_action_change_letters(self):
        self.scrabble.game_state = 'select_action'
        self.scrabble.play('4')
        self.assertEqual(self.scrabble.change_letters, 4)
        self.assertEqual(self.scrabble.game_state, 'change_letters')

    def test_play_challenge(self):
        player_names = ["Pedro", "Ricardo"]
        self.scrabble.game = Game(player_names)
        self.scrabble.game_state = 'ask_challenge'
        self.scrabble.play(1)
        self.assertEqual(self.scrabble.challenger_player, 1)
        self.assertEqual(self.scrabble.game_state, 'in_challenge')

    def test_play_challenge_skip(self):
        player_names = ["Pedro", "Ricardo"]
        self.scrabble.game = Game(player_names)
        self.scrabble.game_state = 'ask_challenge'
        self.scrabble.play(99)
        self.assertEqual(self.scrabble.game_state, 'change_turn')

    @parameterized.expand([
        ('yes', True),
        ('no', False),
    ])
    @patch.object(Game, 'resolve_challenge')
    def test_play_challenge_result(
        self, user_input, expected_param, resolve_challenge_patched
    ):
        player_names = ["Pedro", "Ricardo"]
        self.scrabble.game = Game(player_names)
        self.scrabble.game_state = 'in_challenge'
        self.scrabble.challenger_player = 1
        self.scrabble.play(user_input)
        self.assertEqual(self.scrabble.game_state, 'change_turn')
        resolve_challenge_patched.assert_called_with(expected_param, 1)

    @parameterized.expand([
        ('create_game', True),
        ('input_players', False),
        ('play_word', False),
        ('change_letters', False),
        ('ask_challenge', True),
        ('in_challenge', False),
        ('select_action', False),
    ])
    def test_input_are_ints(self, state, expected):
        self.scrabble.game_state = state
        self.assertEqual(self.scrabble.input_are_ints, expected)

    @parameterized.expand([
        ('create_game', 'Enter number of players\n'),
        ('input_players', 'Enter player names\n'),
        ('change_letters', 'Which letters do you want to change?\n'),
        ('play_word', 'Enter all in a line:\n'
            '- start position of word (nº of row and nº of column)\n'
            '- direction(h --> horizontal or v --> vertical)\n'
            '- the word\n'),
        ('ask_challenge', 'Select the challenger player:\n'),
        ('in_challenge', 'Look up new words in a dictionary. '
            'Are they correct?\n'),
        ('select_action', 'Enter "play" to play a new word, '
            '"pass" to end your turn or '
            'any number to change that amount of tiles\n'),
    ])
    def test_next_turn_state_query(self, state, expected):
        self.scrabble.game_state = state
        text = self.scrabble.next_turn_state_query()
        self.assertEqual(text, expected)

    @patch.object(Game, 'ask_challenge_show_players')
    def test_next_turn_ask_challenge(self, mock_ask_challenge_show_players):
        player_names = ["Pedro", "Ricardo"]
        self.scrabble.game = Game(player_names)
        self.scrabble.game_state = 'ask_challenge'
        self.scrabble.next_turn()
        mock_ask_challenge_show_players.assert_called()

    @patch.object(Game, 'get_current_player_hand')
    def test_next_turn_show_hand(self, get_current_player_hand_patched):
        player_names = ["Pedro", "Ricardo"]
        self.scrabble.game = Game(player_names)
        self.scrabble.next_turn_show_hand()
        get_current_player_hand_patched.assert_called()

    @patch.object(Scrabble, 'next_turn_state_query')
    @patch.object(Scrabble, 'next_turn_show_hand')
    @patch.object(Game, 'change_turn')
    def test_next_turn_changed_letters(
        self, change_turn_patched, show_hand_patched, state_query_patched
    ):
        player_names = ["Pedro", "Ricardo"]
        self.scrabble.game = Game(player_names)
        self.scrabble.game_state = 'changed_letters'
        self.scrabble.next_turn()
        self.assertEqual(show_hand_patched.call_count, 2)
        state_query_patched.assert_called()
        change_turn_patched.assert_called()

    @patch.object(Scrabble, 'next_turn_state_query')
    @patch.object(Scrabble, 'next_turn_show_hand')
    @patch.object(Game, 'change_turn')
    def test_next_turn_change_turn(
        self, change_turn_patched, show_hand_patched, state_query_patched
    ):
        player_names = ["Pedro", "Ricardo"]
        self.scrabble.game = Game(player_names)
        self.scrabble.game_state = 'change_turn'
        self.scrabble.next_turn()
        self.assertEqual(show_hand_patched.call_count, 1)
        state_query_patched.assert_called()
        change_turn_patched.assert_called()

    @patch.object(Scrabble, 'next_turn_state_query')
    @patch.object(Scrabble, 'next_turn_show_hand')
    @patch.object(Game, 'change_turn')
    def test_next_turn_change_turn_on_play(
        self, change_turn_patched, show_hand_patched, state_query_patched
    ):
        player_names = ["Pedro", "Ricardo"]
        self.scrabble.game = Game(player_names)
        self.scrabble.game_state = 'play_word'
        self.scrabble.next_turn()
        self.assertEqual(show_hand_patched.call_count, 1)
        state_query_patched.assert_called()
        change_turn_patched.assert_not_called()

    @patch.object(Scrabble, 'next_turn_state_query')
    @patch.object(Scrabble, 'next_turn_show_hand')
    @patch.object(Game, 'skip_turn')
    def test_next_turn_skip_turn(
        self, skip_turn_patched, show_hand_patched, state_query_patched
    ):
        player_names = ["Pedro", "Ricardo"]
        self.scrabble.game = Game(player_names)
        self.scrabble.game_state = 'skip_turn'
        self.scrabble.next_turn()
        self.assertEqual(show_hand_patched.call_count, 1)
        state_query_patched.assert_called()
        skip_turn_patched.assert_called()

    @patch.object(Game, 'get_game_results')
    def test_next_turn_game_over(self, get_game_results_patched):
        player_names = ["Pedro", "Ricardo"]
        self.scrabble.game = Game(player_names)
        self.scrabble.game.is_playing = False
        self.scrabble.next_turn()
        get_game_results_patched.assert_called()

    def test_is_playing(self):
        player_names = ["Pedro", "Ricardo"]
        self.scrabble.game = Game(player_names)
        self.assertTrue(self.scrabble.is_playing)

    def test_is_playing_no_game(self):
        self.assertTrue(self.scrabble.is_playing)

    def test_is_not_playing(self):
        player_names = ["Pedro", "Ricardo"]
        self.scrabble.game = Game(player_names)
        self.scrabble.game.is_playing = False
        self.assertFalse(self.scrabble.is_playing)

    @parameterized.expand([
        ('7', '7', 'h', 'hola', True),
        ('7', '7', 'v', 'hola', True),
        ('7', '7', 'f', 'hola', False),
    ])
    @patch.object(Game, 'place_word')
    def test_play_play_word(self, row, col, direction, word, expected, mock_place_word):
        player_names = ["Pedro", "Ricardo"]
        self.scrabble.game = Game(player_names)
        self.scrabble.play_play_word(col, row, direction, word)
        if expected:
            mock_place_word.assert_called()
        else:
            mock_place_word.assert_not_called()

    @parameterized.expand([
        (True, 'ask_challenge', ''),
        (False, 'change_turn', 'Invalid word position'),
    ])
    def test_play_play_word_place_result(self, place_word_result, expected_state, expected_msg):
        player_names = ["Pedro", "Ricardo"]
        self.scrabble.game = Game(player_names)
        self.scrabble.game_state = 'play_word'
        with patch.object(Game, 'place_word', return_value=place_word_result):
            msg = self.scrabble.play('5', '7', 'h', 'word')
            self.assertEqual(self.scrabble.game_state, expected_state)
            self.assertEqual(msg, expected_msg)
