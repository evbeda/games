import unittest
from unittest.mock import patch
from parameterized import parameterized
from ..tile_bag import TileBag
from ..game import Game
from ..player import Player
from ..board import Board


class TestGame(unittest.TestCase):

    def setUp(self):
        self.player_names = ["Pedro", "Juana", "Mia"]
        self.game = Game(self.player_names)

    def test_game_attributes(self):
        self.assertEqual(type(self.game.tile_bag), type(TileBag()))
        self.assertEqual(len(self.game.players), 3)
        self.assertEqual(self.game.current_turn, 0)

    def test_create_players(self):
        with patch('rummy_and_burakko.game.Player') as player_patched:
            self.game.create_players(self.player_names)

        self.assertEqual(len(self.game.players), 3)
        player_patched.assert_called()

    @parameterized.expand([
        # Players, Current, Next
        (3, 0, 1),
        (4, 3, 0),
        (3, 2, 0),
    ])
    def test_next_turn(self, players, current_turn, next_turn):
        self.game.players = [Player("Pedro")] * players
        self.game.current_turn = current_turn

        self.game.next_turn()

        self.assertEqual(self.game.current_turn, next_turn)

    @patch.object(Player, "temporary_hand")
    @patch.object(Board, "temp_board")
    @patch.object(Player, "change_state")
    def test_next_turn_calls(
        self,
        m_change_state,
        m_temporary_board,
        m_temporary_hand,
    ):
        # data
        self.game.players = [Player("Pedro")]
        # process
        self.game.next_turn()
        # assert
        m_change_state.assert_called_once_with()
        m_temporary_board.assert_called_once_with()
        m_temporary_hand.assert_called_once_with()

    @patch.object(TileBag, "assign_tiles")
    def test_call_assign_tiles(self, mock):
        self.game.distribute_tiles()
        self.assertEqual(mock.call_count, 1)

    @patch('random.shuffle')
    def test_start_order(self, mock):
        # data
        first_order = self.game.players.copy()
        # process
        self.game.random_order()
        mock.assert_called_once_with(first_order)

    board = (
        "1: L[ 0:r5 1:b5 2:y5 ]\n"
        "2: L[ 0:r3 1:b3 2:y3 3:w3 ]\n"
        "3: S[ 0:r3 1:r4 2:r5 3:r6 ]"
    )
    hand = "player_1> 0:r11 1:y2 2:y13 3:b5"
    reused = '5:r3   6:r4   7:r5'

    @patch.object(Board, "get_reused_tiles", return_value=reused)
    @patch.object(Player, "get_hand", return_value=hand)
    @patch.object(Board, "get_board", return_value=board)
    def test_show_game(self, m_get_board, m_get_hand, m_reused):
        # data
        expected = (
            "Mesa\n" +
            m_get_board.return_value +
            "\n\nMano\n" +
            m_get_hand.return_value +
            "\n\nFichas sueltas\n" +
            m_reused.return_value
        )
        # process
        self.game.create_players(["player_1", "player_2"])
        self.game.distribute_tiles()
        result = self.game.show_game()
        # assert
        self.assertEqual(result, expected)
        m_get_board.assert_called_once()
        m_get_hand.assert_called_once()
        m_reused.assert_called_once()

    @patch.object(Player, "valid_hand", return_value=True)
    @patch.object(Board, "valid_sets", return_value=False)
    @patch.object(Game, "validate_first_move", return_value=True)
    def test_valid_turn(
        self,
        mock_first_move,
        mock_valid_sets,
        mock_valid_hand
    ):
        # data
        expected = False
        # process
        self.game.create_players(["player_1", "player_2"])
        self.game.distribute_tiles()
        self.game.board.current_play_score = 30
        result = self.game.valid_turn()
        # assert
        self.assertEqual(mock_valid_hand.call_count, 1)
        self.assertEqual(mock_valid_sets.call_count, 1)
        self.assertEqual(result, expected)

    # @patch.object(Player, "valid_hand", return_value=True)
    # @patch.object(Board, "valid_sets", return_value=True)
    # @patch.object(Game, "validate_first_move", return_value=True)
    # def test_valid_turn_first_move(
    #     self, mock_valid_hand, mock_valid_sets, mock_player
    # ):
    #     # data
    #     expected = False
    #     # process
    #     self.game.create_players(["player_1", "player_2"])
    #     self.game.distribute_tiles()
    #     result = self.game.valid_turn()
    #     # assert
    #     self.assertEqual(mock_valid_hand.call_count, 1)
    #     self.assertEqual(mock_valid_sets.call_count, 1)
    #     self.assertEqual(result, expected)

    @parameterized.expand([
        # (option, call_count)
        (1, (1, 0, 0)),
        (2, (0, 1, 0)),
        (3, (0, 0, 1)),
    ])
    @patch.object(Board, "give_one_tile_from_board")
    @patch.object(Game, "select_put_a_tile")
    @patch.object(Game, "put_new_set")
    def test_make_play_calls(
        self,
        option,
        call_count,
        mock_new_set,
        mock_put_a_tile,
        mock_take_tile,
    ):
        # data
        self.game.players = [Player("test_1")]
        arg_1 = 10
        arg_2 = 55
        # process
        self.game.make_play(option, [arg_1, arg_2])
        # assert
        self.assertEqual(mock_new_set.call_count, call_count[0])
        self.assertEqual(mock_put_a_tile.call_count, call_count[1])
        self.assertEqual(mock_take_tile.call_count, call_count[2])

    @patch.object(Board, "give_one_tile_from_board")
    def test_make_play_arguments(self, mock):
        # data
        self.game.players = [Player("test_1")]
        option = 3
        set_id = 1
        index = 3
        # process
        self.game.make_play(option, [set_id, index])
        # assert
        mock.assert_called_once_with(set_id, index)

    @parameterized.expand([
        # (return_value, validate.call_count, give_one_tile.call_count)
        (True, 1, 0),
        (False, 0, 1),
    ])
    @patch.object(TileBag, "give_one_tile")
    @patch.object(Player, "validate_turn")
    @patch.object(Board, "validate_turn")
    @patch.object(Player, "change_state")
    @patch.object(Player, "change_first_move")
    def test_end_turn(
        self,
        rv,
        call_count_1,
        call_count_2,
        mock_player_change_first_move,
        mock_player_change_state,
        mock_board,
        mock_player_validate,
        mock_bag,
    ):
        # data
        self.game.create_players(["player_1", "player_2"])
        self.game.distribute_tiles()
        # process
        with patch.object(Game, "valid_turn", return_value=rv) as mock_v_t:
            self.game.end_turn()
            # assert
            self.assertEqual(mock_v_t.call_count, 1)
            self.assertEqual(mock_player_change_state.call_count, 1)
            self.assertEqual(mock_board.call_count, call_count_1)
            self.assertEqual(mock_player_validate.call_count, call_count_1)
            self.assertEqual(
                mock_player_change_first_move.call_count,
                call_count_1,
            )
            self.assertEqual(mock_bag.call_count, call_count_2)
            self.assertEqual(self.game.board.current_play_score, 0)

    @patch.object(Player, 'get_lenght', return_value=5)
    def test_quantity_of_tiles(self, mock_player):
        # data
        self.game.distribute_tiles()
        # process
        result = self.game.quantity_of_tiles()
        # assert
        mock_player.assert_called_once_with()
        self.assertEqual(result, mock_player.return_value)

    @parameterized.expand([
        # (indexes, call_count_1, call_count_2, expected)
        ([14, 5, 1, 7], 3, 1, [6, 1, 2, 3]),
        ([0, 12, 13, 14], 2, 2, [1, 2, 6, 7]),
        ([13, 14, 15, 16], 0, 4, [6, 7, 8, 9]),
        ([0, 5, 10, 12], 4, 0, [1, 2, 3, 4]),
    ])
    @patch.object(
        Board,
        'get_a_reused_tile',
        side_effect=[6, 7, 8, 9, 10]
    )
    @patch.object(
        Player,
        'get_a_tile',
        side_effect=[1, 2, 3, 4, 5]
    )
    def test_make_tile_array(
        self,
        indexes,
        cc_1,
        cc_2,
        expected,
        mock_player,
        mock_board,
    ):
        # process
        self.game.distribute_tiles()
        self.game.next_turn()
        result = self.game.make_tile_array(indexes)
        # assert
        self.assertEqual(mock_player.call_count, cc_1)
        self.assertEqual(mock_board.call_count, cc_2)
        self.assertEqual(result, expected)

    @parameterized.expand([
        # (indexes, call_count_1, call_count_2, expected)
        ([14, 5, 1, 7], 3, 1),
        ([0, 12, 13, 14], 2, 2),
        ([13, 14, 15, 16], 0, 4),
        ([0, 5, 10, 12], 4, 0),
    ])
    @patch.object(Board, 'remove_reused_tile')
    @patch.object(Player, 'remove_tile')
    def test_clean_calls(self, indexes, cc_1, cc_2, mock_player, mock_board):
        # process
        self.game.distribute_tiles()
        self.game.next_turn()
        self.game.clean(indexes)
        # assert
        self.assertEqual(mock_player.call_count, cc_1)
        self.assertEqual(mock_board.call_count, cc_2)

    @parameterized.expand([
        # (indexes, expected_temp_hand, expected_reused_tiles)
        ([6, 1, 3, 2], [0, 4], [5, 7, 8, 9]),
        ([0, 7, 8, 9], [1, 2, 3, 4], [5, 6]),
        ([0, 4, 5, 9], [1, 2, 3], [6, 7, 8]),
    ])
    def test_clean_result(self, indexes, expected_1, expected_2):
        # data
        player = self.game.players[self.game.current_turn]
        player.temp_hand = list(range(5))
        self.game.board.reused_tiles = list(range(5, 10))
        # process
        self.game.clean(indexes)
        # assert
        self.assertEqual(player.temp_hand, expected_1)
        self.assertEqual(self.game.board.reused_tiles, expected_2)

    @patch.object(Board, 'place_new_set')
    @patch.object(Game, 'clean')
    @patch.object(Game, 'make_tile_array', return_value=[1, 2, 3])
    def test_put_new_set_calls(self, m_make, m_clean, m_place):
        # data
        indexes = (1, 2, 3, 4, 5)
        # proces
        self.game.put_new_set(*indexes)
        # assert
        m_make.assert_called_once_with(indexes)
        m_clean.assert_called_once_with(indexes)
        m_place.assert_called_once_with(m_make.return_value, True)

    @parameterized.expand([
        (True, 30, True),
        (False, 30, True),
        (True, 29, False),
        (False, 30, True),
    ])
    def test_validate_first_turn(self, is_first_play, score, expected):
        self.game.current_turn = 0
        self.game.players[0].first_move = is_first_play
        self.game.board.current_play_score = score
        self.assertEqual(self.game.validate_first_move(), expected)

    @patch.object(Board, 'put_a_tile')
    @patch.object(Game, 'clean')
    @patch.object(Game, 'make_tile_array', return_value=[1])
    def test_select_put_a_tile_calls(self, m_make, m_clean, m_put):
        # data
        my_tile = 3
        set_id = 1
        index = 3
        args = (my_tile, set_id, index)
        # process
        self.game.select_put_a_tile(*args)
        # assert
        m_make.assert_called_once_with([my_tile])
        m_clean.assert_called_once_with([my_tile])
        m_put.assert_called_once_with(*m_make.return_value, set_id, index)

    @patch.object(Player, 'has_tiles')
    def test_check_is_game_alive(self, m_has_tiles):
        self.game.check_is_game_alive()
        m_has_tiles.assert_called_once_with()

    def test_get_current_player(self):
        self.game.current_turn = 0
        player = self.game.get_current_player()
        self.assertEqual(player.name, 'Pedro')

    @parameterized.expand([
        # (option, call_count)
        (1, (1, 0, 0)),
        (2, (0, 1, 0)),
        (3, (0, 0, 1)),
    ])
    @patch.object(Board, 'valid_set_index')
    @patch.object(Game, 'valid_input_put_a_tile')
    @patch.object(Game, 'valid_tiles')
    def test_move_verification_calls(
        self,
        option,
        call_count,
        mock_tiles,
        mock_put_a_tile,
        mock_set,
    ):
        moves = (1, 2, 3)
        self.game.move_verification(option, moves)
        self.assertEqual(mock_tiles.call_count, call_count[0])
        self.assertEqual(mock_put_a_tile.call_count, call_count[1])
        self.assertEqual(mock_set.call_count, call_count[2])

    @patch.object(Board, 'valid_set_index', return_value='Error_2')
    @patch.object(Game, 'valid_tiles', return_value='Error_1\n')
    def test_input_put_a_tile_calls(self, mock_tiles, mock_set):
        index_hand = 3
        set_id = 1
        set_index = 4
        expected = 'Error_1\n' + 'Error_2'
        result = self.game.valid_input_put_a_tile(index_hand, set_id, set_index)
        self.assertEqual(result, expected)
        mock_tiles.assert_called_once_with(index_hand)
        mock_set.assert_called_once_with(set_id, set_index - 1)

    @patch.object(Player, 'valid_tiles_in_hand')
    def test_valid_tiles(self, mock_player):
        self.game.board.reused_tiles = [1, 2, 3, 4]
        size = len(self.game.board.reused_tiles)
        moves = (1, 2, 3)
        self.game.valid_tiles(*moves)
        mock_player.assert_called_once_with(size, moves)
