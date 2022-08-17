import unittest
from copy import deepcopy

from parameterized import parameterized

from .constants import (GOLD, GOLD_QUANTITY, HIDE_CELL, LOSE, PLAYER,
                        SCORE_GAME, VISITED_CELL, VISITED_CELL_USER, WIN,
                        WUMPUS, WUMPUS_QUANTITY, HOLES_QUANTITY, HOLES, COL,
                        ROW, MOVES, MOVES_DIRECTION,
                        MESSAGE_NEXT_TURN)


from wumpus.game import WumpusGame

from .scenarios import (INITIAL_BIG_FAIL_BOARD, SCENARIO_1, SCENARIO_2,
                        SCENARIO_3, SCENARIO_4,
                        SCENARIO_CELL_PARSE_1, SCENARIO_CELL_PARSE_2,
                        SCENARIO_CELL_PARSE_3, SCENARIO_CELL_PARSE_4,
                        SCENARIO_CELL_PARSE_5,
                        SCENARIO_CELL_PARSE_1_USER_VIEW,
                        SCENARIO_CELL_PARSE_2_USER_VIEW,
                        SCENARIO_CELL_PARSE_3_USER_VIEW,
                        SCENARIO_CELL_PARSE_4_USER_VIEW,
                        SCENARIO_CELL_PARSE_5_USER_VIEW,
                        SCENARIO_EATEN_BY_WUMPUS,
                        SCENARIO_MOVE_ACTION,
                        SCENARIO_5,
                        SCENARIO_FALL_IN_HOLES, SCENARIO_PLAY_SHOOT_OK_F,
                        SCENARIO_TEST_GOLD,
                        SCENARIO_TEST_DELETE,
                        SCENARIO_WIN_GOLD,
                        SCENARIO_SHOOT_WUMPUS_INIT,
                        SCENARIO_SHOOT_WUMPUS_FINAL,
                        SCENARIO_SHOOT_WUMPUS_SIGNAL_INIT,
                        SCENARIO_SHOOT_WUMPUS_SIGNAL_FIN,
                        SCENARIO_SHOOT_FAIL_INIT,
                        SCENARIO_SIGNAL_WUMPUS_HOLE,
                        SCENARIO_SIGNAL_HOLE,
                        SCENARIO_SIGNAL_WUMPUS,
                        SCENARIO_SIGNAL_EMPTY,
                        SCENARIO_PLAY_MOVE,
                        SCENARIO_SIGNAL_HOLE_J,
                        SCENARIO_SIGNAL_WUMPUS_J,
                        SCENARIO_SIGNAL_WUMPUS_HOLE_J,
                        SCENARIO_SIGNAL_J_EMPTY,
                        SCENARIO_WITH_OUT_GOLD,
                        SCENARIO_FIND_POSITION,
                        SCENARIO_FIND_POSITION_HOLES,
                        SCENARIO_FIND_POSITION_H_BORDER,
                        SCENARIO_FIND_POS_H_BOR_LEFT,
                        RECURSIVE, INITIAL_FAIL_BOARD,
                        RECURSIVE_SIDE, VALID_HOLE_SCENARIO,
                        RECURSIVE_SIDE_BORDER,
                        SCENARIO_PLAY_MOVE_FINAL,
                        SCENARIO_PLAY_SHOOT,
                        SCENARIO_PLAY_SHOOT_OK,
                        SCENARIO_PLAY_LAST_GOLD,
                        SCENARIO_PLAY_LAST_GOLD_FIN,
                        SCENARIO_PLAY_WIN_GOLD,
                        SCENARIO_PLAY_WIN_GOLD_F)


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = WumpusGame()

    def test_initial_game(self):
        self.assertEqual(self.game.is_playing, True)

    def test_board_columns(self):
        for row in self.game._board:
            self.assertEqual(len(row), COL)

    def test_board_rows(self):
        self.assertEqual(len(self.game._board), ROW)

    def test_initial_place_player(self):
        self.game.place_player()
        self.assertEqual(self.game._board[0][0], PLAYER)

    @parameterized.expand([
        (SCENARIO_1, PLAYER, [(0, 0)]),
        (SCENARIO_2, PLAYER, [(1, 3)]),
        (SCENARIO_3, PLAYER, [(3, 5)]),
        (SCENARIO_4, PLAYER, [])
    ])
    def test_position_finder(self, board, item, expected):
        self.game._board = board
        position_list = self.game.position_finder(item)
        self.assertEqual(position_list, expected)

    @parameterized.expand([
        (SCENARIO_1, 7, 0, True),
        (SCENARIO_2, 1, 3, False),
        (SCENARIO_3, 3, 0, True),
        (SCENARIO_4, 3, 6, True),
    ])
    def test_check_is_empty(self, board, row, col, expected):
        self.game._board = board
        is_empty = self.game.check_is_empty(row, col)
        self.assertEqual(is_empty, expected)

    @parameterized.expand([
        (SCENARIO_5, 1, 4),
        (SCENARIO_5, 3, 4),
        (SCENARIO_5, 2, 5),
        (SCENARIO_5, 2, 6)

    ])
    def test_move_transaction(self, board, row, col):
        self.game._board = board
        old_row, old_row = self.game.position_finder(PLAYER)[0]
        value_cell = self.game._board[old_row][old_row]
        self.game.move_player_transaction(row, col)
        self.assertEqual(self.game._board[old_row][old_row],
                         value_cell.replace(PLAYER, ''))
        self.assertEqual(self.game._board[row][col], PLAYER)

    @parameterized.expand([
        (GOLD, GOLD_QUANTITY),
        (WUMPUS, WUMPUS_QUANTITY),
        (HOLES, HOLES_QUANTITY)
    ])
    def test_place_item(self, item, quantity):
        gameTest = WumpusGame()
        gameTest._board = [['' for j in range(COL)] for i in range(ROW)]
        gameTest.place_item(item, quantity)
        self.assertEqual(len(gameTest.position_finder(item)), 8)

    @parameterized.expand([
        (2, 4, True),
        (4, 12, False),
        (4, 5, True),
        (7, 14, True),
        (1, 0, False),
        (0, 0, False),
        (6, 4, True),
        (5, 5, True),
        (7, 0, False),
        (5, 6, False),
    ])
    def test_there_is_gold(self, row, col, expeted):
        game = WumpusGame()
        game._board = SCENARIO_TEST_GOLD
        result = game.there_is_gold(row, col)
        self.assertEqual(result, expeted)

    @parameterized.expand([
        (GOLD, 5, 5, ''),
        (WUMPUS, 7, 8, ''),
        (WUMPUS, 7, 14, ''),
        (GOLD, 2, 10, ''),
        (PLAYER, 3, 4, ''),
    ])
    def test_delete_item(self, item, row, col, expected):
        game = WumpusGame()
        game._board = SCENARIO_TEST_DELETE
        game.delete_item_on_position(item, row, col)
        result = game._board[row][col]
        self.assertEqual(result, expected)

    @parameterized.expand([
        (5, 4),
        (5, 6),
        (4, 5),
        (6, 5),
    ])
    def test_move_and_win_gold(self, row, col):

        game = WumpusGame()
        game._board = deepcopy(SCENARIO_WIN_GOLD)
        old_player_row, old_player_col = game.position_finder(PLAYER)[0]
        game.move_and_win_gold(row, col)
        new_player_row, new_player_col = game.position_finder(PLAYER)[0]
        self.assertEqual((new_player_row, new_player_col), (row, col))
        self.assertEqual(game._board[old_player_row][old_player_col],
                         VISITED_CELL)
        self.assertTrue(GOLD not in game._board[row][col])
        self.assertEqual(len(game.position_finder(GOLD)), 3)

    @parameterized.expand([
        (1000, 2000, SCORE_GAME["gold_wumpus"]),
        (0, -10, SCORE_GAME["move"]),
        (1000, 950, SCORE_GAME["lost_shoot"])
    ])
    def test_score_manager(self, initial_score, final_score, score):
        self.game.score = initial_score
        self.game.modify_score(score)
        self.assertEqual(final_score, self.game.score)

    @parameterized.expand([
        (WIN, '', 'CONGRATS!! You WIN!!! Your final score is '),
        (LOSE, WUMPUS, "Bad Luck! You lose. You have eaten by a Wumpus."
            + " Your final score is "),
        (LOSE, HOLES, "Bad Luck! You lose. You falled into a hole."
            + " Your final score is "),
    ])
    def test_game_over(self, result, reason, expected_message):
        game = WumpusGame()
        game.game_over(result, reason)
        self.assertEqual(game.is_playing, False)
        self.assertEqual(game.result_of_game, result)
        self.assertEqual(game.message_game_over, expected_message)

    @parameterized.expand([  # parameters of shoot_arrow
        (SCENARIO_SHOOT_WUMPUS_INIT, 1000, 4, 4,
         SCENARIO_SHOOT_WUMPUS_FINAL, 2000, 10, 9),
        (SCENARIO_SHOOT_WUMPUS_SIGNAL_INIT, 1000, 4, 4,
         SCENARIO_SHOOT_WUMPUS_SIGNAL_FIN, 2000, 8, 7),
        (SCENARIO_SHOOT_FAIL_INIT, 1000, 4, 4,
         SCENARIO_SHOOT_FAIL_INIT, 950, 1, 0)
    ])
    def test_shoot_arrow(self, initial_board, initial_score,
                         row, col, final_board, final_score,
                         quantity_rows, final_q_row):
        self.game._board = initial_board
        self.game.score = initial_score
        self.game.swords = quantity_rows
        self.game.shoot_arrow(row, col)
        self.assertEqual(self.game._board, final_board)
        self.assertEqual(self.game.score, final_score)
        self.assertEqual(self.game.swords, final_q_row)

    @parameterized.expand([  # parameters of shoot_arrow
        (SCENARIO_SHOOT_WUMPUS_INIT, 4, 4, 0),
    ])
    def test_shoot_arrow_exception(self, initial_board,
                                   row, col, quantity_rows):
        self.game._board = initial_board
        self.game.swords = quantity_rows
        with self.assertRaises(Exception):
            self.game.shoot_arrow(row, col)

    @parameterized.expand([
        (5, 4),
        (5, 6),
        (4, 5),
        (6, 5),
    ])
    def test_fall_in_hole(self, row, col):

        game = WumpusGame()
        game._board = deepcopy(SCENARIO_FALL_IN_HOLES)

        content_destination_cell = game._board[row][col]
        old_player_row, old_player_col = game.position_finder(PLAYER)[0]
        game.move_and_game_over(HOLES)
        player_in_board = game.position_finder(PLAYER)

        self.assertEqual(game._board[old_player_row][old_player_col],
                         VISITED_CELL)
        self.assertEqual(game._board[row][col], content_destination_cell)
        self.assertEqual(player_in_board, [])
        self.assertEqual(game.is_playing, False)
        self.assertEqual(game.result_of_game, LOSE)

    @parameterized.expand([
        (5, 4),
        (5, 6),
        (4, 5),
        (6, 5),
    ])
    def test_eaten_by_wumpus(self, row, col):

        game = WumpusGame()
        game._board = deepcopy(SCENARIO_EATEN_BY_WUMPUS)
        content_destination_cell = game._board[row][col]
        old_player_row, old_player_col = game.position_finder(PLAYER)[0]
        game.move_and_game_over(WUMPUS)
        player_in_board = game.position_finder(PLAYER)

        self.assertEqual(game._board[old_player_row][old_player_col],
                         VISITED_CELL)
        self.assertEqual(game._board[row][col], content_destination_cell)
        self.assertEqual(player_in_board, [])
        self.assertEqual(game.is_playing, False)
        self.assertEqual(game.result_of_game, LOSE)

    @parameterized.expand([

        (5, 4, WUMPUS, True),
        (5, 6, WUMPUS, False),
        (5, 6, HOLES, True),
        (4, 5, HOLES, False),
        (4, 5, GOLD, True),
        (6, 5, GOLD, False),
    ])
    def test_is_there_item(self, row, col, item, expected):

        game = WumpusGame()
        game._board = deepcopy(SCENARIO_MOVE_ACTION)
        game.there_is_item(item, row, col)

    @parameterized.expand([
        ("s", 0, 0, (1, 0)),
        ("w", 0, 0, ()),
        ("w", 1, 1, (0, 1)),
        ("a", 0, 0, ()),
        ("a", 1, 1, (1, 0)),
        ("d", 0, 0, (0, 1)),
        ("y", 0, 0, ()),
        ("s", 7, 7, ()),
    ])
    def test_find_coord(self, direction, row, col, final_coord):
        game = WumpusGame()
        game._board[0][0] = ""
        game._board[row][col] = "J"
        final_dir = game.find_coord(direction)
        self.assertEqual(final_dir, final_coord)

    @parameterized.expand([  # test with correct moves
        (MOVES["move"], MOVES_DIRECTION["south"], 0, 0, 1, 0, -10),
        (MOVES["move"], MOVES_DIRECTION["east"], 0, 0, 0, 1, -10),
        (MOVES["move"], MOVES_DIRECTION["north"], 1, 1, 0, 1, -10),
        (MOVES["move"], MOVES_DIRECTION["south"], 1, 1, 2, 1, -10),
        (MOVES["shoot"], MOVES_DIRECTION["east"], 0, 0, 0, 0, -50),
        (MOVES["shoot"], MOVES_DIRECTION["north"], 1, 1, 1, 1, -50),
        (MOVES["shoot"], MOVES_DIRECTION["west"], 1, 1, 1, 1, -50),
    ])
    def test_admin_move(self, accion, direccion, row, col,
                        final_row, final_col, expected_score):
        self.game._board = [["" for j in range(COL)] for i in range(ROW)]
        self.game._board[row][col] = "J"
        self.game.score = 0
        self.game.manager_move(accion, direccion)
        position_player = self.game.position_finder(PLAYER)
        self.assertEqual(self.game.score, expected_score)
        self.assertEqual(position_player[0], (final_row, final_col))

    @parameterized.expand([  # test exceptions moves
        (MOVES["shoot"], MOVES_DIRECTION["north"], 0, 0),
        (MOVES["shoot"], MOVES_DIRECTION["south"], 7, 14),
        (MOVES["shoot"], MOVES_DIRECTION["east"], 7, 14),
        (MOVES["shoot"], MOVES_DIRECTION["west"], 7, 0),
    ])
    def test_admin_move_exceptions_shoot(self, accion, direccion, row, col):
        self.game._board = [["" for j in range(COL)] for i in range(ROW)]
        self.game._board[row][col] = "J"
        self.game.score = 0
        with self.assertRaises(Exception):
            self.game.manager_move(accion, direccion)

    @parameterized.expand([  # test exceptions moves
        (MOVES["move"], MOVES_DIRECTION["north"], 0, 0),
        (MOVES["move"], MOVES_DIRECTION["south"], 7, 14),
        (MOVES["move"], MOVES_DIRECTION["east"], 7, 14),
        (MOVES["move"], MOVES_DIRECTION["west"], 7, 0),
    ])
    def test_admin_move_exceptions(self, accion, direccion, row, col):
        self.game._board = [["" for j in range(COL)] for i in range(ROW)]
        self.game._board[row][col] = "J"
        self.game.score = 0
        with self.assertRaises(Exception):
            self.game.manager_move(accion, direccion)

    @parameterized.expand([
        (5, 4, WUMPUS, False),
        (5, 6, HOLES, False),
        (4, 5, PLAYER, False),
        (6, 5, PLAYER, True),
    ])
    def test_move_action(self, row, col, expeted_item, is_playing):

        game = WumpusGame()
        game._board = deepcopy(SCENARIO_MOVE_ACTION)

        old_player_row, old_player_col = game.position_finder(PLAYER)[0]
        game.move_player(row, col)

        self.assertEqual(game._board[old_player_row][old_player_col],
                         VISITED_CELL)
        self.assertEqual(game._board[row][col], expeted_item)
        self.assertEqual(game.is_playing, is_playing)

    @parameterized.expand([

        ("   ", 0, 1, "~  ", SCENARIO_SIGNAL_HOLE),
        ("   ", 2, 2, "  +", SCENARIO_SIGNAL_WUMPUS),
        ("   ", 5, 5, "~ +", SCENARIO_SIGNAL_WUMPUS_HOLE),
        ("   ", 3, 3, "   ", SCENARIO_SIGNAL_EMPTY),
        (" J ", 4, 4, "~J ", SCENARIO_SIGNAL_HOLE_J),
        (" J ", 4, 4, " J+", SCENARIO_SIGNAL_WUMPUS_J),
        (" J ", 5, 5, "~J+", SCENARIO_SIGNAL_WUMPUS_HOLE_J),
        (" J ", 4, 4, " J ", SCENARIO_SIGNAL_J_EMPTY),
    ])
    def test_find_signal(self, item, row, col, final_item, board):
        game = WumpusGame()
        game._board = board
        game._board[row][col] = item
        modify_item = game.find_signal(item, row, col)
        self.assertEqual(modify_item, final_item)

    @parameterized.expand([
        (SCENARIO_CELL_PARSE_1, 5, 5, '~J+'),
        (SCENARIO_CELL_PARSE_1, 5, 4, HIDE_CELL),
        (SCENARIO_CELL_PARSE_1, 5, 6, HIDE_CELL),
        (SCENARIO_CELL_PARSE_1, 4, 5, HIDE_CELL),
        (SCENARIO_CELL_PARSE_1, 6, 5, HIDE_CELL),
        (SCENARIO_CELL_PARSE_1, 7, 5, VISITED_CELL_USER),
        (SCENARIO_CELL_PARSE_2, 1, 4, ' J '),
        (SCENARIO_CELL_PARSE_2, 1, 1, HIDE_CELL),
        (SCENARIO_CELL_PARSE_2, 1, 2, HIDE_CELL),
        (SCENARIO_CELL_PARSE_2, 0, 5, HIDE_CELL),
        (SCENARIO_CELL_PARSE_2, 0, 0, VISITED_CELL_USER),
        (SCENARIO_CELL_PARSE_2, 2, 4, HIDE_CELL),
        (SCENARIO_CELL_PARSE_2, 0, 4, '~  '),
        (SCENARIO_CELL_PARSE_2, 0, 3, VISITED_CELL_USER),
        (SCENARIO_CELL_PARSE_2, 0, 2, '~  '),
        (SCENARIO_CELL_PARSE_2, 0, 1, '  +'),
        (SCENARIO_CELL_PARSE_3, 5, 5, ' J+'),
        (SCENARIO_CELL_PARSE_4, 5, 5, '~J '),
        (SCENARIO_CELL_PARSE_5, 5, 5, ' J '),


    ])
    def test_parse_cell(self, board, row, col, expected):

        game = WumpusGame()

        game._board = deepcopy(board)
        parsed_cell = game.parse_cell(row, col)
        self.assertEqual(parsed_cell, expected)

    @parameterized.expand([

        (True, 1000, MESSAGE_NEXT_TURN),
    ])
    def test_next_turn_true(self, play_condition, score, final_message):
        game = WumpusGame()
        game._playing = play_condition
        game.score = score
        message = game.next_turn()
        self.assertEqual(message, final_message)

    @parameterized.expand([
        (WIN, '', 'CONGRATS!! You WIN!!! Your final score is 1000'),
        (LOSE, WUMPUS, "Bad Luck! You lose. You have eaten by a Wumpus."
            + " Your final score is 1000"),
        (LOSE, HOLES, "Bad Luck! You lose. You falled into a hole."
            + " Your final score is 1000"),
    ])
    def test_next_turn_game_over(self, result, reason, expected_msg):

        game = WumpusGame()
        game.score = 1000

        game.game_over(result, reason)
        message = game.next_turn()
        self.assertEqual(message, expected_msg)

    @parameterized.expand([
        (SCENARIO_CELL_PARSE_1, SCENARIO_CELL_PARSE_1_USER_VIEW),
        (SCENARIO_CELL_PARSE_2, SCENARIO_CELL_PARSE_2_USER_VIEW),
        (SCENARIO_CELL_PARSE_3, SCENARIO_CELL_PARSE_3_USER_VIEW),
        (SCENARIO_CELL_PARSE_4, SCENARIO_CELL_PARSE_4_USER_VIEW),
        (SCENARIO_CELL_PARSE_5, SCENARIO_CELL_PARSE_5_USER_VIEW),
    ])
    def test_board(self, board, expeted_board):

        game = WumpusGame()
        game._board = board
        self.assertEqual(game.board, expeted_board)

    @parameterized.expand([
        (SCENARIO_WITH_OUT_GOLD, False, WIN)
    ])
    def test_count_golds(self, board_i, state_game, final_expresion):
        game = WumpusGame()
        game._board = board_i
        game.count_golds()
        self.assertEqual(game.is_playing, state_game)
        self.assertEqual(game.result_of_game, final_expresion)

    @parameterized.expand([
        (1, 1, SCENARIO_FIND_POSITION, [(0, 1), (1, 0), (1, 2), (2, 1)]),
        (5, 5, SCENARIO_FIND_POSITION_HOLES, []),
        (0, 5, SCENARIO_FIND_POSITION_H_BORDER, [(0, 4), (0, 6)]),
        (2, 0, SCENARIO_FIND_POS_H_BOR_LEFT, [(2, 1)]),
    ])
    def test_find_posible_moves_gold(self, row, col, board,
                                     position_list):
        game = WumpusGame()
        game._board = board
        find_list = game._find_posible_moves_gold(row, col, board)
        self.assertEqual(find_list, position_list)

    @parameterized.expand([
        ((7, 7), RECURSIVE, True),
        ((4, 4), INITIAL_FAIL_BOARD, False),
        ((7, 7), INITIAL_BIG_FAIL_BOARD, False),
        ((2, 7), RECURSIVE_SIDE, True),
        ((7, 0), RECURSIVE_SIDE_BORDER, False),
    ])
    def test_find_gold_way(self, gold_position, board, bool_return):
        game = WumpusGame()
        game._board = board
        self.assertEqual(game._find_gold_recursive(0, 0, gold_position,
                         board, []), bool_return)

    @parameterized.expand([
        (7, 10, VALID_HOLE_SCENARIO, True),
        (7, 4, VALID_HOLE_SCENARIO, False),
        (7, 5, VALID_HOLE_SCENARIO, False),
        (7, 3, VALID_HOLE_SCENARIO, False),
    ])
    def test_valid_hole(self, row, col, board, expected):
        game = WumpusGame()
        game._board = board
        self.assertEqual(game._valid_hole(row, col), expected)

    @parameterized.expand([
        ("m", "w", SCENARIO_PLAY_MOVE, SCENARIO_PLAY_MOVE_FINAL, True, -10),
        ("z", "w", SCENARIO_PLAY_SHOOT, SCENARIO_PLAY_SHOOT, True, -50),
        ("z", "w", SCENARIO_PLAY_SHOOT_OK, SCENARIO_PLAY_SHOOT_OK_F,
         True, 1000),
        ("m", "w", SCENARIO_PLAY_LAST_GOLD, SCENARIO_PLAY_LAST_GOLD_FIN,
         False, 990),
        ("m", "w", SCENARIO_PLAY_WIN_GOLD, SCENARIO_PLAY_WIN_GOLD_F,
         True, 990),
    ])
    def test_play(self, action, direction, initial_board, expected_result,
                  expected_is_playing, expected_score):
        game = WumpusGame()
        game._board = initial_board
        game.play(action, direction)
        self.assertEqual(game.is_playing, expected_is_playing)
        self.assertEqual(game.score, expected_score)
        self.assertEqual(initial_board, expected_result)

    def test_play_exception(self):
        game = WumpusGame()
        self.assertEqual(game.play('m', 'w'), "Bad move")
