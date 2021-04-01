import unittest
from parameterized import parameterized
from ..spot import Spot
from ..tile import Tile


class TestSpot(unittest.TestCase):

    def test_spot_constructor(self):
        s = Spot(1, 'c')
        self.assertEqual(s.mult_value, 1)
        self.assertEqual(s.mult_type, 'c')
        self.assertEqual(s.mult_not_used, True)

    def test_set_tile(self):
        t = Tile('a')
        s = Spot(1, 'c')
        s.set_tile(t)
        self.assertEqual(s.tile.letter, t.letter)

    @parameterized.expand([
        (Spot(1, 'c'), Tile('a'), ' a '),
        (Spot(2, 'l'), None, '2xL'),
        (Spot(2, 'l'), Tile('a'), ' a '),
        (Spot(2, 'w'), None, '2xW'),
        (Spot(2, 'l'), Tile('a'), ' a '),
        (Spot(3, 'w'), None, '3xW'),
        (Spot(2, 'l'), Tile('a'), ' a '),
        (Spot(3, 'l'), None, '3xL'),
        (Spot(2, 'l'), Tile('a'), ' a '),
        (Spot(1, 'c'), None, '   '),
    ])
    def test_spot_format(self, spot, tile, expected):
        s = spot
        if tile:
            s.set_tile(tile)
        self.assertEqual(s.get_spot(), expected)

    def test_spot_eq(self):
        spot_1 = Spot(1, 'c', 3, 4)
        spot_2 = Spot(1, 'c', 3, 4)
        self.assertTrue(spot_1 == spot_2)
