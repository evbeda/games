

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

    def play(self, column):
        if(
            self.board_status[0][column] != 'W' and
            self.board_status[0][column] != 'B'
        ):
            if self.turn % 2 != 0:
                for x in xrange(3, -1, -1):
                    if self.board_status[x][column] == 'E':
                        self.board_status[x][column] = 'W'
                        break
            else:
                for x in xrange(3, -1, -1):
                    if self.board_status[x][column] == 'E':
                        self.board_status[x][column] = 'B'
                        break
            self.turn += 1
            return self.board_status
        else:
            return 'Full column'

    def playingW(self, turn):
        if self.turn % 2 != 0:
            return 'White plays'
        else:
            return 'Black plays'
