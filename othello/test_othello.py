import unittest
from parameterized import parameterized

from othello.othello_game import Othello
from othello.scenarios_test import (
    black_12,
    white_12,
    mix_6,
    flip_black,
    final_flip_black,
    flip_row_white,
    final_flip_row_white,
    diagonal_flip,
    final_diagonal_flip,
    board_winner_w,
    board_tie,
    board_tie_empty,
    validate_direction_1,
    validate_direction_2,
    all_poss_moves_board_1,
    all_poss_moves_exp_1,
    none_pos_exp_1,
    black_12_that_will_print,
    white_12_that_will_print,
    play_board_1,
    play_board_b_wins,
    play_board_w_wins,
    play_board_tie,
    put_piece_board,
    all_poss_moves_board_2)
from othello.constants import (
    PLAYER1,
    PLAYER2,
    N,
    NE,
    E,
    SE,
    S,
    SW,
    W,
    NW,
    TIE_MATCH,
    GAME_OVER,
    MOVE_OK,
)


class Test_othello(unittest.TestCase):

    def _convert_scenario_to_matrix(self, scenario):
        players = PLAYER1 + PLAYER2
        matrix = []
        for scenario_line in scenario:
            matrix_line = [
                scenario_letter
                if scenario_letter in players
                else None
                for scenario_letter in scenario_line
            ]
            matrix.append(matrix_line)
        return matrix

    def setUp(self):
        self.game = Othello()

    def test_board_size(self):
        self.assertEqual(len(self.game._board), 8)
        for row in self.game._board:
            self.assertEqual(len(row), 8)

    def test_initial_black_piece_count(self):
        player1_pieces = self.game.get_piece_count(PLAYER1)
        self.assertEqual(2, player1_pieces)

    @parameterized.expand(
        [
            (black_12, 12, PLAYER1),
            (white_12, 12, PLAYER2),
            (mix_6, 6, PLAYER2),
            (mix_6, 6, PLAYER1),
        ]
    )
    def test_initial_white_piece_count(self, board, expected, kind):
        # replace board to see diferents situacions
        self.game._board = self._convert_scenario_to_matrix(board)
        pieces = self.game.get_piece_count(kind)
        self.assertEqual(expected, pieces)

    def test_initial_player(self):
        self.assertTrue(self.game.player_turn == PLAYER1)

    @parameterized.expand(
        [
            (1, PLAYER2),
            (3, PLAYER2),
            (4, PLAYER1),
            (7, PLAYER2),
        ]
    )
    def test_current_turn(self, it, expected):
        for _ in range(it):
            self.game.change_player()
        self.assertEqual(expected, self.game.player_turn)

    @parameterized.expand(
        [
            (1, PLAYER1),
            (3, PLAYER1),
            (4, PLAYER2),
            (7, PLAYER1),
        ]
    )
    def test_opposite_piece(self, it, expected):
        for _ in range(it):
            self.game.change_player()
        self.assertEqual(expected, self.game.get_opposite_piece())

    @parameterized.expand(
        # initial_board , coordinates , index_player, final_board
        [
            (flip_black, [(0, 0)], 1, final_flip_black),
            (flip_row_white, [(5, 0), (5, 2), (5, 4)], 0,
                final_flip_row_white),
            (diagonal_flip, [(0, 0), (1, 1), (2, 2)], 1,
                final_diagonal_flip)
        ]
    )
    def test_flip_pieces(self, initial_board, cordinates, index, final_board):
        self.game._board = self._convert_scenario_to_matrix(initial_board)
        self.game.player_turn = self.game.possibles_players[index]
        self.game.flip_pieces(cordinates)
        self.assertEqual(
            self._convert_scenario_to_matrix(final_board), self.game._board)

    @parameterized.expand(
        [
            (validate_direction_1, PLAYER1, 6, 4, N, [(5, 4), (4, 4)]),
            (validate_direction_1, PLAYER2, 7, 4, NE, [(6, 5), (5, 6)]),
            (validate_direction_1, PLAYER2, 0, 5, E, [(0, 6)]),
            (validate_direction_1, PLAYER1, 0, 0, SE, [(1, 1)]),
            (validate_direction_2, PLAYER1, 0, 6, S, [(1, 6), (2, 6), (3, 6),
                                                      (4, 6), (5, 6), (6, 6)]),
            (validate_direction_1, PLAYER2, 2, 5, SW, [(3, 4), (4, 3)]),
            (validate_direction_2, PLAYER2, 4, 3, W, [(4, 2), (4, 1)]),
            (validate_direction_2, PLAYER2, 6, 4, NW, [(5, 3), (4, 2),
                                                       (3, 1)]),
            (validate_direction_2, PLAYER2, 0, 4, N, []),
            (validate_direction_2, PLAYER1, 3, 0, W, []),
            (validate_direction_2, PLAYER2, 7, 1, S, []),
            (validate_direction_2, PLAYER1, 5, 7, E, []),
            (validate_direction_2, PLAYER1, 1, 3, E, []),
        ]
    )
    def test_validate_direction(self, board, player,
                                row, col, direction, expected):
        self.game._board = board
        self.game.player_turn = player
        self.assertEqual(expected,
                         self.game.validate_direction(row, col, direction))

    def test_select_winner_white(self):
        self.game._board = self._convert_scenario_to_matrix(board_winner_w)
        winner = self.game.determine_winner()
        self.assertEqual(PLAYER2, winner)

    def test_select_winner_black(self):
        self.game._board = self._convert_scenario_to_matrix(diagonal_flip)
        winner = self.game.determine_winner()
        self.assertEqual(PLAYER1, winner)

    def test_select_winner_tie(self):
        self.game._board = self._convert_scenario_to_matrix(board_tie)
        winner = self.game.determine_winner()
        self.assertEqual(TIE_MATCH, winner)

    def test_select_empty_tie(self):
        self.game._board = self._convert_scenario_to_matrix(board_tie_empty)
        winner = self.game.determine_winner()
        self.assertEqual(TIE_MATCH, winner)

    @parameterized.expand(
        [
            (validate_direction_2, PLAYER1, 1, 2, []),
            (validate_direction_2, PLAYER1, 0, 6, [(1, 6), (2, 6), (3, 6),
                                                   (4, 6), (5, 6), (6, 6)]),
        ]
    )
    def test_validate_move(self, board, player, row, col, expected):
        self.game._board = board
        self.game.player_turn = player
        self.assertEqual(expected, self.game.validate_move(row, col))

    @parameterized.expand(
        [
            (all_poss_moves_board_1, all_poss_moves_exp_1),
        ]
    )
    def test_all_possible_moves_values(self, board, expected):
        self.game._board = self._convert_scenario_to_matrix(board)
        result = self.game.all_possible_moves()
        for key, value in result.items():
            result_list = sorted(value, key=lambda tup: (tup[0], tup[1]))
            expected_list = sorted(expected[key],
                                   key=lambda tup: (tup[0], tup[1]))
            self.assertEqual(result_list, expected_list)

    @parameterized.expand(
        [
            (all_poss_moves_board_1, all_poss_moves_exp_1)
        ]
    )
    def test_all_possible_moves_values_key(self, board, expected):
        self.game._board = self._convert_scenario_to_matrix(board)
        result = self.game.all_possible_moves()
        self.assertEqual(result.keys(), expected.keys())

    def test_no_posible_moves(self):
        self.game._board = self._convert_scenario_to_matrix(
            all_poss_moves_board_2)
        result = self.game.all_possible_moves()
        self.assertEqual(result, {})

    @parameterized.expand(
        [
            (all_poss_moves_board_1, none_pos_exp_1),
            (all_poss_moves_board_2, [])
        ]
    )
    def test_none_pos(self, board, expected):
        self.game._board = self._convert_scenario_to_matrix(board)
        result = self.game.none_pos()
        self.assertListEqual(result, expected)

    @parameterized.expand([
        (black_12, black_12_that_will_print)
    ])
    def test_board_printer(self, board, expected_result):
        self.game._board = board
        result = self.game.board_printer()
        for row in range(len(self.game._board)):
            self.assertEqual(result[row], expected_result[row])

    @parameterized.expand([
        (black_12, black_12_that_will_print),
        (white_12, white_12_that_will_print),
    ])
    def test_board(self, board, expected_result):
        expected_result_as_string = ''
        for rows in expected_result:
            expected_result_as_string += rows + '\n'
        self.game._board = board
        result = self.game.board
        self.assertEqual(result, expected_result_as_string)

    @parameterized.expand(
        [
            (play_board_tie, 7, 0, PLAYER2, TIE_MATCH),
            (play_board_1, 0, 0, PLAYER1,
             f"Bad move of player {PLAYER1}. Try again"),
            (play_board_1, 2, 3, PLAYER1, MOVE_OK),
            (play_board_b_wins, 0, 7, PLAYER1, f"{PLAYER1} wins the match"),
            (play_board_w_wins, 7, 7, PLAYER2, f"{PLAYER2} wins the match"),
        ]
    )
    def test_play(self, board, row, col, player, expected):
        self.game.player_turn = player
        self.game._board = self._convert_scenario_to_matrix(board)
        result = self.game.play(row, col)
        self.assertEqual(result, expected)

    @parameterized.expand(
        [
            (True, PLAYER1, f"Turn of Player {PLAYER1}"),
            (True, PLAYER2, f"Turn of Player {PLAYER2}"),
            (False, PLAYER2, GAME_OVER),
        ]
    )
    def test_next_turn(self, state, player, expected):
        self.game.is_playing = state
        self.game.player_turn = player
        result = self.game.next_turn()
        self.assertEqual(result, expected)

    def test_put_piece(self):
        self.game.put_piece((0, 0))
        expected = self._convert_scenario_to_matrix(put_piece_board)
        self.assertEqual(self.game._board, expected)


if __name__ == "__main__":
    unittest.main()
