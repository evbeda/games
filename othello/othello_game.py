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


class Othello():

    name = 'Othello'
    input_args = 2
    input_are_ints = True

    def __init__(self):
        self.possibles_players = [PLAYER1, PLAYER2]
        self.player_turn = self.possibles_players[0]
        self._board = [
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, PLAYER2, PLAYER1, None, None, None],
            [None, None, None, PLAYER1, PLAYER2, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
        ]
        self.is_playing = True

    def get_piece_count(self, kind):
        return sum(
            [piece == kind for row in self._board for piece in row])

    def change_player(self):
        self.player_turn = self.get_opposite_piece()

    def get_opposite_piece(self):
        if self.player_turn == PLAYER1:
            return PLAYER2
        return PLAYER1

    def determine_winner(self):
        if self.get_piece_count(PLAYER2) == self.get_piece_count(PLAYER1):
            return TIE_MATCH
        if self.get_piece_count(PLAYER2) > self.get_piece_count(PLAYER1):
            return PLAYER2
        return PLAYER1

    def flip_pieces(self, coordinates):
        for row, col in coordinates:
            self._board[row][col] = self.player_turn

    def validate_move(self, row, col):
        directions = [N, NE, E, SE, S, SW, W, NW]
        flips = []
        for direction in directions:
            potential_flips = self.validate_direction(row, col, direction)
            if potential_flips:
                flips += potential_flips
        return flips

    def validate_direction(self, row, col, direction):

        direction_coordinates = {
            N: [-1, 0],
            NE: [-1, 1],
            E: [0, 1],
            SE: [1, 1],
            S: [1, 0],
            SW: [1, -1],
            W: [0, -1],
            NW: [-1, -1]
        }
        change = direction_coordinates[direction]
        pieces_available_to_flip = []
        ending_same_color = False

        while (row + change[0] >= 0 and
               row + change[0] < 8 and
               col + change[1] >= 0 and col + change[1] < 8):
            row = row + change[0]
            col = col + change[1]
            if self._board[row][col] is None:
                return []
            if self._board[row][col] == self.player_turn:
                ending_same_color = True
                break
            pieces_available_to_flip.append((row, col))

        return pieces_available_to_flip if ending_same_color else []

    def all_possible_moves(self):
        moves = {}
        positions = self.none_pos()

        for pos in positions:
            aux = self.validate_move(pos[0], pos[1])
            if aux:
                moves[(pos[0], pos[1])] = aux

        return moves

    def none_pos(self):
        pos = []
        for x, row in enumerate(self._board):
            for y, element in enumerate(row):
                if element is None:
                    pos.append((x, y))
        return pos

    # this method may be unused...
    def board_printer(self):
        list_of_the_printable_board = []
        list_of_the_printable_board.append(' 0 1 2 3 4 5 6 7   ')
        for row_count, row in enumerate(self._board):
            string_row = ''
            for element in row:
                string_row += '|'
                string_row += ' ' if element is None else element
            string_row += '| ' + str(row_count)
            list_of_the_printable_board.append(string_row)
        return list_of_the_printable_board

    @property
    def board(self):
        string_board = ' 0 1 2 3 4 5 6 7   \n'
        for row_count, row in enumerate(self._board):
            for element in row:
                string_board += '|'
                string_board += ' ' if element is None else element
            string_board += '| ' + str(row_count) + '\n'
        return string_board

    def play(self, row, col):

        move = (row, col)
        moves = self.all_possible_moves()
        # pdb.set_trace()
        if not (move in moves):
            return (f"Bad move of player {self.player_turn}. Try again")

        self.put_piece(move)
        self.flip_pieces(moves[move])

        self.change_player()

        if not self.all_possible_moves():
            self.change_player()
            if not self.all_possible_moves():
                winner = self.determine_winner()
                self.is_playing = False
                return TIE_MATCH if winner == TIE_MATCH else f"{winner} wins the match"

        return MOVE_OK

    def next_turn(self):
        if self.is_playing:
            return f"Turn of Player {self.player_turn}"
        else:
            return GAME_OVER

    def put_piece(self, coordinate):
        row, col = coordinate
        self._board[row][col] = self.player_turn
