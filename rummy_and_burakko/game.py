from .player import Player
from .tile_bag import TileBag
from .board import Board
import random
import copy


class Game:

    def __init__(self, players):
        self.players = self.create_players(players)
        self.current_turn = 0
        self.tile_bag = TileBag()
        self.board = Board()

    def create_players(self, names):
        return [Player(name) for name in names]

    def distribute_tiles(self):
        self.tile_bag.assign_tiles(self.players)

    def random_order(self):
        random.shuffle(self.players)

    def next_turn(self):
        self.current_turn = (self.current_turn + 1) % len(self.players)
        self.board.current_play_score = 0
        self.players[self.current_turn].change_state()
        self.players[self.current_turn].temporary_hand()
        self.board.temp_board()

    def show_game(self):
        player = self.players[self.current_turn]
        return "\n".join([
            "Mesa",
            self.board.get_board(),
            "\nMano",
            self.players[self.current_turn].get_hand(),
            "\nFichas sueltas",
            self.board.get_reused_tiles(player.get_lenght()),
        ])

    # pass
    def make_play(self, option, args):
        options = {
            1: self.put_new_set,
            2: self.select_put_a_tile,
            3: self.board.give_one_tile_from_board,
        }
        options[option](*args)

    # Option 1
    def put_new_set(self, *indexes):
        # intercambiar indices por tiles (copiando)
        tiles = self.make_tile_array(indexes)
        # eliminar tiles respecto a los indices
        self.clean(indexes)
        # crear el set con las tiles
        self.board.place_new_set(
            tiles, self.players[self.current_turn].get_first_move()
        )

    def make_tile_array(self, indexes):
        tiles = []
        player = self.players[self.current_turn]
        max_index_hand = player.get_lenght()
        for index in indexes:

            if index < max_index_hand:
                tile = copy.deepcopy(player.get_a_tile(index))
            else:
                tile = copy.deepcopy(self.board.get_a_reused_tile(index - max_index_hand))

            tiles.append(tile)
        return tiles

    def clean(self, indexes):
        player = self.players[self.current_turn]
        max_index_hand = player.get_lenght()

        indexes = list(indexes)
        indexes.sort(reverse=True)
        for index in indexes:
            if index < max_index_hand:
                player.remove_tile(index)
            else:
                self.board.remove_reused_tile(index - max_index_hand)

    # Option 2
    def select_put_a_tile(self, my_tile, set_id, index_id):
        # search and retrieve tile
        tile = self.make_tile_array([my_tile])
        # clean tile
        self.clean([my_tile])
        # put tile
        self.board.put_a_tile(tile[0], set_id, index_id)

    def quantity_of_tiles(self):
        return self.players[self.current_turn].get_lenght()

    def end_turn(self):
        self.players[self.current_turn].change_state()
        if self.valid_turn():
            self.players[self.current_turn].change_first_move()
            self.players[self.current_turn].validate_turn()
            self.board.validate_turn()
        else:
            self.tile_bag.give_one_tile(self.players[self.current_turn])

    def valid_turn(self):
        return (
            self.validate_first_move() and
            self.players[self.current_turn].valid_hand() and
            self.board.valid_sets() and
            self.board.all_reused_tiles()
        )

    def validate_first_move(self):
        return (
            not self.players[self.current_turn].first_move or
            self.board.current_play_score >= 30
        )

    def check_is_game_alive(self):
        return self.players[self.current_turn].has_tiles()

    def get_current_player(self):
        return self.players[self.current_turn]

    def move_verification(self, option, moves):
        options = {
            1: self.valid_tiles,
            2: self.valid_input_put_a_tile,
            3: self.board.valid_set_index,
        }
        return options[option](*moves)

    def valid_tiles(self, *moves):
        loose_tiles = len(self.board.reused_tiles)
        player = self.players[self.current_turn]
        return player.valid_tiles_in_hand(loose_tiles, moves)

    def valid_input_put_a_tile(self, index_hand, set_id, set_index):
        message = self.valid_tiles(index_hand)
        # -1 so we can use the same method to validate for putting and taking a tile
        if set_index > 0:
            set_index -= 1
        message += self.board.valid_set_index(set_id, set_index)
        return message
