import unittest
from unittest.mock import patch
from parameterized import parameterized
from ..rummy_and_burakko import RummyAndBurakko
from ..game import Game
from ..board import Board


class TestRummyAndBurakko(unittest.TestCase):
    def setUp(self):
        self.rummy = RummyAndBurakko()

    @parameterized.expand([
        # (game_state, expected)
        ('start_game', 1),
        ('new_set_tiles', 0),
        ('put_a_tile', 3),
    ])
    def test_input_args_property(self, game_state, expected):
        self.rummy.game_state = game_state
        result = self.rummy.input_args
        self.assertEqual(result, expected)

    @patch.object(Game, "show_game", return_value="test")
    def test_board(self, mock):
        # data
        players = ["test_1", "test_2", "test_3"]
        # process
        result = self.rummy.board
        message = '\n\n*************************************************************\n'
        self.assertEqual(result, message + "Starting...")

        self.rummy.game = Game(players)
        result = self.rummy.board
        mock.assert_called_once_with()
        self.assertEqual(mock.return_value, "test")

    @parameterized.expand([
        # (input_players, assign_input, game_state, input_are_ints)
        (0, 0, 'start_game', True),
        (2, 2, 'players_input', False),
        (4, 4, 'players_input', False),
        (5, 0, 'start_game', True),
    ])
    def test_play_start_game(self, input_players, res_1, res_2, are_ints):
        self.rummy.play_start_game(input_players)
        self.assertEqual(self.rummy.input_player_args, res_1)
        self.assertEqual(self.rummy.game_state, res_2)
        self.assertEqual(self.rummy.input_are_ints, are_ints)

    @patch.object(Game, "next_turn")
    @patch.object(Game, "distribute_tiles")
    @patch.object(Game, "random_order")
    @patch.object(Game, "create_players")
    def test_play_players_input(
        self,
        m_init,
        m_order,
        m_distribute,
        m_next_turn,
    ):
        # data
        players = ["test_1", "test_2", "test_3"]
        # process
        self.rummy.play_players_input(*players)
        # assert
        m_init.assert_called_once_with(tuple(players))
        m_order.assert_called_once_with()
        m_distribute.assert_called_once_with()
        m_next_turn.assert_called_once_with()
        self.assertTrue(self.rummy.input_are_ints)

    @parameterized.expand([
        # (game_state, expected)
        ('start_game', '\nEnter number of players'),
        ('new_set_q', '\nHow many tiles will have the set?'),
        # ('end_turn', '\nTurn Ended'),
    ])
    @patch.object(Game, 'check_is_game_alive', return_value=True)
    def test_next_turn_message(self, game_state, expected, mock_alive):
        players = ["player_1", "player_2", 'player_3']
        self.rummy.game = Game(players)
        self.rummy.game_state = game_state
        result = self.rummy.next_turn()
        self.assertEqual(result, expected)

    @patch.object(Game, 'get_current_player', return_value='player_2')
    @patch.object(Game, 'check_is_game_alive', return_value=False)
    def test_next_turn_message_end_game(self, mock_alive, mock_player):
        game_state = 'end_turn'
        expected = '\nWE HAVE A WINNER! Congratulations {}'.format('player_2')
        players = ["player_1", "player_2", "player_3"]
        self.rummy.game = Game(players)
        self.rummy.game_state = game_state
        result = self.rummy.next_turn()
        self.assertEqual(result, expected)

    @parameterized.expand([
        # (option, game_state)
        (0, 'select_option'),
        (1, 'new_set_q'),
        (4, 'end_turn'),
        (5, 'select_option'),
    ])
    def test_play_select_option(self, option, game_state):
        # data
        self.rummy.game_state = 'select_option'
        # process
        self.rummy.play_select_option(option)
        # assert
        self.assertEqual(self.rummy.game_state, game_state)

    @parameterized.expand([
        # (quantity, call_count, input_q_tiles)
        (2, 'new_set_q', 5),
        (3, 'new_set_tiles', 3),
        (4, 'new_set_tiles', 4),
        (6, 'new_set_q', 5),
        (14, 'new_set_q', 5),
    ])
    @patch.object(Game, 'quantity_of_tiles', return_value=5)
    def test_play_new_set_q(
        self,
        quantity,
        state,
        q,
        mock,
    ):
        # data
        players = ["player_1", "player_2", 'player_3']
        self.rummy.game = Game(players)

        old_q_tiles = 5
        self.rummy.input_q_tiles = old_q_tiles
        self.rummy.game_state = 'new_set_q'
        # process
        self.rummy.game.distribute_tiles()
        self.rummy.play_new_set_q(quantity)
        # assert
        mock.assert_called_once_with()
        self.assertEqual(self.rummy.game_state, state)
        self.assertEqual(self.rummy.input_q_tiles, q)

    @patch.object(Game, 'show_game')
    @patch.object(Game, 'next_turn')
    @patch.object(Game, 'end_turn')
    @patch.object(Game, 'check_is_game_alive', return_value=True)
    def test_next_turn(self, mock_alive, mock_end, mock_next, mock_show):
        # data
        players = ["player_1", "player_2", 'player_3']
        self.rummy.game = Game(players)

        self.rummy.game_state = 'end_turn'
        # process
        self.rummy.next_turn()
        # assert
        self.assertEqual(self.rummy.game_state, 'select_option')
        mock_end.assert_called_once_with()
        mock_next.assert_called_once_with()
        mock_show.assert_called_once_with()

    @parameterized.expand([
        # (game_state, call_count)
        ('start_game', (1, 0, 0)),
        ('players_input', (0, 1, 0)),
        ('put_a_tile', (0, 0, 1)),
        ('new_set_tiles', (0, 0, 1)),
    ])
    @patch.object(RummyAndBurakko, 'play_input_verification')
    @patch.object(RummyAndBurakko, 'play_players_input')
    @patch.object(RummyAndBurakko, 'play_start_game')
    def test_play(
        self,
        game_state,
        call_count,
        mock_start,
        mock_players,
        mock_verification,
    ):
        args = [1, 2, 3, 4]
        self.rummy.game_state = game_state
        self.rummy.play(*args)

        self.assertEqual(mock_start.call_count, call_count[0])
        self.assertEqual(mock_players.call_count, call_count[1])
        self.assertEqual(mock_verification.call_count, call_count[2])

    @patch.object(Board, 'give_one_tile_from_board')
    def test_play_make_move_confirmed(self, m_give_one):
        players = ["player_1", "player_2", 'player_3']
        self.rummy.game = Game(players)
        confirm = 'y'
        self.rummy.option = 3
        self.rummy.move = (0, 1, 3, 5)
        self.rummy.play_make_move(confirm)
        m_give_one.assert_called_once_with(*self.rummy.move)
        self.assertEqual(self.rummy.game_state, 'select_option')

    def test_play_make_move_not_confirmed(self):
        confirm = 'n'
        expected = 'Discarded movement, select a new one'

        result = self.rummy.play_make_move(confirm)
        self.assertEqual(result, expected)

    @parameterized.expand([
        # (verif_result, game_state, return)
        ('', 'make_move', 'Input is valid'),
        ('Error', 'select_option', 'Error'),
    ])
    def test_play_input_verification(self, result, state, expected):
        players = ["player_1", "player_2", 'player_3']
        self.rummy.game = Game(players)
        self.rummy.option = 1
        data = (0, 1, 3, 5)
        with patch.object(Game, 'move_verification', return_value=result) as mock:
            result = self.rummy.play_input_verification(*data)
            mock.assert_called_once_with(1, data)
            self.assertEqual(result, expected)
            self.assertEqual(self.rummy.game_state, state)
