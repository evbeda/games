import random


class Dice:
    def __init__(self, color):
        self.color = color
        self.value = 0

    def roll_dice(self):
        # return random.randint(1, 6)
        self.value = random.randint(1, 6)
