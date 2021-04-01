TILE_POINTS = (
    (list('aeoisnlrut'), 1),
    (list('dg'), 2),
    (list('cbmp'), 3),
    (list('hfvy'), 4),
    ('ch-q'.split('-'), 5),
    ('j-ll-ñ-rr-x'.split('-'), 8),
    (list('z'), 10)
)


class Tile:

    def __init__(self, letter):
        self.letter = letter
        self.score = 0
        for tiles, score in TILE_POINTS:
            if letter in tiles:
                self.score = score
                break

    def __eq__(self, other):
        if isinstance(other, Tile):
            return self.letter == other.letter
        else:
            return self.letter == other
