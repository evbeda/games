class ReversiGame(object):

    def __init__(self):
        super(ReversiGame, self).__init__()
        self.playing = True
        self.playingWhites = True

    def next_turn(self):
        if self.playing:
            if self.playingWhites:
                return 'Turn of the whiteones'
            else:
                return 'Turn of the blackones'
        else:
            return 'Game Over'

# def play(self):
