class Tateti(object):
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

    def next(self):
        if self.playing:
            if self.turn:
                return "Plays X"
            else:
                return "Plays O"
        else:
            return "Game Over"

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

            else:
                raise Exception("Movement not allowed.")
        else:
            raise Exception("Game Over.")

    @property
    def board(self):
        return str(self.tablero)

    def check_empty_position(self, x, y):
        return self.tablero[x][y] == 0

    def insert_symbol(self, x1, y1, pieza):
        if self.check_empty_position(x1, y1):
            self.tablero[x1][y1] = pieza
        else:
            raise Exception("Can't insert a symbol here")

    # def checkTateti(self,x1,y1):
