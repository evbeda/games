RED = '\U0001F534'
BLUE = '\U0001F535'
YELLOW = '\U0001F7E1'
GREEN = '\U0001F7E2'
JOKER = ' \U0001F0DF'


class Tile():
    def __init__(self, color, number):
        self.color = color
        self.number = number
        self.is_joker = not(
            self.color != JOKER and self.number != 0
        )
        self.set_id = 0

    def assign_set_id(self, set_id):
        self.set_id = set_id

    def get_number(self):
        return self.number

    def __eq__(self, other):
        if isinstance(other, Tile):
            return self.color == other.color and self.number == other.number
