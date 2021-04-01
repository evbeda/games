import unittest
from unittest.mock import patch
from parameterized import parameterized
from ..player import Player
from ..tile_bag import TileBag
from ..tile import Tile


class TestPlayer(unittest.TestCase):
    def setUp(self):
        # data
        self.id_test = 1
        self.name_test = 'Test_1'
        self.player_test = Player(self.id_test, self.name_test)
        self.t_bag = TileBag()

    def test_player_init(self):
        self.assertEqual(self.player_test.id, self.id_test)
        self.assertEqual(self.player_test.name, self.name_test)

    def test_one_draw(self):
        # process
        self.player_test.one_draw(self.t_bag)
        # assert
        self.assertEqual(len(self.t_bag.tiles), 99)
        self.assertEqual(len(self.player_test.tiles_in_hand), 1)

    @parameterized.expand([
        (['a', 'b'], ['c'] * 100, 7, 95),
        (['a', 'b'], ['c'] * 3, 5, 0),
        (['a', 'b'], [], 2, 0),
    ])
    def test_full_draw(
        self, tiles_hand, tiles_in_bag, len_hand, len_bag,
    ):
        # data
        self.player_test.tiles_in_hand = tiles_hand
        self.t_bag.tiles = tiles_in_bag
        self.player_test.full_draw(self.t_bag)
        # assert
        self.assertEqual(len(self.player_test.tiles_in_hand), len_hand)
        self.assertEqual(len(self.t_bag.tiles), len_bag)

    @patch('random.randint')
    def test_put_t_draw_t(self, mock_random):
        # data
        hand = [Tile(x) for x in ['a', 'a', 'b', 'c', 'd', 'e', 'e']]
        self.player_test.tiles_in_hand = hand.copy()
        tiles = ['a', 'a']
        # process
        self.player_test.put_t_draw_t(self.t_bag, tiles)
        # assert
        self.assertEqual(mock_random.call_count, 2)
        self.assertEqual(len(self.player_test.tiles_in_hand), 7)

    @patch('random.randint')
    def test_one_draw_random(self, mock_random):
        # data
        start = 0
        end = len(self.t_bag.tiles) - 1
        # process
        self.player_test.one_draw(self.t_bag)
        # assert
        mock_random.assert_called_once_with(start, end)

    @patch.object(Player, 'one_draw')
    def test_full_draw_calls(self, mock_draw_one):
        # data
        self.player_test.tiles_in_hand = [3, 7, 17]
        # process
        self.player_test.full_draw(self.t_bag)
        # assert
        self.assertEqual(mock_draw_one.call_count, 4)

    @parameterized.expand([
        ('abcdefg', 'a | b | c | d | e | f | g'),
    ])
    def test_get_hand(self, letters, expected):
        self.player_test.tiles_in_hand = [
            Tile(letter) for letter in letters
        ]
        self.assertEqual(self.player_test.get_hand(), expected)

    def test_add_points(self):
        self.player_test.score = 50
        self.player_test.add_points(5)
        self.assertEqual(self.player_test.score, 55)
        self.assertEqual(self.player_test.prev_score, 50)

    def test_revert_play(self):
        self.player_test.score = 55
        self.player_test.prev_score = 50
        self.player_test.tiles_in_hand = ['a', 'b', 'c']
        self.player_test.prev_tiles_in_hand = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        self.player_test.revert_play()
        self.assertEqual(self.player_test.score, 50)
        self.assertEqual(self.player_test.tiles_in_hand, ['a', 'b', 'c', 'd', 'e', 'f', 'g'])

    def test_use_tiles(self):
        tiles = [Tile(t) for t in ['a', 'b', 'c']]
        self.player_test.tiles_in_hand = tiles.copy()
        self.player_test.use_tiles(['a', 'c'])
        self.assertEqual(self.player_test.tiles_in_hand, [Tile('b')])
        self.assertEqual(self.player_test.prev_tiles_in_hand, tiles)
