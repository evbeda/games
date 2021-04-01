import unittest
from unittest.mock import patch
from ..player import Player
from ..tile_bag import TileBag
from parameterized import parameterized
from ..tile import BLUE
from ..tile import YELLOW
from ..tile import GREEN
from ..tile import RED
from ..tile import JOKER


class TestTileBag(unittest.TestCase):
    def setUp(self):
        self.t_bag = TileBag()
        self.players = [Player('test_1'), Player('test_2'), Player('test_3')]

    def test_create_tiles(self):
        with patch('rummy_and_burakko.tile_bag.Tile') as tile_patched:
            self.t_bag.create_tiles()

        self.assertEqual(len(self.t_bag.remaining_tiles), 106)

        tile_list = {
            RED: list(range(1, 14)),
            YELLOW: list(range(1, 14)),
            GREEN: list(range(1, 14)),
            BLUE: list(range(1, 14)),
            JOKER: [0] * 2,
        }

        for color, number_list in tile_list.items():
            for number in number_list:
                tile_patched.assert_any_call(color, number)

    # teste de mock
    @patch.object(Player, "add_tiles")
    def test_call_add_tiles_by_assign_tiles(self, mock):
        self.t_bag.assign_tiles(self.players)
        self.assertEqual(mock.call_count, 3)

    # result test
    def test_assign_tiles(self):
        # data
        q_tiles = 13
        q_starting_sack = 106
        # process
        self.assertEqual(len(self.players[0].hand), 0)
        self.assertEqual(len(self.t_bag.remaining_tiles), q_starting_sack)
        self.t_bag.assign_tiles(self.players)
        remaining = q_starting_sack - q_tiles * len(self.players)
        # assert
        self.assertEqual(len(self.players[0].hand), q_tiles)
        self.assertEqual(len(self.t_bag.remaining_tiles), remaining)

    @parameterized.expand([
        (106, 105, 1),
        (50, 49, 1),
        # (0, 0, 0)  #  esto genera un raise exception
    ])
    def test_give_one_tile(self, top, e_remaining, e_hand):
        self.t_bag.remaining_tiles = self.t_bag.remaining_tiles[:top]
        self.t_bag.give_one_tile(self.players[2])
        self.assertEqual(len(self.players[2].hand), e_hand)
        self.assertEqual(len(self.t_bag.remaining_tiles), e_remaining)

    def test_give_one_tile_fail(self):
        self.t_bag.remaining_tiles = []
        with self.assertRaises(Exception):
            self.t_bag.give_one_tile(self.players[2])
