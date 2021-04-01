from .set_tiles import SetTiles
import copy


class Board():
    def __init__(self):
        self.sets = {}
        self.temp_sets = {}
        self.last_id = 0
        self.reused_tiles = []
        self.current_play_score = 0

    def get_board(self):
        return '\n'.join([
            f'{index}: {tile_set.get_tiles()}'
            for index, tile_set in self.temp_sets.items()
        ])

    def get_reused_tiles(self, start_index):
        return '   '.join([
            f'{index}:{tile.color}{tile.number}'
            for index, tile in enumerate(self.reused_tiles, start_index)
        ])

    def temp_board(self):
        self.temp_sets = copy.deepcopy(self.sets)
        self.reused_tiles = []

    def valid_sets(self):
        return all(
            [value_set.is_valid() for value_set in self.temp_sets.values()]
        )

    def validate_turn(self):
        self.sets = copy.deepcopy(self.temp_sets)

    def give_one_tile_from_board(self, set_id, index):
        self.reused_tiles.append(
            self.temp_sets[set_id].extract_one_tile(index)
        )

    def place_new_set(self, tiles, is_first_move):
        self.last_id = self.last_id + 1
        self.temp_sets[self.last_id] = SetTiles(tiles)
        if is_first_move:
            new_set = self.temp_sets[self.last_id]
            self.current_play_score += new_set.get_set_value()

    def get_a_reused_tile(self, index):
        return self.reused_tiles[index]

    def remove_reused_tile(self, index):
        self.reused_tiles.pop(index)

    def all_reused_tiles(self):
        if len(self.reused_tiles) == 0:
            return True
        return False

    def put_a_tile(self, tile, set_id, index):
        self.temp_sets[set_id].put_tile(tile, index)

    def valid_set_index(self, set_id, index):
        message = ''
        if set_id not in self.temp_sets:
            message += 'Error, select an existing set'
        elif index >= len(self.temp_sets[set_id].tiles):
            message += 'Error, index in set to high'
        elif index < 0:
            message += 'Error, index below 0'
        return message
