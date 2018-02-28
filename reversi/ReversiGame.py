class ReversiGame(object):

    def __init__(self):
        super(ReversiGame, self).__init__()
        self.playing = True
        self.playingBlack = True
        self.tablero = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 'B', 'W', 0, 0, 0],
            [0, 0, 0, 'W', 'B', 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]

    def next_turn(self):
        if self.playing:
            if self.playingBlack:
                return 'Turn of the whiteones'
            else:
                return 'Turn of the blackones'
        else:
            return 'Game Over'

    def validate(self, x, y):
        posibilidades = [
            (x - 1, y - 1),
            (x - 1, y),
            (x - 1, y + 1),
            (x, y - 1),
            (x, y + 1),
            (x + 1, y - 1),
            (x + 1, y),
            (x + 1, y + 1),
        ]
        count = 0
        for i in posibilidades:

            a, b = i
            casilla = self.tablero[a][b]
            if casilla == 0:
                count += 1
        if count == 8:
            return False
        else:
            return True

    def play(self, x, y):
        if not(self.validate(x, y)):
            return 'Movimiento no permitido'
