class GameBase(object):

    name = 'Undefined'
    input_args = 0

    def __init__(self, *args, **kwargs):
        super(GameBase, self).__init__(*args, **kwargs)
        self._playing = True

    @property
    def board(self):
        raise NotImplementedError("Subclass should implement this!")

    @property
    def is_playing(self):
        return self._playing

    def play(self, *args):
            return ''

    def next_turn(self):
        return ''

    def finish(self):
        self._playing = False


class GameWithTurns(object):
    player_one = 'Undefined'
    player_two = 'Undefined'

    def __init__(self, *args, **kwargs):
        super(GameWithTurns, self).__init__(*args, **kwargs)
        self._turn = self.player_one

    def change_turn(self):
        if self._turn == self.player_one:
            self._turn = self.player_two
        else:
            self._turn = self.player_one

    @property
    def actual_player(self):
        return self._turn


class GameWithBoard(object):

    minimum = 0
    _col = 0
    _row = 0

    def __init__(self):
        self._board = []

    @property
    def get_board(self):
        return self._board

    # fixme-8: char args?
    def create_board(self):
        self._board = [[''] * self._col]
        self._board = self._board * self._row

    def get_value(self, x, y):
        return self._board[x][y]

    def set_value(self, x, y, value):
        self._board[x][y] = value

    # fixme-7: separate in_board(x, y) & in_columns(col)
    def in_board(self, *args):
        count_args = len(args)
        if (count_args == 2):
            if isinstance(args, int):
                return (
                    self.minimum <= args[0] < self.col and
                    self.minimum <= args[1] < self.row
                )
            else:
                return False

    def in_columns(self, *args):
        count_args = len(args)
        if count_args == 1:
            if isinstance(args, int):
                return (
                    self.minimum <= args[0] < self.col
                )
            else:
                return False

    # fixme-8: link with create_board
    def fill_board(self, char):
        for c in range(self._col):
            for r in range(self._row):
                self._board[c][r] = char

