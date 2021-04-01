from .tile import Tile


class TileBag():

    def __init__(self):
        self.tiles = self.create_tile()

    def create_tile(self):
        letters = [
            'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a',
            'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e',
            'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o',
            'i', 'i', 'i', 'i', 'i', 'i',
            's', 's', 's', 's', 's', 's',
            'n', 'n', 'n', 'n', 'n',
            'l', 'l', 'l', 'l',
            'r', 'r', 'r', 'r', 'r',
            'u', 'u', 'u', 'u', 'u',
            't', 't', 't', 't',
            'd', 'd', 'd', 'd', 'd',
            'g', 'g',
            'c', 'c', 'c', 'c',
            'b', 'b',
            'm', 'm',
            'p', 'p',
            'h', 'h',
            'f',
            'v',
            'y',
            'ch',
            'q',
            'j',
            'll',
            'ñ',
            'rr',
            'x',
            'z',
            '*', '*',
        ]

        return [Tile(letter) for letter in letters]

    def add_tile(self, tile):
        self.tiles.append(tile)

    def draw_tile(self, index):
        return self.tiles.pop(index)
