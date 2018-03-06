class GameBase(object):

    name = 'Undefined'
    input_args = 0

    def __init__(self):
        super(GameBase, self).__init__()
        self._playing = True

    @property
    def board(self):
        return ''

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

    def __init__(self):
        super(GameWithTurns, self).__init__()
        self._turn = self.player_one

    def change_turn(self):
        if self._turn == self.player_one:
            self._turn = self.player_two
        else:
            self._turn = self.player_one

    @property
    def player_in_game(self):
        return self._turn
