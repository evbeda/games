class Buscaminas(object):

    def __init__(self):
        super(Buscaminas, self).__init__()
        self.playing = True
        self.pos_x = 0
        self.pos_y = 0
        self.bombs = [(1, 1, ), (2, 4, )]

    def play(self, x, y):
        if (x, y,) in self.bombs:
            self.playing = False
            return 'You lost'
        else:
            return 'No bomb, keep going'
