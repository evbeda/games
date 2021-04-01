class Spot:
    def __init__(self, mult_value, mult_type, row=0, col=0):
        self.tile = None
        self.mult_value = mult_value
        self.mult_type = mult_type
        self.mult_not_used = True
        self.row = row
        self.col = col

    def set_tile(self, tile):
        self.tile = tile

    def get_spot(self):
        return (
            f' {self.tile.letter} '
            if self.tile else
            f'{self.mult_value}x{self.mult_type.upper()}'
            if self.mult_type != 'c' else '   '
        )

    def __eq__(self, other):
        if isinstance(other, Spot):
            return self.row == other.row and self.col == other.col
