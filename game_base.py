class GameBase(object):

    name = 'Undefined'
    input_args = 0

    def __init__(self):
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
