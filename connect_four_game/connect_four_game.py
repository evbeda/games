

class ConnectFourGame(object):

    def __init__(self):
        super(ConnectFourGame, self).__init__()
        self.playing = True
        self.turn = 1
        self.ficha = ''
        self.board_status = [
            ['E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E'],
        ]

    def play(self, column):
        if(
            self.board_status[0][column] != 'W' and
            self.board_status[0][column] != 'B'
        ):
            if self.turn % 2 != 0:
                for x in xrange(5, -1, -1):
                    if self.board_status[x][column] == 'E':
                        self.board_status[x][column] = 'W'
                        self.ficha = 'W'
                        break
            else:
                for x in xrange(5, -1, -1):
                    if self.board_status[x][column] == 'E':
                        self.board_status[x][column] = 'B'
                        self.ficha = 'B'
                        break
            for x in range(6):
                for y in range(7):
                    # win oblicuo derecho
                    if(
                        self.board_status[x][y] == 'ficha' and
                        self.board_status[x + 1][y + 1] == 'ficha' and
                        self.board_status[x + 2][y + 2] == 'ficha' and
                        self.board_status[x + 2][y + 2] == 'ficha'
                    ):
                        return 'You win'
                    # win oblicuo derecho
                    elif(
                        self.board_status[x][y] == 'ficha' and
                        self.board_status[x - 1][y - 1] == 'ficha' and
                        self.board_status[x - 2][y - 2] == 'ficha' and
                        self.board_status[x - 2][y - 2] == 'ficha'
                    ):
                        return 'You win'
                    # win horizontal
                    elif(
                        self.board_status[x][y] == 'ficha' and
                        self.board_status[x][y + 1] == 'ficha' and
                        self.board_status[x][y + 2] == 'ficha' and
                        self.board_status[x][y + 2] == 'ficha'
                    ):
                        return 'You win'
                    # win vertical
                    elif(
                        self.board_status[x][y] == 'ficha' and
                        self.board_status[x + 1][y] == 'ficha' and
                        self.board_status[x + 2][y] == 'ficha' and
                        self.board_status[x + 2][y] == 'ficha'
                    ):
                        return 'You win'

            self.turn += 1
            return self.board_status
        else:
            return 'Full column'

    def playingW(self, turn):
        if self.turn % 2 != 0:
            return 'White plays'
        else:
            return 'Black plays'

    @property
    def board(self):
            result = ''
            for x in xrange(0, 6):
                for y in xrange(0, 7):
                    result += self.board_status[x][y]
                result += '\n'
            return result
