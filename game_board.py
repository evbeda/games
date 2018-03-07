# fixme-9: move to game_base
class GameWithBoard(object):

    minimum = 0

    # fixme-4: class var, remove args
    def __init__(self, col, row):
        # fixme-4: class var
        self._col = col
        # fixme-4: class var
        self._row = row
        self._board = []

    @property
    def get_board(self):
        return self._board

    # fixme-6: useful?
    def clear_board(self):
        del self._board[:]

    # fixme-8: char args?
    def create_board(self):
        # fixme-5: it won't work...
        self._board = ['' * self._col]
        self._board = self._board * self._row

    def get_value(self, x, y):
        return self._board[x][y]

    def set_value(self, x, y, value):
        self._board[x][y] = value

    # fixme-7: separate in_board(x, y) & in_columns(col)
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

    # fixme-8: link with create_board
    def fill_board(self, char):
        for c in range(self._col):
            for r in range(self._row):
                self._board[c][r] = char
