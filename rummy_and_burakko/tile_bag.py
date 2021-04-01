from .tile import Tile
import itertools
import random
from .tile import BLUE
from .tile import YELLOW
from .tile import GREEN
from .tile import RED
from .tile import JOKER


class TileBag():
    def __init__(self):
        self.remaining_tiles = self.create_tiles()

    def create_tiles(self):
        temp_tiles = list(itertools.chain(
            *[[Tile(color, number) for
                color in [BLUE, RED, YELLOW, GREEN] * 2] for
                number in range(1, 14)]
        ))
        temp_tiles += [Tile(JOKER, 0), Tile(JOKER, 0)]
        return temp_tiles

    def assign_tiles(self, players):
        random.shuffle(self.remaining_tiles)
        for i in players:
            i.add_tiles(self.remaining_tiles[:13])
            self.remaining_tiles = self.remaining_tiles[13:]

    def give_one_tile(self, player):
        if len(self.remaining_tiles) > 0:
            random.shuffle(self.remaining_tiles)
            player.add_tiles([self.remaining_tiles.pop()])
        else:
            raise Exception
