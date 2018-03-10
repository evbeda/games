from random import randint
#from game_base import GameBase


class FourNumber(object):
    name = 'Four_number'
    input_args = 1

    def __init__(self):
        super(FourNumber, self).__init__()
        self.chose_number = randint(1000, 9999)
        self.player_ = []
        self.is_playing = True

    def next_turn(self):
        if self.is_playing:
            return 'Enter a four-digit number'
        else:
            return 'Game over'

    def valid_number(self, number):
        if (number < self.chose_number):
            return 'invalid number'
        elif (number > self.chose_number):
            return 'invalid number'

    def play(self, number):
        if (self.is_playing):
            list_num = [int(x) for x in str(number).zfill(4)]
            list_num_chose = [int(x) for x in str(self.chose_number).zfill(4)]
            if list_num == list_num_chose:
                        return '4B'
            for x in range(4):
                for y in range(4):
                    if list_num[x] == list_num_chose[y]:
                        if x == y:
                            # good
                        else:
                            # regular




