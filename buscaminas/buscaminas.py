from random import randint
from game_base import GameBase


class Buscaminas(GameBase):
    name = 'Buscaminas'
    input_args = 2

    def __init__(self):
        super(Buscaminas, self).__init__()
        self.max = 8
        self.min = 0
        self.pos_x = 0
        self.pos_y = 0
        # fixme-20: you don't need this... use: self._board
        self.bombs = []
        # fixme-20: you don't need this... use: self._board
        self.number_clicks = 0
        # fixme-20: you don't need this... use: self._board
        self.number_bombs = 10
        # fixme-20: you don't need this... use: self._board
        self.number_blocks = 64
        # fixme-20: you don't need this... use: self._board
        self.clicks = []
        # fixme-25: clear_board is included in generate_bombs
        self.clear_board()
        self.generate_bombs()
        # fixme-20: you don't need this... use: self._board
        self.possible_clicks()

    def in_board(self, x, y):
        # fixme-21: no need to validate int
        if isinstance(x, int) and isinstance(y, int):
            return not(
                self.max <= x or
                self.min > x or
                self.max <= y or
                self.min > y
            )
        else:
            return False

    def next_turn(self):
        if self.is_playing:
            return "Play"
        else:
            return '*********** Game Over ************'

    def check_lose(self, x, y):
        if (x, y,) in self.bombs:
            self._board[x][y] = "*"
            return True
        return False

    # fixme-22: no need args... use object vars
    def check_win(self, number_clicks, number_blocks, bombs):
        if number_clicks == (number_blocks - len(bombs)):
            return True
        return False

    # fixme-23: just need x, y args...
    def keep_playing(self, x, y, movements):
        self.clicks.remove((x, y, ))
        self.number_clicks += 1
        self.count += sum([
            1
            for m in movements
            if m is True
        ])
        self._board[x][y] = str(self.count)
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
                if self.check_lose(x, y):
                    self.finish()
                    return '*********** You Lose ***********'
                if self.check_win(self.number_clicks, self.number_blocks, self.bombs):
                    self.finish()
                    return  '*********** You Win ***********'
                if not self.keep_playing(x, y, movements):
                    self.finish()
                # fixme-24: return ''
            else:
                return 'Position selected yet'
        else:
            return 'Movement not allowed.'

    def generate_bombs(self):
        i = 0
        j = 0
        for x in range(0, self.number_bombs):
            i, j = self.generate_random()
            while ((i, j,) in self.bombs):
                i, j = self.generate_random()
            self.bombs.append((i, j, ))
        self.generate_board()
        return len(self.bombs)

    def generate_random(self):
        return (randint(0, self.max - 1), randint(0, self.max - 1),)

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
        for x in range(self.max):
            for y in range(self.max):
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
                    # fixme-25: no need to use `x % 8` or `x % 7`...place code outside `for`
                    if x % 8 == 0:
                        output += str(y) + ' '
                    casilla = ' '
                    output += '|' + casilla
                    # fixme-25: no need to use `x % 8` or `x % 7`...place code outside `for`
                    if(x == 7):
                        output += '|' + '\n'
                elif casilla == '*':
                    # fixme-25: no need to use `x % 8` or `x % 7`...place code outside `for`
                    if x % 8 == 0:
                        output += str(y) + ' '
                    casilla = '*'
                    output += '|' + casilla
                    # fixme-25: no need to use `x % 8` or `x % 7`...place code outside `for`
                    if(x == 7):
                        output += '|' + '\n'
                else:
                    # fixme-25: no need to use `x % 8` or `x % 7`...place code outside `for`
                    if x % 8 == 0:
                        output += str(y) + ' '
                    output += '|' + casilla
                    # fixme-25: no need to use `x % 8` or `x % 7`...place code outside `for`
                    if(x == 7):
                        output += '|' + '\n'
        return output
