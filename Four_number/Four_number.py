from random import randint
#from game_base import GameBase


class FourNumber(object):
    name = 'Four_number'
    input_args = 1

    def __init__(self):
        super(FourNumber, self).__init__()
        self.chose_number = randint(102, 9876)
        self.player_ = []
        self.is_playing = True
        self.counter = 0

    def next_turn(self):
        if self.is_playing:
            return 'Enter a four-digit number'
        else:
            return 'Game over'

    def same_number(self, number):
        if (number < self.chose_number and number > self.chose_number):
            number = abs(int(number))
            d = number % 10
            while number > 9:
                number = number // 10
                if d != number % 10:
                    return False
            return True

    def valid_number(self, number):
        if not(self.same_number(number)):
            return 'invalid number'
        elif (self.same_number(number)):
            return 'valid number'

    def play(self, number):
        if (self.is_playing):
            list_num = [int(x) for x in str(number).zfill(4)]
            list_num_chose = [int(x) for x in str(self.chose_number).zfill(4)]
            if (list_num == list_num_chose):
                return '4G'
            else:
                #import ipdb; ipdb.set_trace()
                for x in range(4):
                    for y in range(4):
                        if list_num[x] == list_num_chose[y]:
                            if x == y:
                                self.counter = str(+ 1)
                                return self.counter + 'G'
                            else:
                                self.counter = str(+ 1)
                                return self.counter + 'R'

                    # self.counter = + 1
                    # return self.counter + 'R'
                # regular
