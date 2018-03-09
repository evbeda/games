class GameBase(object):

    name = 'Undefined'
    input_args = 0

    def __init__(self, *args, **kwargs):
        super(GameBase, self).__init__(*args, **kwargs)
        self._playing = True

    # @property
    # def board(self):
    #     raise NotImplementedError("Subclass should implement this!")

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
    cols = 0
    rows = 0

    def __init__(self):
        self._board = []

    @property
    def get_board(self):
        return self._board

    def set_board(self, board):
        self._board = board

    def create_board(self, char):
        for x in xrange(self.rows):
            columns = []
            for x in xrange(self.cols):
                columns.append(char)
            self._board.append(columns)

    def get_value(self, x, y):
        return self._board[x][y]

    def set_value(self, x, y, value):
        self._board[x][y] = value

    def in_board(self, x, y):
        return self.cols > x and self.cols > y and x >= 0 and y >= 0

    def in_columns(self, *args):
        count_args = len(args)
        if count_args == 1:
            if isinstance(args, int):
                return (
                    self.minimum <= args[0] < self.cols
                )
            else:
                return False