from game_base import GameBase
from game_base import GameWithTurns

class Tateti(GameBase, GameWithTurns):

    name = 'Tateti'
    input_args = 2
    player_one = 'X'
    player_two = 'O'

    def __init__(self):
        super(Tateti, self).__init__()
        self.tablero = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]

        self.col = 3
        self.row = 3
        self.winner = ""

    def next_turn(self):
        if self.is_playing:
            return 'Plays ' + self.player_in_game
        else:
            return self.winner

    def play(self, x1, y1):
        if self.is_playing:
            if y1 >= 0 and y1 < 3 and x1 >= 0 and x1 < 3:
                if not self.insert_symbol(x1, y1):
                    return "Position already taken. Please, choose another one."
                if self.winner:
                    return self.winner
                elif self.tie:
                    return self.winner
                else:
                    return ''

                self.insert_symbol(x1, y1)
                if(self.check_win_hor(x1, y1) or
                        self.check_win_vertical(x1, y1) or
                        self.check_diagonal_asc(x1, y1) or
                        self.check_win_diagonal_desc(x1, y1)):
                    return self.win(self.player_in_game)
                elif self.check_tie(x1, y1):
                    return self.tie()
            else:
                return "Movement not allowed."
        else:
            return "Game Over."

    @property
    def board(self):
        result = '\n'
        for x in xrange(0, 3):
            for y in xrange(0, 3):
                result += str(self.tablero[x][y])
            result += '\n'
        return result

    def check_empty_position(self, x, y):
        return self.tablero[x][y] == 0

    def insert_symbol(self, x1, y1):
        if self.check_empty_position(x1, y1):
            self.tablero[x1][y1] = self.player_in_game
            if(self.check_win_hor(x1, y1) or
                self.check_win_vertical(x1, y1) or
                self.check_diagonal_asc(x1, y1) or
                self.check_win_diagonal_desc(x1, y1)
               ):
                return self.win()
            elif self.check_tie(x1, y1):
                return self.tie()
            else:
                # Cambia el turno si nadie gano o empataron
                self.change_turn()
        else:
            return False
            raise Exception("Can't insert a symbol here")
        return self.board

    # check horizontal
    def check_win_hor(self, x1, y1):
        win = True
        for column in xrange(0, 3):
            if self.tablero[x1][column] != self.player_in_game:
                win = False
        return win

    def check_tie(self, x1, y1):
        bool = True
        for x in range(0, 3):
            for y in range(0, 3):
                if (self.tablero[x][y] == 0):
                    bool = False
        return bool

    # check vertical
    def check_win_vertical(self, x1, y1):
        win = True
        for row in xrange(0, 3):
            if self.tablero[row][y1] != self.player_in_game:
                win = False
        return win

    # check diagonal
    def check_win_diagonal_desc(self, x1, y1):
        win = True
        if(self.tablero[0][0] != self.player_in_game or
                self.tablero[1][1] != self.player_in_game or
                self.tablero[2][2] != self.player_in_game):
            win = False
        return win

    # check diagonal
    def check_diagonal_asc(self, x1, y1):
        win = True
        if(self.tablero[0][2] != self.player_in_game or
                self.tablero[1][1] != self.player_in_game or
                self.tablero[2][0] != self.player_in_game):
            win = False
        return win

    def tie(self):
        self.finish()
        self.winner = "It's a TIE!"
        return self.winner

    # win
    def win(self):
        self.finish()
        self.winner = self.player_in_game + " wins"
        return self.winner
