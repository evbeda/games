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

    def set(self, x1, y1):
        if isinstance(y1, int) and isinstance(x1, int):
            if self.turn == 0:
                pieza = 'X'
                self.turn = 1
            else:
                pieza = 'O'
                self.turn = 0

            self.tablero[x1][y1] = pieza
        else:
            raise Exception("Movmiento no permitido.")

    @property
    def board(self):
        return str(self.tablero)


