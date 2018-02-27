

class Buscaminas(object):

    def __init__(self):
        super(Buscaminas, self).__init__()
        self.playing = True
        self.pos_x = 0
        self.pos_y = 0
        bombs = [(1, 1, ), (2, 4, )]

    #def play(self, x, y):
