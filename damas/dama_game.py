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
        if not self.valid_movement_inside_board(x, y, w, z):
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
        else:
            return "This position is outside our board"

    @property
    def board(self):
        result = ''
        for x in xrange(0, 8):
            for y in xrange(0, 8):
                result += self.board_status[x][y]
            result += '\n'
        return result

    def valid_movement_inside_board(self, x1, y1, x2, y2):
        return (x1 < 0 or x1 > 7 or x2 < 0 or x2 > 7 or
                y1 < 0 or y1 > 7 or y2 < 0 or y2 > 7)

        # if self.board_status[w - 1][z - 1] == 'b':
        #     self.board_status[x][y] = ' '
        #     self.board_status[w - 1][z - 1] = ' '
        #     self.board_status[w][z] = 'w'
        #     self.turn = 'Black'
