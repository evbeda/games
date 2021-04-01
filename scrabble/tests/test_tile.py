import unittest
from parameterized import parameterized

from ..tile import Tile


class TestTile(unittest.TestCase):
    def test_tile(self):
        tile = Tile('a')
        self.assertEqual(
            tile.letter,
            'a',
        )
        self.assertEqual(
            tile.score,
            1,
        )

    @parameterized.expand([
        # Letters, Score
        (['a', 'e', 'o', 'i', 's', 'n', 'l', 'r', 'u', 't'], 1),
        (['d', 'g'], 2),
        (['c', 'b', 'm', 'p'], 3),
        (['h', 'f', 'v', 'y'], 4),
        (['ch', 'q'], 5),
        (['j', 'll', 'ñ', 'rr', 'x'], 8),
        (['z'], 10),
    ])
    def test_tile_score(self, letter_list, score):
        tiles = [Tile(letter) for letter in letter_list]
        for tile in tiles:
            self.assertEqual(tile.score, score)
