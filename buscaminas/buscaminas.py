from random import randint
from game_base import GameBase
#fixme-buscaminas-1: add GameWithBoard import

#fixme-buscaminas-1: add GameWithBoard import inheritance
class Buscaminas(GameBase):
    name = 'Buscaminas'
    input_args = 2
    #fixme-buscaminas-2: overwrite GameWithBoard attributes

    def __init__(self):
        super(Buscaminas, self).__init__()
        #fixme-buscaminas-3: remove max, min, pos_x, pos_y
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
        #fixme-buscaminas-7: need to create board before insert bombs in it
        self.generate_bombs()
        # fixme-20: you don't need this... use: self._board
        self.possible_clicks()

    #fixme-buscaminas-4: dont overwrite this, it's already inside GameWithBoard
    def in_board(self, x, y):
        return not(
            self.max <= x or
            self.min > x or
            self.max <= y or
            self.min > y
        )

    def next_turn(self):
        if self.is_playing:
            return "Play"
        else:
            return '*********** Game Over ************'

    def check_lose(self, x, y):
        if (x, y,) in self.bombs:
            #fixme-buscaminas-5: call 'set_value' method from parent
            self._board[x][y] = "*"
            return True
        return False

    def check_win(self):
        if self.number_clicks == (self.number_blocks - len(self.bombs)):
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
        #fixme-buscaminas-6: call 'set_value' method from parent
        self._board[x][y] = str(self.count)

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
                if self.check_win():
                    self.finish()
                    return '*********** You Win ***********'

                self.keep_playing(x, y, movements)

                return 'Keep playing'
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
        #fixme-buscaminas-10: use rows and columns instead
        return (randint(0, self.max - 1), randint(0, self.max - 1),)

    #fixme-buscaminas-7: confusing name
    def generate_board(self):
        self.clear_board()
        for (x, y, ) in self.bombs:
            #fixme-buscaminas-8: need to cal 'set_value' method from parent
            self._board[x][y] = 'B'

    #fixme-buscaminas-9:  delete clear board, only use 'create_board' from parent ONCE
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
        #fixme-buscaminas-10: use rows and columns instead
        for x in range(self.max):
            for y in range(self.max):
                self.clicks.append((x, y, ))
        return self.clicks

    #fixme-buscaminas-11: delete this, used 'get_board' form parent
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
        #fixme-buscaminas-10: use rows and columns instead
        for y in range(0, self.max):
            for x in range(0, self.max):
                #fixme-buscaminas-12: use 'get_value' from parent
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
