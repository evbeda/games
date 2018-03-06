class GameWithBoard(object):

    minimum = 0

    def __init__(self, col, row):
        self._col = col
        self._row = row
        self._board = []

    @property
    def get_board(self):
        return self._board

    def clear_board(self):
        del self._board[:]

    def create_board(self):
        self._board = ['' * self._col]
        self._board = self._board * self._row

    def get_value(self, x, y):
        return self._board[x][y]

    def set_value(self, x, y, value):
        self._board[x][y] = value

    def in_board(self, *args):
        count_args = len(args)

        if count_args == 1:
            if isinstance(args, int):
                return (
                    self.minimum <= args[0] < self.col
                )
            else:
                return False
        elif (count_args == 2):
            if isinstance(args, int):
                return (
                    self.minimum <= args[0] < self.col and
                    self.minimum <= args[1] < self.row
                )
            else:
                return False

    def fill_board(self, char):
        for c in range(self._col):
            for r in range(self._row):
                self._board[c][r] = char
