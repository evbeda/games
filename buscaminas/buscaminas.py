from random import randint


class Buscaminas(object):

    def __init__(self):
        super(Buscaminas, self).__init__()
        self.playing = True
        self.max = 7
        self.min = 0
        self.pos_x = 0
        self.pos_y = 0
        self.bombs = []
        self.number_clicks = 0
        self.number_bombs = 10
        self.number_blocks = 64
        self.clicks = []
        self.clear_board()
        self.generate_bombs()
        self.possible_clicks()

    def in_board(self, x, y):
        if isinstance(x, int) and isinstance(y, int):
            return not(
                self.max < x or
                self.min > x or
                self.max < y or
                self.min > y
            )
        else:
            return False

    def play(self, x, y):
        if self.in_board(x, y):
            if (x, y) in self.clicks:
                if (x, y,) in self.bombs:
                    self.playing = False
                    return 'You lost'
                elif self.number_clicks == (
                        self.number_blocks - len(self.bombs)
                ):
                    self.playing = False
                    return 'You win'
                else:
                    count = 0
                    self.clicks.remove((x, y, ))
                    self.number_clicks += 1
                    if self.board[x + 1][y] == 'B':
                        count += 1
                    if self.board[x][y + 1] == 'B':
                        count += 1
                    if self.board[x - 1][y] == 'B':
                        count += 1
                    if self.board[x][y - 1] == 'B':
                        count += 1
                    if self.board[x + 1][y + 1] == 'B':
                        count += 1
                    if self.board[x - 1][y - 1] == 'B':
                        count += 1
                    if self.board[x + 1][y - 1] == 'B':
                        count += 1
                    if self.board[x - 1][y + 1] == 'B':
                        count += 1
                    self.board[x][y] = str(count)

                    return 'No bomb, keep going'
            else:
                return 'esa posicion ya fue seleccionada'
        else:
            return 'Movimiento no permitido'

    def generate_bombs(self):
        i = 0
        j = 0
        for x in range(0, self.number_bombs):
            while ((i, j,) in self.bombs):
                i = randint(0, 7)
                j = randint(0, 7)
            self.bombs.append((i, j, ))
        self.generate_board()
        return len(self.bombs)

    def generate_board(self):
            self.clear_board()
            for (x, y, ) in self.bombs:
                self.board[x][y] = 'B'

    def clear_board(self):
        self.board = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ]

    def possible_clicks(self):
        self.clicks = []
        for x in xrange(7):
            for y in xrange(7):
                self.clicks.append((x, y, ))
        return self.clicks

    def check_board(self):
        return self.board









