from random import randint
from game_base import (
    GameBase,
    GameWithBoard,
)


class Buscaminas(GameWithBoard, GameBase):
    name = 'Buscaminas'
    input_args = 2
    cols = 8
    rows = 8
    minimum = 0
    input_are_ints = True

    def __init__(self):
        super(Buscaminas, self).__init__()
        self.number_bombs = 10
        self.create_board(' ')
        self.generate_bombs()

    def next_turn(self):
        return "Play" if self.is_playing\
            else '*********** Game Over ************'

    def check_lose(self, x, y):
        return self.get_value(x, y) == 'B'

    def check_win(self):
        return all(
            [self.get_value(col, row) != ' '
             for col in range(self.cols)
             for row in range(self.rows)]
        )

    def keep_playing(self, x, y):
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

        count_bombs = sum(
            [1
             for x1, y1 in coord
             if self.in_board(x1, y1) and self._board[x1][y1] == 'B']
        )
        self.set_value(x, y, str(count_bombs))

    def play(self, x, y):

        if self.check_win():
            self.finish()
            return '*********** You Win ***********'

        if not self.is_playing:
            return '*********** Game Over ************'

        if not self.in_board(x, y):
            return 'Movement not allowed.'

        if self.check_position_used(x, y):
            return 'Position selected yet'

        if self.check_lose(x, y):
            self.finish()
            return '*********** You Lose ***********'

        self.keep_playing(x, y)
        return 'Keep playing'

    def generate_bombs(self):
        i = 0
        j = 0
        for x in range(0, self.number_bombs):
            i, j = self.generate_random()
            self.set_value(i, j, 'B')

    def generate_random(self):
        x = randint(0, self.rows - 1)
        y = randint(0, self.cols - 1)
        return (x, y,) if self.get_value(x, y) != 'B'\
            else self.generate_random()

    def check_position_used(self, x, y):
        return self.get_value(x, y) != ' ' and self.get_value(x, y) != 'B'

    def poster(self):
        p = """
        ______ _   _ _____ _____  ___ ___  ________ _   _  ___  _____
        | ___ \\ | | /  ___/  __ \\/ _ \\|  \\/  |_   _| \\ | |/ _ \\/  ___|
        | |_/ / | | \\ `--.| /  |\\/ /_\\ \\ .  . | | | |  \\| / /_\\ \\ `--.
        | ___ \\ | | |`--. \\ |   |  _  | |\\/| | | | | . ` |  _  |`--.
        | |_/ / |_| /\\__/ / \\__/\\ | | | |  | |_| |_| |\\  | | | /\\__/ /
        \\____/ \\___/\\____/ \\____|_| |_|_|  |_/\\___/\\_| \\_|_| |_|____/ "
        """
        return p

    @property
    def board(self):
        output = self.poster()
        output = ''
        output += " x 0 1 2 3 4 5 6 7 \n"
        output += "y  \n"
        for y in range(0, self.cols):
            for x in range(0, self.rows):
                casilla = str(self.get_value(x, y))
                if x % 8 == 0:
                    output += str(y) + ' '

                if casilla == 'B':
                    casilla = ' '
                    output += '|' + casilla

                else:
                    output += '|' + casilla

                if(x == 7):
                    output += '|' + '\n'

        return output
