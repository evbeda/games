from random import randint
from game_base import GameBase


class FourNumber(GameBase):
    name = 'Four number'
    input_args = 1

    def __init__(self):
        super(FourNumber, self).__init__()
        self.chose_number = self.chose_valid_number()

    def next_turn(self):
        if self.is_playing:
            return 'Enter a four-digit number'
        else:
            return 'Game over'

    def chose_valid_number(self):
        num = randint(102, 9876)
        if self.valid_number(num):
            return num
        else:
            return self.chose_valid_number()

    def valid_number(self, number):
        list_num = [int(x) for x in str(number).zfill(4)]
        if set([x for x in list_num if list_num.count(x) > 1]) == set():
            return True
        else:
            return False

    def same_enter_number(self, number):
        if number in range(102, 9876):
            if self.valid_number(number):
                return 'valid number'
            else:
                return 'invalid number'
        else:
            return 'invalid number'

    def play(self, number):
        if (self.is_playing):
            if self.same_enter_number(number) == 'invalid number':
                return 'invalid number'
            else:
                list_num = [int(x) for x in str(number).zfill(4)]
                list_num_chose = [int(x)
                                  for x in str(self.chose_number).zfill(4)]
            if (list_num == list_num_chose):
                self.finish()
                return '4G, You win'
            else:
                counterG = 0
                counterR = 0
                for x in range(4):
                    for y in range(4):
                        if list_num[x] == list_num_chose[y]:
                            if x == y:
                                counterG += 1
                            else:
                                counterR += 1
                if counterG > 0 and counterR > 0:
                    return '{}G {}R'.format(counterG, counterR)

                if counterG > 0 and counterR == 0:
                    return '{}G'.format(counterG)

                if counterR > 0 and counterG == 0:
                    return '{}R'.format(counterR)

                return '0 coincidence'

    @property
    def board(self):
        return ''
