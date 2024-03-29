
import unittest
from parameterized import parameterized
from backgammon.game.backgammon import BackgammonGame
from backgammon.tests.test_scenarios import (
    initial_board,
    board_1,
    board_4,
    board_5,
    board_6,
    board_9,
    board_10,
    board_11,
    board_12,
    board_13,
    message,
    next_turn_message_B,
    next_turn_message_W,
    next_turn_message_TIE,
    initial_board2,
    board_7,
    presented_initial_board,
    presented_board7,
    return_board_str,)
from unittest.mock import patch
from backgammon.game.constants import (
    BLACK,
    WHITE,
    TIE,
    WINNER_BLACK,
    WINNER_WHITE)


class BackgammonGameTest(unittest.TestCase):

    def setUp(self):
        self.backgammon = BackgammonGame()

    def test_game_active_change(self):
        self.backgammon.game_active_change()
        self.assertEqual(self.backgammon.active_game, False)

    def test_slots(self):
        self.assertEqual(len(self.backgammon.board_matrix), 24)

    def test_initial_board(self):
        expected_board = [
            [2, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 5],
            [0, 0], [0, 3], [0, 0], [0, 0], [0, 0], [5, 0],
            [0, 5], [0, 0], [0, 0], [0, 0], [3, 0], [0, 0],
            [5, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 2]
        ]
        self.assertListEqual(expected_board, self.backgammon.board_matrix)

    @parameterized.expand([
        (WHITE, initial_board, 0, 11, 16, 18),
        (BLACK, initial_board, 5, 7, 12, 23)
    ])
    def test_available_pieces(self, side, board, *expected_result):
        self.backgammon.board_matrix = board
        result = self.backgammon.available_pieces(side)
        self.assertEqual(result, list(expected_result))

    @parameterized.expand([
        (WHITE,),
        (BLACK,),
    ])
    def test_player(self, patch_color):
        with patch('random.choice', return_value=patch_color):
            new_game = BackgammonGame()
            player = new_game._turn
        self.assertEqual(player, patch_color)

    @parameterized.expand([
        (1, 2,),
        (2, 3,),
        (3, 4,),
        (4, 6,),
        (5, 5,),
        (6, 1,),
    ])
    @patch('random.randint')
    def test_roll_dices_number_interval(self, first_dice,
                                        second_dice, patch_function):
        patch_function.side_effect = [first_dice, second_dice]
        self.assertEqual(self.backgammon.roll_dices(),
                         (first_dice, second_dice))

    @parameterized.expand([
        (WHITE, BLACK),
        (BLACK, WHITE),
    ])
    def test_opposite(self, current_player, expected):

        self.backgammon._turn = current_player
        self.assertEqual(self.backgammon.opposite, expected)

    @parameterized.expand(
        [
            (3, BLACK, WHITE),
            (1, WHITE, BLACK),
            (4, WHITE, WHITE),
            (7, WHITE, BLACK),
        ]
    )
    @patch('random.choice')
    def test_change_player(self, it, expected,
                           patch_value, patch_function):
        patch_function.return_value = patch_value
        game = BackgammonGame()
        for _ in range(it):
            game.change_turn()
        self.assertEqual(expected, game._turn)

    @parameterized.expand([
        (BLACK, 0, False),
        (WHITE, 1, True)
    ])
    def test_less_than_two_enemies_in_position(self, current_player, position,
                                               expected_result):
        self.backgammon._turn = current_player
        result = self.backgammon.less_than_two_enemies_in_position(position)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        (WHITE, 11, False),
        (WHITE, 16, True),
        (WHITE, 18, False),
        (BLACK, 5, False),
        (BLACK, 12, False),
    ])
    def test_less_than_five_own_pieces(self, current_player,
                                       position, expected):
        self.backgammon._turn = current_player
        result = self.backgammon.less_than_five_own_pieces(position)
        self.assertEqual(result, expected)

    @parameterized.expand(
        [
            (BLACK, 0, False),
            (WHITE, 1, False),
            (WHITE, 11, True),
            (BLACK, 5, True),
        ]
    )
    def test_at_least_one_piece_of_the_player(self, current_player,
                                              position, expected_result):
        self.backgammon._turn = current_player
        result = self.backgammon.at_least_one_piece_of_the_player(position)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        (BLACK, 2, -1, True),
        (WHITE, 21, 27, True),
        (WHITE, 1, 5, False),
        (WHITE, 5, 6, False),
        (WHITE, 0, 11, False),
        (BLACK, 5, 2, True),
        (BLACK, 12, 7, True),
        (BLACK, 23, 19, True),
        (BLACK, 21, 22, False),
        (BLACK, 23, 18, False),
    ])
    def test_valid_move(self, current_player,
                        initial_pos, final_pos, expected):
        self.backgammon._turn = current_player
        result = self.backgammon.is_valid_move(initial_pos, final_pos)
        self.assertEqual(result, expected)

    @parameterized.expand([
        (5,)
    ])
    def test_capture_opposite_piece(self, new_position):
        game = BackgammonGame()
        game._turn = WHITE
        game.capture_opposite_piece(new_position)
        captured_piece = game.expelled[BLACK]
        self.assertEqual(1, captured_piece)

    @parameterized.expand([
        (initial_board, 0, 1, 0),
        (initial_board, 23, 21, 1),
        (initial_board, -1, 2, 0),
        (initial_board, 25, 20, 1)
    ])
    def test_change_position(self, board, old_position, new_position, actual_player):
        game = BackgammonGame()
        game._turn = WHITE if actual_player == 0 else BLACK
        game.board_matrix = board
        game.change_position(old_position, new_position)
        self.assertEqual(1, game.board_matrix[new_position][actual_player])

    @parameterized.expand([
        (2, 3, [2, 3, 5]),
        (3, 4, [3, 4, 7]),
        (5, 5, [5, 10, 15, 20])
    ])
    def test_get_move_options(self, d1, d2, expected):
        self.backgammon.roll_dices(d1, d2)
        self.assertEqual(self.backgammon.move_options, expected)

    @parameterized.expand([
        (3, 4, 3, [4]),
        (3, 4, 4, [3]),
        (3, 4, 7, []),
        (4, 4, 16, []),
        (4, 4, 12, [4]),
        (4, 4, 8, [4, 8]),
        (4, 4, 4, [4, 8, 12]),
        (5, 5, 15, [5]),
        (5, 5, 5, [5, 10, 15]),
        (5, 5, 10, [5, 10]),
        (5, 5, 5, [5, 10, 15]),
        (6, 6, 6, [6, 12 ,18]),
        (6, 6, 12, [6, 12]),
        (2, 2, 2, [2, 4, 6]),
    ])
    def test_update_move_options(
        self, 
        d1, 
        d2, 
        move,
        expectedResult,
    ):
        self.backgammon.roll_dices(d1, d2)
        self.backgammon.update_move_options(move)
        self.assertEqual(self.backgammon.move_options, expectedResult)

    @parameterized.expand([
        (board_1, WHITE, 5, True),
        (board_1, WHITE, 1, False),
        (board_1, BLACK, 10, True),
        (board_1, BLACK, 11, False)
    ])
    def test_can_capture(self, board, current_player, new_position, expected):
        game = BackgammonGame()
        game.board_matrix = board
        game._turn = current_player
        result = game.can_capture(new_position)
        self.assertEqual(result, expected)

    @parameterized.expand([
        (WHITE, 0, 1, 1, 3, [3]),
        (WHITE, 0, 6, 6, 5, [5]),
        (WHITE, 0, 2, 1, 1, [1, 1]),
        (BLACK, 23, 21, 1, 2, [1]),
        (BLACK, 23, 18, 2, 3, []),
    ])
    def test_make_move(self, current_player, actual_position,
                       new_position, first_dice, second_dice, expected):
        game = BackgammonGame()
        game._turn = current_player
        game.roll_dices(first_dice, second_dice)
        game.make_move(actual_position, new_position)
        self.assertEqual(game.total_dices, expected)


    @parameterized.expand([  # test check game status
        (6, 8, 20, True),
        (15, 8, 20, False),
        (6, 15, 20, False),
        (6, 8, 20, True),
        (6, 12, 40, False),
        (11, 5, 40, False),
        (11, 11, 40, False),
    ])
    def test_check_game_status(self, black_points, white_points, turn,
                               expected):
        self.backgammon.points[BLACK] = black_points
        self.backgammon.points[WHITE] = white_points
        self.backgammon.current_turn = turn
        self.backgammon.check_game_status()
        self.assertEqual(self.backgammon.active_game, expected)

    @parameterized.expand([
        (15, 8, WINNER_BLACK),
        (15, 15, TIE),
        (6, 15, WINNER_WHITE),
    ])
    def test_get_current_winner(self, black_points, white_points,
                                expected):
        self.backgammon.points[BLACK] = black_points
        self.backgammon.points[WHITE] = white_points
        result = self.backgammon.get_current_winner()
        self.assertEqual(result, expected)

    @parameterized.expand([
        (WHITE, 2, 5, 5, [5, 10, 15, 20], 20, board_12, 1),
        (BLACK, 0, 4, 1, [1, 4, 5], 22, board_11, 0),
        (BLACK, 1, 1, 1, [1, 2, 3, 4], 22, board_13, 1),
        (WHITE, 3, 3, 4, [3, 4, 7], 3, board_13, 1)
    ])
    @unittest.skip('refactor')
    def test_insert_captured_piece(self, current_player,
                                   pieces_captured, first_dice,
                                   second_dice, move_options, new_position,
                                   board, expected):
        game = BackgammonGame()
        game.board_matrix = board
        game._turn = current_player
        game.expelled[current_player] = pieces_captured
        game.roll_dices(first_dice, second_dice)
        game.insert_captured_piece(new_position)
        col = 0 if game._turn == WHITE else 1
        result = game.board_matrix[new_position][col]
        self.assertEqual(result, expected)

    @parameterized.expand([
        (WHITE, 24, 1),
        (BLACK, 0, 0),
        (BLACK, -1, 1),
        (WHITE, 23, 0)
    ])
    def test_increment_points(self, current_player,
                              new_position, expected):
        game = BackgammonGame()
        game._turn = current_player
        game.increment_points(new_position)
        points = game.points[current_player]
        self.assertEqual(points, expected)

    @parameterized.expand([
        (True, 1, 2, [1, 2, 3],
            {BLACK: 3, WHITE: 2},
            {BLACK: 1, WHITE: 0}, 20, BLACK, message),
        (False, 3, 5, [3, 5, 15],
            {BLACK: 15, WHITE: 2},
            {BLACK: 1, WHITE: 0}, 20, BLACK, next_turn_message_B),
        (False, 3, 5, [3, 5, 15],
            {BLACK: 10, WHITE: 15},
            {BLACK: 1, WHITE: 0}, 20, BLACK, next_turn_message_W),
        (False, 3, 5, [3, 5, 15],
            {BLACK: 15, WHITE: 15},
            {BLACK: 1, WHITE: 0}, 20, WHITE, next_turn_message_TIE),
    ])
    def test_next_turn(self, is_active, first_dice, second_dice, move_options,
                       points, captured, turn, current_player, expected):
        self.backgammon.active_game = is_active
        self.backgammon._turn = current_player
        self.backgammon.dice_one = first_dice
        self.backgammon.dice_two = second_dice
        self.backgammon.points = points
        self.backgammon.expelled = captured
        self.backgammon.move_options = move_options
        self.backgammon.current_turn = turn
        result = self.backgammon.next_turn()
        self.assertEqual(result, expected)

    @parameterized.expand([  # test present_board()
        (initial_board2, presented_initial_board),
        (board_7, presented_board7),
    ])
    def test_present_board(self, board, expected):
        # self.backgammon.board = initial_board
        new_game = BackgammonGame()
        new_game.board_matrix = board
        self.assertEqual(new_game.p_board(), expected)

    @parameterized.expand([
        (board_4, WHITE, {WHITE: 2}, True),
        (board_5, WHITE, {WHITE: 2}, True),
        (board_6, BLACK, {BLACK: 2}, True),
        (board_5, BLACK, {BLACK: 2}, True),
        (board_6, BLACK, {BLACK: 0}, False),
        (board_5, WHITE, {WHITE: 0}, False),
    ])
    def test_captured_piece(self, board, current_player, captured_pieces,
                            expected):
        self.backgammon.board_matrix = board
        self.backgammon._turn = current_player
        self.backgammon.expelled = captured_pieces
        result = self.backgammon.can_insert_captured_piece()
        self.assertEqual(result, expected)

    @parameterized.expand([
        (WHITE, 1, 2, {
            0: [1, 2, 3],
            11: [12, 13, 14],
            16: [17, 18, 19],
            18: [19, 20, 21]
        }),
        (BLACK, 4, 4, {
            23: [19, 15, 11, 7],
            12: [8, 4, 0, -4],
            7: [3, -1, -5, -9],
            5: [1, -3, -7, -11]
        })
    ])
    def test_all_posible_moves(self, current_player, first_dice, second_dice, expected):
        game = BackgammonGame()
        game._turn = current_player
        game.roll_dices(first_dice, second_dice)
        posible_moves_list = game.all_moves()
        self.assertEqual(posible_moves_list, expected)

    @parameterized.expand([
        (WHITE, {
            0: [1, 2, 3],
            11: [12, 13, 14],
            16: [17, 18, 19],
            18: [19, 20, 21]
        }, board_10, [(0, 1), (0, 2), (0, 3), (11, 13), (11, 14), (16, 17), (16, 19), (18, 19), (18, 20), (18, 21)]),
        (BLACK, {
            23: [19, 15, 11, 7],
            12: [8, 4, 0],
            7: [3],
            5: [1]
        }, board_9, []),
    ])
    def test_avialable_moves(self, current_player, all_moves, board, expected):
        game = BackgammonGame()
        game._turn = current_player
        game.board_matrix = board
        with patch.object(BackgammonGame, 'all_moves', return_value=all_moves):
            result = game.available_moves()
        self.assertEqual(result, expected)

    @parameterized.expand([
        (BLACK, 23, 21, 2, 1, 'GOOD MOVE', initial_board),
        (WHITE, 0, 2, 2, 1, 'GOOD MOVE', initial_board),
        (WHITE, 0, 10, 1, 1, 'BAD MOVE', initial_board),
    ])
    def test_play(self, player, from_coor, to_coor, dice_one,
                  dice_two, expected_result, board):
        game = BackgammonGame()
        game._turn = player
        game.roll_dices(dice_one, dice_two)
        game.board_matrix = board
        result = game.play(from_coor, to_coor)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        (0, 1, "GAME OVER"),
    ])
    def test_game_over(self, from_coor, to_coor,expected_result):
        game = BackgammonGame()
        game._turn = 'WHITE'
        with patch.object(BackgammonGame, "available_moves", side_effect = ([(0, 1)], [], [])):
            result = game.play(from_coor, to_coor)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        (BLACK, 3, 3, 4, 50, 20, board_11, 'GOOD MOVE'),
        (WHITE, 1, 1, 2, 40, 2, board_11, 'GOOD MOVE')
    ])
    def test_good_capture_in_play(self, player, expelled_pieces, dice_one,
                                  dice_two, from_coor, to_coor, board,
                                  expected_result):
        game = BackgammonGame()
        game._turn = player
        game.expelled[game._turn] = expelled_pieces
        game.roll_dices(dice_one, dice_two)
        game.board_matrix = board
        result = game.play(from_coor, to_coor)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        (board_7, return_board_str())
    ])
    def test_return_board(self, board, expected):
        game = BackgammonGame()
        game.board_matrix = board
        result = game.board
        self.assertEqual(result, expected)

    @parameterized.expand([
        (WHITE, 0, 1, 1, 2, BLACK)
    ])
    def test_play_no_move_options(self, current_player, from_coor, to_coor,
                                  dice_one, dice_two, expected):
        game = BackgammonGame()
        game._turn = current_player
        game.roll_dices(dice_one, dice_two)

        with patch.object(BackgammonGame, 'available_moves', side_effect = [ [(from_coor, to_coor)] ,[], [(23,22)], ]):
            game.play(from_coor, to_coor)
            result = game._turn
            self.assertEqual(result, expected)
    
    def test_play_can_not_insert_captured(self):
        game = BackgammonGame()
        game._turn = WHITE 
        game.roll_dices(1, 2)
        game.expelled[game._turn] = 0
        result = game.play(25, 2)
        self.assertEqual(result, "BAD MOVE")
    
    @parameterized.expand([
        (WHITE, 25, False),
        (BLACK, -3, False)
    ])
    def test_can_not_capture(self, current_player, position, expected):
        game = BackgammonGame()
        game._turn = current_player
        result = game.can_capture(position)
        self.assertEqual(result, expected)

    @parameterized.expand([
        (WHITE, 23, 25, 1),
        (BLACK, 0, -2, 1)
    ])
    def test_change_position_move_off_board(self, current_player, actual_position, new_position, expected):
        self.backgammon._turn = current_player
        self.backgammon.points[self.backgammon._turn] = 0
        self.backgammon.change_position(actual_position, new_position)
        result = self.backgammon.points[self.backgammon._turn]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
