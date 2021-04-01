from .dice import Dice


class SetDices:
    def __init__(self):
        self.dices = self.create_set()

    def create_set(self):
        dices = []
        colors = ['white_1', 'white_2', 'red', 'yellow', 'blue', 'green']
        for color in colors:
            dices.append(Dice(color))
        return dices

    def roll_dices(self):
        values = {}
        for dice in self.dices:
            values[dice.color] = dice.roll_dice()
        # return values

    def get_value_of_die(self, color):
        return next(
            (die.value for die in self.dices if die.color == color),
            None
        )
