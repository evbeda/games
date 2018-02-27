

class ConnectFourGame(object):

    def __init__(self):
        super(ConnectFourGame, self).__init__()
        self.playing = True
        self.turn = 1
        self.board_status = [
            ['E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E'],
        ]

    def move(self, column):
        self.playing = True
        if self.turn % 2 != 0:
            for x in xrange(3, 0, -1):
                if self.board_status[x][column] == 'E':
                    self.board_status[x][column] = 'W'
                    break
        else:
            for x in xrange(3, 0, -1):
                if self.board_status[x][column] == 'E':
                    self.board_status[x][column] = 'B'
                    break
        print self.board_status
        self.turn += 1
        return self.board_status
