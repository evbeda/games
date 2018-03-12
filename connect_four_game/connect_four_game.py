from game_base import GameBase
from game_base import GameWithTurns
from game_base import GameWithBoard


class ConnectFourGame(GameBase, GameWithTurns, GameWithBoard):

    name = 'Cuatro en linea'
    input_args = 1
    player_one = 'White'
    player_two = 'Black'

    def __init__(self):
        super(ConnectFourGame, self).__init__()
        self.piece = ''
        self.row = 6
        self.min = 0
        self.col = 7
        self.board_status = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ]

    def play(self, column):
        if(self.in_board(column)):
            if(
                self.board_status[0][column] != 'W' and
                self.board_status[0][column] != 'B'
            ):
                self.set_piece_in_board(column)
                if self.check_win():
                    self.finish()
                    return 'You win'
                return 'Keep playing'
            elif(self.tie()):
                self.finish()
                return 'Tie'
            else:
                return 'Full column'
        else:
            return 'Movement not allowed'

    def in_board(self, column):
        # fixme-connectfour-5: Remove isinstance condition.
        # It's already checked in game.py.
        if isinstance(column, int):
            return (
                self.min <= column <= self.col
            )
        else:
            return False

    def tie(self):
        # fixme-connectfour-6: Remove not self.check_win() condition.
        # If check_win executed before 'tie()' in play() it's not necessary.
        return all([
                self.board_status[0][col] != ' '
                for col in range(self.col)
            ]) if (not self.check_win()) else False

    def set_piece_in_board(self, column):
        if self.actual_player == self.player_one:
            self.actual_piece = 'W'
        else:
            self.actual_piece = 'B'
        for x in range(5, -1, -1):
            if self.board_status[x][column] == ' ':
                self.board_status[x][column] = self.actual_piece
                self.piece = self.actual_piece
                self.change_turn()
                break

    def check_win_left_diagonal(self):
        for row in range(self.row):
            for col in range(self.col):
                if(
                    3 <= row <= 5 and 0 <= col <= 3 and
                    self.board_status[row][col] == self.piece and
                    self.board_status[row - 1][col + 1] == self.piece and
                    self.board_status[row - 2][col + 2] == self.piece and
                    self.board_status[row - 3][col + 3] == self.piece
                ):
                    return True
        return False

    def check_win_right_diagonal(self):
        for row in range(self.row):
            for col in range(self.col):
                if(
                    3 <= row <= 5 and 3 <= col <= 6 and
                    self.board_status[row][col] == self.piece and
                    self.board_status[row - 1][col - 1] == self.piece and
                    self.board_status[row - 2][col - 2] == self.piece and
                    self.board_status[row - 3][col - 3] == self.piece
                ):
                    return True
        return False

    def check_win_horizontal(self):
        for row in range(self.row):
            for col in range(self.col):
                if(
                    col <= 3 and
                    self.board_status[row][col] == self.piece and
                    self.board_status[row][col + 1] == self.piece and
                    self.board_status[row][col + 2] == self.piece and
                    self.board_status[row][col + 3] == self.piece
                ):
                    return True
        return False

    def check_win_vertical(self):
        for row in range(self.row):
            for col in range(self.col):
                if(
                    row <= 2 and
                    self.board_status[row][col] == self.piece and
                    self.board_status[row + 1][col] == self.piece and
                    self.board_status[row + 2][col] == self.piece and
                    self.board_status[row + 3][col] == self.piece
                ):
                    return True
        return False

    def poster(self):
        poster = "\n"
        poster += "   __ __  _______   ____    _____   ___________ \n"
        poster += "  / // / / ____/ | / / /   /  _/ | / / ____/   |\n"
        poster += " / // /_/ __/ /  |/ / /    / //  |/ / __/ / /| |\n"
        poster += "/__  __/ /___/ /|  / /____/ // /|  / /___/ ___ |\n"
        poster += "  /_/ /_____/_/ |_/_____/___/_/ |_/_____/_/  |_|\n"

        return poster

    def next_turn(self):
        return self.actual_player + ' plays'

    # fixme-connectfour-11: Can get better! Columns indistinguishable.
    @property
    def board(self):
        result = ''
        for x in range(self.row):
            for y in range(self.col):
                result += self.board_status[x][y]
            result += '\n'
        return result

    def check_win(self):
        return (self.check_win_left_diagonal() or
                self.check_win_right_diagonal() or
                self.check_win_horizontal() or
                self.check_win_vertical()
                )
