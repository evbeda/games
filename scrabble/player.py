import random
from .tile import Tile


class Player:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.prev_tiles_in_hand = []
        self.tiles_in_hand = []
        self.score = 0
        self.prev_score = 0

    def one_draw(self, tiles_sack):
        index = random.randint(0, len(tiles_sack.tiles) - 1)
        tile_to_draw = tiles_sack.draw_tile(index)
        self.tiles_in_hand.append(tile_to_draw)

    def full_draw(self, tiles_sack):
        diff = 7 - len(self.tiles_in_hand)
        # Por si quedan menos fichas en el pozo que diff
        if diff > len(tiles_sack.tiles):
            diff = len(tiles_sack.tiles)
        while diff != 0:
            self.one_draw(tiles_sack)
            diff -= 1

    def put_t_draw_t(self, tiles_sack, letters):
        for letter in letters:
            tile = self.tiles_in_hand.pop(
                self.tiles_in_hand.index(Tile(letter)))
            tiles_sack.add_tile(tile)
        self.full_draw(tiles_sack)

    def get_hand(self):
        return ' | '.join([tile.letter for tile in self.tiles_in_hand])

    def add_points(self, points):
        self.prev_score = self.score
        self.score += points

    def revert_play(self):
        self.score = self.prev_score
        self.tiles_in_hand = self.prev_tiles_in_hand

    def use_tiles(self, tiles):
        self.prev_tiles_in_hand = self.tiles_in_hand.copy()
        for tile in tiles:
            self.tiles_in_hand.remove(Tile(tile))
