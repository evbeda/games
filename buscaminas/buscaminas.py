from random import randint


class Buscaminas(object):
    name = 'Buscaminas'
    input_args = 2

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

    def next_turn(self):
        if self.playing:
            return "Play"
        else:
            return '*********** Game Over ************'

    def check_lose(self, x, y, bombs):
        if (x, y,) in bombs:
            self._board[x][y] = "*"
            return True
        return False

    def check_win(self, number_clicks, number_blocks, bombs):
        if number_clicks == (number_blocks - len(bombs)):
            print "------------- You Win -------------------"
            return True
        return False

    def keep_playing(self, x, y, movements):
        self.clicks.remove((x, y, ))
        self.number_clicks += 1
        self.count += sum([
            1
            for m in movements
            if m is True
        ])
        self._board[x][y] = str(self.count)
        print 'No bomb, keep going'
        return True

    def play(self, x, y):
        self.count = 0
        coord = [
            (x + 1, y, ),
            (x, y + 1, ),
            (x - 1, y, ),
            (x, y - 1, ),
            (x + 1, y + 1, ),
            (x - 1, y - 1, ),
            (x + 1, y - 1, ),
            (x - 1, y + 1, ),
        ]
        movements = []
        for elements in coord:
            x1, y1 = elements
            if self.in_board(x1, y1):
                movements.append(self._board[x1][y1] == 'B')

        if self.in_board(x, y):
            if (x, y) in self.clicks:
                if self.check_lose(x, y, self.bombs):
                    self.playing = False
                    return "------------- You Lose -------------------"
                if self.check_win(self.number_clicks, self.number_blocks, self.bombs):
                    self.playing = False
                    return "------------- You Win -------------------"
                self.playing = self.keep_playing(x, y, movements)
            else:
                return 'Position selected yet'
        else:
            return 'Movement not allowed.'

    def generate_bombs(self):
        i = 0
        j = 0
        for x in range(0, self.number_bombs):
            i = randint(0, 7)
            j = randint(0, 7)
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
        output = ''
        output += " x 0 1 2 3 4 5 6 7 \n"
        output += "y  \n"
        for y in range(0, self.max):
            for x in range(0, self.max):
                casilla = str(self._board[x][y])
                if casilla == 'B':
                    if x % 8 == 0:
                        output += str(y) + ' '
                    casilla = ' '
                    output += '|' + casilla
                    if(x == 7):
                        output += '|' + '\n'
                elif casilla == '*':
                    if x % 8 == 0:
                        output += str(y) + ' '
                    casilla = '*'
                    output += '|' + casilla
                    if(x == 7):
                        output += '|' + '\n'
                else:
                    if x % 8 == 0:
                        output += str(y) + ' '
                    output += '|' + casilla
                    if(x == 7):
                        output += '|' + '\n'
        return output
