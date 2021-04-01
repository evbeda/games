import unittest
from ..player import Player
from ..tile import Tile
from parameterized import parameterized
from ..tile import BLUE
from ..tile import YELLOW
from ..tile import RED
from ..tile import JOKER


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("Pedro")

    def test_player_attributes(self):
        self.assertEqual(self.player.name, "Pedro")
        self.assertEqual(self.player.first_move, True)
        self.assertEqual(self.player.hand, [])

    def test_add_tiles_to_hand(self):
        # To hand
        self.player.add_tiles([1, 2, 5])
        [self.assertIn(tile, self.player.hand) for tile in [1, 2, 5]]

        # To temp_hand
        self.player.is_playing = True
        self.player.add_tiles([7, 8, 12, 13])
        [self.assertIn(tile, self.player.temp_hand) for tile in [7, 8, 12, 13]]

    @parameterized.expand([
        # (indexes, expected)
        (0, [2, 3, 4, 5]),
        (4, [1, 2, 3, 4]),
        (2, [1, 2, 4, 5]),
    ])
    def test_remove_tile(self, index, expected):
        # data
        self.player.temp_hand = list(range(1, 6))
        # process
        self.player.remove_tile(index)
        # assert
        self.assertEqual(self.player.temp_hand, expected)

    # def test_hand_format(self):
    #     self.player.temp_hand = [Tile(RED, 7), Tile(BLUE, 4), Tile(YELLOW, 5)]

    #     self.assertEqual(
    #         self.player.get_hand(),
    #         'Pedro> 0:{}7 1:{}4 2:{}5'.format(RED, BLUE, YELLOW)
    #     )

    @parameterized.expand([
        (
            [Tile(RED, 7), Tile(BLUE, 4), Tile(YELLOW, 5)],
            'Pedro> {}7 {}4 {}5'
            '\n'
            '        0   1   2   '.format(RED, BLUE, YELLOW),
        ),
    ])
    def test_hand_format(self, tiles, expected):
        self.player.temp_hand = [Tile(RED, 7), Tile(BLUE, 4), Tile(YELLOW, 5)]
        self.assertEqual(
            self.player.get_hand(),
            expected
        )

    @parameterized.expand([
        # temp_hand, expected
        (
            [Tile(RED, 7), Tile(BLUE, 4), Tile(YELLOW, 5), Tile(JOKER, 0)],
            False
        ),
        (
            [
                Tile(RED, 7),
                Tile(BLUE, 4),
                Tile(YELLOW, 5),
                Tile(JOKER, 0),
                Tile(RED, 13)
            ],
            False,
        ),
        ([Tile(RED, 7), Tile(BLUE, 4)], True),
        ([], True),
    ])
    def test_valid_hand(self, temp_hand, expected):
        # data
        self.player.hand = [
            Tile(RED, 7),
            Tile(BLUE, 4),
            Tile(YELLOW, 5),
            Tile(JOKER, 0)
        ]
        self.player.temp_hand = temp_hand
        # process
        result = self.player.valid_hand()
        # assert
        self.assertEqual(result, expected)

    def test_validate_turn(self):
        p = Player('jugador 1')
        p.temp_hand = [1, 2, 3]

        p.validate_turn()

        self.assertTrue(p.hand == p.temp_hand)
        self.assertFalse(p. hand is p.temp_hand)

    def test_change_state(self):
        self.assertFalse(self.player.is_playing)
        self.player.change_state()
        self.assertTrue(self.player.is_playing)

    def test_get_lenght(self):
        # data
        self.player.temp_hand = [
            Tile(RED, 7),
            Tile(BLUE, 4),
            Tile(YELLOW, 5),
            Tile(JOKER, 0),
        ]
        expected = 4
        # process
        result = self.player.get_lenght()
        # assert
        self.assertEqual(result, expected)

    def test_get_a_tile(self):
        # data
        self.player.temp_hand = [
            Tile(RED, 7),
            Tile(BLUE, 4),
            Tile(YELLOW, 5),
            Tile(JOKER, 0),
        ]
        index = 3
        expected = Tile(JOKER, 0)
        # process
        result = self.player.get_a_tile(index)
        # assert
        self.assertEqual(result, expected)

    def test_change_first_move(self):
        self.player.first_move = True
        self.player.change_first_move()
        self.assertFalse(self.player.first_move)

    @parameterized.expand([
        (
            [Tile(RED, 7), Tile(BLUE, 4), Tile(YELLOW, 5)],
            True,
        ),
        (
            [], False,
        ),
    ])
    def test_has_tiles(self, tiles, are_there_tiles):
        self.player.hand = tiles
        result = self.player.has_tiles()
        if are_there_tiles:
            self.assertTrue(result)
        else:
            self.assertFalse(result)

    @parameterized.expand([
        # (indexes, expected)
        ([5, 3, 10], True),  # All index in hand
        ([5, 3, 12], True),  # One index in the max limit in
        ([5, 3, 13], False),  # One index in the max limit out
        ([0, 4, 12], True),  # One index in the min limit in
        ([5, -1, 1], False),  # One index in the min limit out
        ([5, 1, 1], False),  # Repeated index
    ])
    def test_valid_tiles_in_hand_with_0_loose_tiles(self, indexes, expected):
        self.player.temp_hand = list(range(13))
        loose_tiles = 0
        result = self.player.valid_tiles_in_hand(loose_tiles, indexes)
        test = False if 'Error' in result else True
        self.assertEqual(test, expected)

    @parameterized.expand([
        # (indexes, expected)
        ([5, 3, 10], True),  # All index in hand
        ([5, 3, 15], True),  # One index in the max limit in
        ([5, 3, 16], False),  # One index in the max limit out
    ])
    def test_valid_tiles_in_hand_with_loose_tiles(self, indexes, expected):
        self.player.temp_hand = list(range(13))
        loose_tiles = 3
        result = self.player.valid_tiles_in_hand(loose_tiles, indexes)
        test = False if 'Error' in result else True
        self.assertEqual(test, expected)
