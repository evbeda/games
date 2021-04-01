import unittest
from unittest.mock import patch
from ..set_tiles import SetTiles
from ..tile import Tile
from parameterized import parameterized
from ..tile import BLUE
from ..tile import YELLOW
from ..tile import GREEN
from ..tile import RED
from ..tile import JOKER


class TestSetTiles(unittest.TestCase):
    # Procedure test to identify a leg
    @patch.object(SetTiles, 'is_a_leg', return_value=True)   # 2 argument
    @patch.object(SetTiles, 'is_a_stair', return_value=False)  # 1 argument
    def test_valid_T_F(self, mock_stair, mock_leg):
        tiles_leg = SetTiles([])
        valid_leg = tiles_leg.is_valid()

        # assert
        self.assertTrue(valid_leg)
        mock_leg.assert_called_once_with()
        # mock_stair.assert_not_called()

    # Procedure test to identify a stair
    @patch.object(SetTiles, 'is_a_leg', return_value=False)   # 2 argument
    @patch.object(SetTiles, 'is_a_stair', return_value=True)  # 1 argument
    def test_valid_F_T(self, mock_stair, mock_leg):
        tiles_stair = SetTiles([])
        valid_stair = tiles_stair.is_valid()

        # assert
        self.assertTrue(valid_stair)
        # mock_leg.assert_called_once_with()
        mock_stair.assert_called_once_with()

    # Procedure test to dischard leg and stair
    @patch.object(SetTiles, 'is_a_leg', return_value=False)
    @patch.object(SetTiles, 'is_a_stair', return_value=False)
    def test_valid_F_F(self, mock_stair, mock_leg):
        tiles_not_set = SetTiles([])
        valid_set = tiles_not_set.is_valid()

        # assert
        self.assertFalse(valid_set)
        mock_leg.assert_called_once_with()
        mock_stair.assert_called_once_with()

    # Procedure test to approve stair
    @parameterized.expand([
        (True, ((RED, 5), (RED, 6), (RED, 7))),
        (False, ((RED, 5), (RED, 6), (RED, 8))),
        (False, ((RED, 5), (BLUE, 6), (GREEN, 5))),
        (True, ((BLUE, 1), (BLUE, 2), (BLUE, 3))),
        (True, ((JOKER, 0), (BLUE, 5), (BLUE, 6))),
        (False, ((JOKER, 0), (BLUE, 5), (BLUE, 6), (JOKER, 0))),
        (False, ((JOKER, 0), (BLUE, 5), (GREEN, 5), (JOKER, 0))),
        (False, ((RED, 5), (RED, 6))),
        (False, (
            (RED, 5), (RED, 6), (RED, 7), (RED, 5), (RED, 6),
            (RED, 7), (RED, 5), (RED, 6), (RED, 7), (RED, 5),
            (RED, 6), (RED, 7), (BLUE, 6)
        )),
        (True, ((BLUE, 1), (BLUE, 2), (JOKER, 0), (BLUE, 4), (BLUE, 5))),
        (True, ((BLUE, 1), (BLUE, 2), (BLUE, 3), (JOKER, 0), (BLUE, 5))),
        (True, ((BLUE, 1), (JOKER, 0), (BLUE, 3), (BLUE, 4), (BLUE, 5))),
        (True, ((BLUE, 2), (JOKER, 0), (BLUE, 4), (BLUE, 5), (BLUE, 6))),
    ])
    def test_is_a_stair(self, expected, tiles):
        # set variables
        tiles_stair = SetTiles([Tile(t[0], t[1]) for t in tiles])
        result = tiles_stair.is_a_stair()
        result_2 = tiles_stair.is_valid()
        # assert
        self.assertEqual(result, expected)
        self.assertEqual(result_2, expected)

    # Pocedure test to approve a leg
    @parameterized.expand([
        (True, ((RED, 5), (BLUE, 5), (GREEN, 5))),
        (False, ((RED, 5), (BLUE, 6), (GREEN, 5))),
        (False, ((RED, 5), (BLUE, 5), (BLUE, 5))),
        (True, ((JOKER, 0), (BLUE, 5), (GREEN, 5))),
        (False, ((JOKER, 0), (BLUE, 5), (GREEN, 5), (JOKER, 0))),
        (False, ((BLUE, 5), (GREEN, 5))),
        (True, ((JOKER, 0), (BLUE, 5), (GREEN, 5), (RED, 5))),
        (True, ((BLUE, 10), (GREEN, 10), (RED, 10), (JOKER, 0))),
        (False, ((JOKER, 0), (BLUE, 5), (GREEN, 5), (RED, 5), (RED, 5))),
    ])
    def test_is_a_leg(self, expected, tiles):
        # set variables
        tiles_leg = SetTiles([Tile(t[0], t[1]) for t in tiles])
        result = tiles_leg.is_a_leg()

        # assert
        self.assertEqual(result, expected)

    def test_remove_tile_from_set(self):
        t1 = Tile(RED, 3)
        t2 = Tile(BLUE, 3)
        t3 = Tile(YELLOW, 3)
        tile_set = SetTiles([t1, t2, t3])
        tile_set.remove_tile(t2)
        self.assertNotIn(t2, tile_set.tiles)

    @parameterized.expand([
        (
            SetTiles([Tile(RED, 3), Tile(BLUE, 3), Tile(YELLOW, 3)]),
            'L[ 0:{}3 1:{}3 2:{}3 ]'.format(RED, BLUE, YELLOW)
        ),
        (
            SetTiles([Tile(RED, 3), Tile(RED, 4), Tile(GREEN, 5)]),
            'Wrong[ 0:{}3 1:{}4 2:{}5 ]'.format(RED, RED, GREEN)
        ),
    ])
    def test_hand_format(self, tile_set, expected):
        self.assertEqual(tile_set.get_tiles(), expected)

    @parameterized.expand([
        (((BLUE, 1), (BLUE, 2), (BLUE, 3)), 2, (BLUE, 3)),
        (((BLUE, 1), (BLUE, 2), (BLUE, 3)), 0, (BLUE, 1)),
        (((BLUE, 1), (BLUE, 2), (BLUE, 3)), 1, (BLUE, 2)),
    ])
    def test_extract_one_tile(self, tiles, index, tile_expected):
        set_tile = SetTiles([Tile(t[0], t[1]) for t in tiles])
        temp_len = len(set_tile.tiles)
        result = set_tile.extract_one_tile(index)
        self.assertEqual(result.color, tile_expected[0])
        self.assertEqual(result.number, tile_expected[1])
        self.assertEqual(len(set_tile.tiles), temp_len - 1)

    @parameterized.expand([
        (((BLUE, 1), (BLUE, 2), (BLUE, 3)), 4),
        # ((), 4),
    ])
    def test_extract_one_tile_fail(self, tiles, index):
        set_tile = SetTiles([Tile(t[0], t[1]) for t in tiles])
        with self.assertRaises(IndexError):
            set_tile.extract_one_tile(index)

    @parameterized.expand([
        # (input_index, output_index)
        (0, 0),
        (2, 2),
        (3, 3),
        (4, 3),
    ])
    def test_put_tile(self, input_index, output_index):
        # data
        set_tile = SetTiles([Tile(RED, 3), Tile(BLUE, 3), Tile(YELLOW, 3)])
        tile = Tile(GREEN, 3)
        # process
        set_tile.put_tile(tile, input_index)
        # assert
        self.assertEqual(set_tile.tiles[output_index], tile)

    def test_get_set_value(self):
        set_tile = SetTiles([])
        result = set_tile.get_set_value()
        self.assertEqual(result, 0)

    @parameterized.expand([
        (True, True, 1, 0, 25),
        (False, True, 0, 1, 30),
        (False, False, 0, 0, 0),
    ])
    @patch.object(SetTiles, 'is_a_stair')
    @patch.object(SetTiles, 'is_a_leg')
    @patch.object(SetTiles, 'stair_value', return_value=30)
    @patch.object(SetTiles, 'leg_value', return_value=25)
    def test_get_set_value_calls(
        self,
        rv_1,
        rv_2,
        cc_1,
        cc_2,
        expected,
        mock_leg,
        mock_stair,
        mock_is_leg,
        mock_is_stair,
    ):
        # data
        set_tile = SetTiles([Tile(RED, 3)])
        mock_is_leg.return_value = rv_1
        mock_is_stair.return_value = rv_2
        # process
        result = set_tile.get_set_value()
        # assert
        self.assertEqual(mock_leg.call_count, cc_1)
        self.assertEqual(mock_stair.call_count, cc_2)
        self.assertEqual(result, expected)

    @parameterized.expand([
        # (tiles, expected)
        (((RED, 5), (BLUE, 5), (GREEN, 5)), 15),
        (((JOKER, 0), (RED, 2), (BLUE, 2)), 6),
        (((RED, 8), (BLUE, 8), (JOKER, 0)), 24),
    ])
    def test_leg_value(self, tiles, expected):
        # data
        tiles_leg = SetTiles([Tile(t[0], t[1]) for t in tiles])
        # process
        result = tiles_leg.leg_value()
        # assert
        self.assertEqual(result, expected)

    @parameterized.expand([
        # (tiles, expected)
        (((RED, 5), (RED, 6), (GREEN, 7)), 18),
        (((JOKER, 0), (RED, 10), (BLUE, 11)), 30),
        (((RED, 2), (BLUE, 3), (JOKER, 0)), 9),
        (((RED, 1), (RED, 2), (JOKER, 0), (RED, 4)), 10),
        (((RED, 1), (RED, 2), (JOKER, 0), (RED, 4), (RED, 5)), 15),
    ])
    def test_stair_value(self, tiles, expected):
        # data
        tiles_stair = SetTiles([Tile(t[0], t[1]) for t in tiles])
        # process
        result = tiles_stair.stair_value()
        # assert
        self.assertEqual(result, expected)
