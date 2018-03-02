class Tateti(object):

    name = 'Tateti'
    input_args = 2

    def __init__(self):
        self.tablero = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]

        self.col = 3
        self.row = 3
        self.x = 'X'
        self.o = 'O'
        self.turn = 0
        self.playing = True
        self.winner = ""

    def next_turn(self):
        if self.playing:
            if self.turn:
                return "Plays X"
            else:
                return "Plays O"
        else:
            return self.winner

    def play(self, x1, y1):
        if self.playing:
            if isinstance(y1, int) and isinstance(x1, int):
                if self.turn == 0:
                    pieza = self.x
                    self.turn = 1
                else:
                    pieza = self.o
                    self.turn = 0

                self.insert_symbol(x1, y1, pieza)
                if(self.check_win_hor(x1, y1, pieza) or
                        self.check_win_vertical(x1, y1, pieza) or
                        self.check_diagonal_asc(x1, y1, pieza) or
                        self.check_win_diagonal_desc(x1, y1, pieza)):
                    return self.win(pieza)
                elif self.check_tie(x1, y1, pieza):
                    return self.tie(pieza)
            else:
                raise Exception("Movement not allowed.")
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

    def insert_symbol(self, x1, y1, pieza):
        if self.check_empty_position(x1, y1):
            self.tablero[x1][y1] = pieza
        else:
            raise Exception("Can't insert a symbol here")
        return self.board

    # check horizontal
    def check_win_hor(self, x1, y1, pieza):
        win = True
        for column in xrange(0, 3):
            if self.tablero[x1][column] != pieza:
                win = False
        return win

    def check_tie(self, x1, y1, pieza):
        bool = True
        for x in range(0, 3):
            for y in range(0, 3):
                if (self.tablero[x][y] == 0):
                    bool = False
        return bool

    # check vertical
    def check_win_vertical(self, x1, y1, pieza):
        win = True
        for row in xrange(0, 3):
            if self.tablero[row][y1] != pieza:
                win = False
        return win

    # check diagonal
    def check_win_diagonal_desc(self, x1, y1, pieza):
        win = True
        if(self.tablero[0][0] != pieza or
                self.tablero[1][1] != pieza or
                self.tablero[2][2] != pieza):
            win = False
        return win

    # check diagonal
    def check_diagonal_asc(self, x1, y1, pieza):
        win = True
        if(self.tablero[0][2] != pieza or
                self.tablero[1][1] != pieza or
                self.tablero[2][0] != pieza):
            win = False
        return win

    def tie(self, pieza):
        self.playing = False
        self.winner = "It's a TIE!"

    # win
    def win(self, pieza):
        self.playing = False
        self.winner = pieza + " wins"
        return self.winner
