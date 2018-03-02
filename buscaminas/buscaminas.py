from random import randint


class Buscaminas(object):

    def __init__(self):
        super(Buscaminas, self).__init__()
        self.playing = True
        self.max = 8
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
            if self.playing:
                # self._board[x][y] = '*'
                if (x, y) in self.clicks:
                    if (x, y,) in self.bombs:
                        self.playing = False
                        self._board[x][y] = '*'
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
                        if self._board[x + 1][y] == 'B':
                            count += 1
                        if self._board[x][y + 1] == 'B':
                            count += 1
                        if self._board[x - 1][y] == 'B':
                            count += 1
                        if self._board[x][y - 1] == 'B':
                            count += 1
                        if self._board[x + 1][y + 1] == 'B':
                            count += 1
                        if self._board[x - 1][y - 1] == 'B':
                            count += 1
                        if self._board[x + 1][y - 1] == 'B':
                            count += 1
                        if self._board[x - 1][y + 1] == 'B':
                            count += 1
                        self._board[x][y] = str(count)

                        return 'No bomb, keep going'
                else:
                    return 'Position selected yet'
            else:
                return 'Game Over'
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
                self._board[x][y] = 'B'

    def clear_board(self):
        self._board = [
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
        for x in range(7):
            for y in range(7):
                self.clicks.append((x, y, ))
        return self.clicks

    def check_board(self):
        return self._board

    def poster(self):
        poster = ""
        poster += " ______ _   _ _____ _____  ___ ___  ________ _   _  ___  _____ \n"
        poster += " | ___ \ | | /  ___/  __ \/ _ \|  \/  |_   _| \ | |/ _ \/  ___|\n"
        poster += " | |_/ / | | \ `--.| /  \/ /_\ \ .  . | | | |  \| / /_\ \ `--. \n"
        poster += " | ___ \ | | |`--. \ |   |  _  | |\/| | | | | . ` |  _  |`--.  \n"
        poster += " | |_/ / |_| /\__/ / \__/\ | | | |  | |_| |_| |\  | | | /\__/ /\n"
        poster += " \____/ \___/\____/ \____|_| |_|_|  |_/\___/\_| \_|_| |_|____/ \n"
        return poster


    @property
    def board(self):
        output = self.poster()
        output += ' x   0 1 2 3 4 5 6 7 \n'
        output += 'y\n'
        for y in range(0, self.max):
            for x in range(0, self.max):

                casilla = str(self._board[x][y])
                if casilla == 'B':
                    if x % 8 == 0:
                        output += str(y) + '   '
                    casilla = ' '
                    output += '|' + casilla
                    if(x == 7):
                        output += '|' + '\n'
                elif casilla == '*':
                    if x % 8 == 0:
                        output += str(y) + '   '
                    casilla = '*'
                    output += '|' + casilla
                    if(x == 7):
                        output += '|' + '\n' + '   '
                else:
                    if x % 8 == 0:
                        output += str(y) + '   '
                    output += '|' + casilla
                    if(x == 7):
                        output += '|' + '\n'
        return output
