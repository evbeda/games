import random
from .constants import (
    BLACK,
    WHITE,
    MESSAGE_FP,
    MESSAGE_SP,
    WINNER_BLACK,
    WINNER_WHITE,
    TIE)


class BackgammonGame():

    name = 'Backgammon'
    input_args = 2
    input_are_ints = True

    def __init__(self):

        self.board_matrix = [
            [2, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 5],
            [0, 0], [0, 3], [0, 0], [0, 0], [0, 0], [5, 0],
            [0, 5], [0, 0], [0, 0], [0, 0], [3, 0], [0, 0],
            [5, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 2]
        ]
        self.expelled = {BLACK: 0, WHITE: 0}
        self.player = random.choice([WHITE, BLACK])
        self.active_game = True
        self.dice_one = random.randint(1, 6)
        self.dice_two = random.randint(1, 6)
        self.move_options = self.get_move_options()
        self.current_turn = 1
        self.points = {BLACK: 0, WHITE: 0}
        self.is_playing = True

    def available_pieces(self, side):
        color = 0 if side == WHITE else 1
        result = []
        for index, pyramid in enumerate(self.board_matrix):
            if pyramid[color]:
                result.append(index)
        return result

    # if there are no movements, the game must finish
    def game_active_change(self):
        self.active_game = False

    # Modified dices mechanism
    def roll_dices(self):
        self.dice_one = random.randint(1, 6)
        self.dice_two = random.randint(1, 6)
        return (self.dice_one, self.dice_two)

    @property
    def move_points(self):
        '''Determines the different move options the player has, based on
        "move points", which is based on the
        rolled dices.
        returns a list of the possible moves a player can make, based only on
        the move points.'''
        if self.dice_one != self.dice_two:
            return [self.dice_one, self.dice_two]
        else:
            return [self.dice_one, self.dice_two, self.dice_one, self.dice_two]

    def get_move_options(self):
        '''Determines the move options based ONLY on the dices.
        Should be used only once per turn'''
        d1 = self.dice_one
        d2 = self.dice_two
        move_options = []
        if len(self.move_points) == 2:
            move_options = [d1, d2, d1 + d2]
            move_options = list(set(move_options))
        elif len(self.move_points) == 4:
            move_options = [d1, d1 * 2, d1 * 3, d1 * 4]
        self.move_options = move_options
        return move_options

    def update_move_options(self, move):
        '''
        Updates the move options remaining, based on the last move.
        Must not be used in the current turn if a player has made no move.
        (in that case use get_move_options() instead).
        the parameter "move" should be already validated, and must be included
        in move_options before the use of this function.
        Returns an empty array if there are no more move_options.
        '''

        self.update_move_aux1(move)

        if self.dice_one == self.dice_two and len(self.move_options) == 4:
            self.update_move_aux2(move)
        elif self.dice_one == self.dice_two and len(self.move_options) <= 3:
            self.update_move_aux3(move)

    def update_move_aux1(self, move):
        if self.dice_one != self.dice_two and len(self.move_options) > 1:
            if move == self.dice_one + self.dice_two:
                self.move_options = []
            elif move == self.dice_one:
                self.move_options = [self.dice_two]
            elif move == self.dice_two:
                self.move_options = [self.dice_one]

        elif self.dice_one != self.dice_two and len(self.move_options) <= 1:
            self.move_options = []

    def update_move_aux2(self, move):
        d1 = self.dice_one
        if len(self.move_options) == 4 and move == self.move_options[3]:
            self.move_options = []
        elif len(self.move_options) == 4 and move == self.move_options[2]:
            self.move_options = [d1]
        elif len(self.move_options) == 4 and move == self.move_options[1]:
            self.move_options = [d1, d1 * 2]
        elif len(self.move_options) == 4 and move == self.move_options[0]:
            self.move_options = [d1, d1 * 2, d1 * 3]

    def update_move_aux3(self, move):
        d1 = self.dice_one
        if len(self.move_options) == 3 and move == self.move_options[2]:
            self.move_options = []
        elif len(self.move_options) == 3 and move == self.move_options[1]:
            self.move_options = [d1]
        elif len(self.move_options) == 3 and move == self.move_options[0]:
            self.move_options = [d1, d1 * 2]

        elif len(self.move_options) == 2 and move == self.move_options[1]:
            self.move_options = []
        elif len(self.move_options) == 2 and move == self.move_options[0]:
            self.move_options = [d1]

        else:
            self.move_options = []

    @property
    def opposite(self):
        return BLACK if self.player == WHITE else WHITE

    def change_active_player(self):
        self.player = self.opposite

    def less_than_two_enemies_in_position(self, position):
        index_opp = 0 if self.opposite == WHITE else 1
        result = True if self.board_matrix[position][index_opp] < 2 else False
        return result

    def less_than_five_own_pieces(self, position):
        side = 0 if self.player == WHITE else 1
        return self.board_matrix[position][side] < 5

    def at_least_one_piece_of_the_player(self, position):
        player_piece = 0 if self.player == WHITE else 1
        if not self.board_matrix[position][player_piece]:
            return False
        return True

    def piece_move_off_board(self, final_pos):
        if ((final_pos < 0 and self.player == BLACK)
           or (final_pos > 23 and self.player == WHITE)):
            return True
        return False

    def can_insert_captured_piece(self):
        return self.expelled[self.player] > 0

    def is_valid_move(self, initial_pos, final_pos) -> bool:
        if self.piece_move_off_board(final_pos):
            return True

        enenmy_condition = self.less_than_two_enemies_in_position(final_pos)
        own_condition = (self.less_than_five_own_pieces(final_pos) and
                         self.at_least_one_piece_of_the_player(initial_pos))

        return enenmy_condition and own_condition

    def capture_opposite_piece(self, actual_position, new_position):
        inter_position_player = 0 if self.player == WHITE else 1
        inter_position_to_capture = 1 if self.player == WHITE else 0
        self.board_matrix[new_position][inter_position_to_capture] -= 1
        self.expelled[self.opposite] += 1
        self.change_position(actual_position, new_position,
                             inter_position_player)

    def change_position(self, old_position, new_position, col):
        if self.piece_move_off_board(new_position):
            self.board_matrix[old_position][col] -= 1
            self.increment_points(new_position)
            return
        if old_position < 0 or old_position > 23:
            self.board_matrix[new_position][col] += 1
            return
        self.board_matrix[old_position][col] -= 1
        self.board_matrix[new_position][col] += 1

    def can_capture(self, position):
        if self.piece_move_off_board(position):
            return False
        opposite_piece = 1 if self.player == WHITE else 0
        return self.board_matrix[position][opposite_piece] == 1

    def increment_points(self, new_position):
        if self.piece_move_off_board(new_position):
            self.points[self.player] += 1

    def make_move(self, old_position, new_position):
        col = 0 if self.player == WHITE else 1
        move = abs(new_position - old_position)
        if move in self.move_options:
            if (
                self.is_valid_move(old_position, new_position)
                and self.can_capture(new_position)
            ):
                self.capture_opposite_piece(old_position, new_position)
                self.update_move_options(move)
                return True
            elif self.is_valid_move(old_position, new_position):
                self.change_position(old_position, new_position, col)
                self.update_move_options(move)
                return True
        return False

    def check_game_status(self):
        if self.current_turn == 40:
            self.game_active_change()
        elif self.current_turn < 40 and (self.points[BLACK] == 15
                                         or self.points[WHITE] == 15):
            self.game_active_change()

    def get_current_winner(self):
        if self.points[BLACK] > self.points[WHITE]:
            return WINNER_BLACK
        elif self.points[WHITE] > self.points[BLACK]:
            return WINNER_WHITE
        else:
            return TIE

    def make_move_change_position(
        self,
        new_position,
        move,
        col
    ):
        if (
            self.less_than_five_own_pieces(new_position)
            or self.less_than_two_enemies_in_position(new_position)
        ):
            self.update_move_options(move)
            self.expelled[self.player] -= 1
            self.board_matrix[new_position][col] += 1
            self.increment_points(new_position)
            return True

    def make_move_expelled_piece(
        self,
        actual_position,
        new_position,
        move,
        col
    ):
        if move in self.move_options:
            if (
                (self.less_than_five_own_pieces(new_position)
                 or self.less_than_two_enemies_in_position(new_position))
                and self.can_capture(new_position)
            ):
                self.capture_opposite_piece(actual_position, new_position)
                self.update_move_options(move)
                self.expelled[self.player] -= 1
                return True
            else:
                self.make_move_change_position(new_position, move, col)

    def insert_captured_piece(self, new_position):
        if self.can_insert_captured_piece():
            actual_position = -1 if self.player == WHITE else 24
            col = 0 if self.player == WHITE else 1
            move = 24 - new_position if self.player == BLACK else new_position
            self.make_move_expelled_piece(actual_position, new_position,
                                          move, col)
            return True
        return False

    def next_turn(self):
        if not self.active_game:
            resume = {
                "result": self.get_current_winner(),
                "point": self.points
            }
            return f"{resume} \n GAME OVER"
        else:
            resume = {
                "dices": [self.dice_one, self.dice_two],
                "move_options": self.move_options,
                "points": self.points,
                "number_of_turns": self.current_turn,
                "piece_captured": self.expelled
            }
            return f"{self.player} turn. {resume} \n {MESSAGE_FP} {MESSAGE_SP}"

    def add_piece(self, color, iteration, position, pboard):
        line = list(pboard[iteration])
        line[position] = color
        new_line = "".join(line)
        pboard[iteration] = new_line

    def iterate(self, pieces_amount, position, pboard, index, color):
        for iter in range(pieces_amount):
            if index <= 11:
                line = 1 + iter
            else:
                line = 11 - iter
            self.add_piece(color, line, position, pboard)

    def calculate_position(self, index):
        if index <= 5:
            return -(index * 2 + 1)
        elif index <= 11:
            return -((index - 6) * 2 + 15)
        elif index <= 17:
            return (index - 12) * 2
        else:
            return (index - 18) * 2 + 14

    def p_board(self):
        aux_board = self.board_matrix[::-1]

        pboard = [
            "121314151617 181920212223",
            "| | | | | |   | | | | | |",
            "| | | | | |   | | | | | |",
            "| | | | | |   | | | | | |",
            "| | | | | |   | | | | | |",
            "| | | | | |   | | | | | |",
            "                         ",
            "| | | | | |   | | | | | |",
            "| | | | | |   | | | | | |",
            "| | | | | |   | | | | | |",
            "| | | | | |   | | | | | |",
            "| | | | | |   | | | | | |",
            "11109 8 7 6   5 4 3 2 1 0"
        ]

        for index, elem in enumerate(aux_board):
            if elem[0] > 0 or elem[1] > 0:
                color = "W" if elem[0] > elem[1] else "B"
                amount = elem[0] if color == 'W' else elem[1]
                position = self.calculate_position(index)
                self.iterate(amount, position, pboard, index, color)
        return pboard

    @property
    def board(self):
        board = ""
        for element in self.p_board():
            board += str(element) + '\n'
        return board

    def all_moves(self):
        player_position = 0 if self.player == WHITE else 1
        _all_moves = {}
        move_options = self.get_move_options()
        for index, element in enumerate(self.board_matrix):
            if element[player_position] > 0:
                _all_moves[str(index)] = list(map(
                    lambda dice:
                        dice + index if player_position == 0
                        else index - dice,
                        move_options))
        return _all_moves

    def available_moves(self):
        moves = self.all_moves()
        for key, value in moves.items():
            for position in value:
                if self.is_valid_move(int(key), position):
                    return True

        return False

    def play(self, start_coor, to_coor):
        result = 'GOOD MOVE'
        self.check_game_status()
        if not self.move_options:
            self.change_active_player()
            self.roll_dices()
            self.get_move_options()
            self.current_turn += 1
        if start_coor > 23:
            self.insert_captured_piece(to_coor)
        elif (str(start_coor) not in self.all_moves()
              or (not self.make_move(start_coor, to_coor))):
            result = 'BAD MOVE'
        if not self.available_moves():
            self.change_active_player()
            self.roll_dices()
            self.get_move_options()
            if not self.available_moves():
                self.game_active_change()
                self.next_turn()
                result = 'GAME OVER'
        return result
