from game_base import GameBase
from game_base import GameWithTurns


class Tateti(GameWithTurns, GameBase):

    name = 'Tateti'
    input_args = 2
    player_one = 'X'
    player_two = 'O'

    def __init__(self, *args, **kwargs):
        super(Tateti, self).__init__(name=self.player_one, name2=self.player_two, *args, **kwargs)
        self.tablero = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]

        self.col = 3
        self.row = 3

    def next_turn(self):
        if self.is_playing:
            return 'Plays ' + self.actual_player

    def play(self, x1, y1):
        if self.is_playing:
            if y1 >= 0 and y1 < 3 and x1 >= 0 and x1 < 3:
                if not self.check_empty_position(x1, y1):
                    return "Position already taken,please, choose another one."
                self.insert_symbol(x1, y1)
                if(self.check_win(x1, y1)):
                    return self.win()
                elif self.check_tie(x1, y1):
                    return self.tie()
                else:
                    self.change_turn()
            else:
                return "Movement not allowed."
        else:
            return "Game Over."

    def check_win(self, x1, y1):
        if(self.check_win_hor(x1, y1) or
            self.check_win_vertical(x1, y1) or
            self.check_diagonal_asc(x1, y1) or
                self.check_win_diagonal_desc(x1, y1)):
            return True
        return False

    @property
    def board(self):
        result = '\n'
        for x in range(0, 3):
            for y in range(0, 3):
                result += str(self.tablero[x][y])
            result += '\n'
        return result

    def check_empty_position(self, x, y):
        return self.tablero[x][y] == 0

    def insert_symbol(self, x1, y1):
        self.tablero[x1][y1] = self.actual_player

    # check horizontal
    def check_win_hor(self, x1, y1):
        for column in range(0, 3):

            if self.tablero[x1][column] != self.actual_player:
                return False
        return True

    def check_tie(self, x1, y1):
        for x in range(0, 3):
            for y in range(0, 3):
                if (self.tablero[x][y] == 0):
                    return False
        return True

    # check vertical
    def check_win_vertical(self, x1, y1):
        for row in range(0, 3):
            if self.tablero[row][y1] != self.actual_player:
                return False
        return True

    # check diagonal
    def check_win_diagonal_desc(self, x1, y1):
        if(self.tablero[0][0] != self.actual_player or
                self.tablero[1][1] != self.actual_player or
                self.tablero[2][2] != self.actual_player):
            return False
        return True

    # check diagonal
    def check_diagonal_asc(self, x1, y1):
        if(self.tablero[0][2] != self.actual_player or
                self.tablero[1][1] != self.actual_player or
                self.tablero[2][0] != self.actual_player):
            return False
        return True

    def tie(self):
        self.finish()
        return "It's a TIE!"

    # win
    def win(self):
        self.finish()
        return self.actual_player + " wins"
