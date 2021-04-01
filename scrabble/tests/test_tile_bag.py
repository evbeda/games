import unittest
from ..tile_bag import TileBag
from ..tile import Tile


class TesttileBag(unittest.TestCase):

    def setUp(self):
        self.bag = TileBag()

    def test_tile_bag_attributes(self):
        t_b = TileBag()
        expected = [
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
        tiles = [tile.letter for tile in t_b.tiles]
        self.assertEqual(tiles, expected)
        self.assertEqual(len(tiles), 100)

    def test_add_tile(self):
        new_tile = Tile('z')
        self.bag.add_tile(new_tile)
        self.assertIn(new_tile, self.bag.tiles)

    def test_draw_tile(self):
        test_tile = self.bag.tiles[7]
        tile_count = self.bag.tiles.count(test_tile)
        drawn_tile = self.bag.draw_tile(7)
        self.assertEqual(self.bag.tiles.count(drawn_tile), tile_count - 1)
        # self.assertNotIn(drawn_tile, self.bag.tiles)
