class DamaGameStart(object):

    def __init__(self):
        super(DamaGameStart, self).__init__()
        self.playing = True
        self.turn = 'White'
        self.board_status = [
            ['b', ' ', 'b', ' ', 'b', ' ', 'b', ' '],
            [' ', 'b', ' ', 'b', ' ', 'b', ' ', 'b'],
            ['b', ' ', 'b', ' ', 'b', ' ', 'b', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', 'w', ' ', 'w', ' ', 'w', ' ', 'w'],
            ['w', ' ', 'w', ' ', 'w', ' ', 'w', ' '],
            [' ', 'w', ' ', 'w', ' ', 'w', ' ', 'w']]

    def play(self, x, y, w, z):
        if(
            self.turn == 'White' and
            self.playing and
            self.board_status[x][y] == 'w'
        ):
                self.board_status[x][y] = ' '
                self.board_status[w][z] = 'w'
                self.turn = 'Black'
        elif(
            self.turn == 'Black' and
            self.playing and
            self.board_status[x][y] == 'b'
        ):
                self.board_status[x][y] = ' '
                self.board_status[w][z] = 'b'
                self.turn = 'White'

    @property
    def board(self):
        result = ''
        for x in xrange(0, 8):
            for y in xrange(0, 8):
                result += self.board_status[x][y]
            result += '\n'
        return result
