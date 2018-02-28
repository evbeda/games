from random import randint


class Buscaminas(object):

    def __init__(self):
        super(Buscaminas, self).__init__()
        self.playing = True
        self.pos_x = 0
        self.pos_y = 0
        self.bombs = []
        self.number_clicks = 0
        self.number_bombs = 10
        self.number_blocks = 64
        self.armar_tablero()

    def play(self, x, y):
        if (x, y,) in self.bombs:
            self.playing = False
            return 'You lost'
        elif self.number_clicks == (self.number_blocks - len(self.bombs)):
            self.playing = False
            return 'You win'
        else:
            self.number_clicks += 1
            return 'No bomb, keep going'

    def armar_tablero(self):
        i = 0
        j = 0
        for x in range(1, self.number_bombs - 1):
            while ((i, j,) in self.bombs):
                i = randint(1, 8)
                j = randint(1, 8)
            self.bombs.append((i, j, ))
        return len(self.bombs)
