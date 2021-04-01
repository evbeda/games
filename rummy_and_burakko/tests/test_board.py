import unittest
from unittest.mock import patch
from ..board import Board
from ..set_tiles import SetTiles
from ..tile import Tile
from parameterized import parameterized
from ..tile import BLUE
from ..tile import YELLOW
from ..tile import GREEN
from ..tile import RED


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    @parameterized.expand([
        (
            [
                SetTiles(
                    [Tile(RED, 5), Tile(BLUE, 6), Tile(RED, 10)]
                ),
                SetTiles(
                    [Tile(BLUE, 5), Tile(BLUE, 6), Tile(BLUE, 7)]
                ),
            ],
            False
        ),
        (
            [
                SetTiles(
                    [Tile(RED, 5), Tile(RED, 6), Tile(BLUE, 7)]
                ),
                SetTiles(
                    [Tile(BLUE, 5), Tile(BLUE, 6), Tile(BLUE, 7)]
                ),
            ],
            False
        ),
        # (
        #     [
        #         SetTiles([
        #             Tile(RED, 5),
        #             Tile(RED, 6),
        #             Tile(RED, 7)]
        #         ),
        #         SetTiles([
        #             Tile(BLUE, 10),
        #             Tile(BLUE, 11),
        #             Tile(BLUE, 12)]
        #         ),
        #         SetTiles([
        #             Tile(BLUE, 7),
        #             Tile(BLUE, 7),
        #             Tile(BLUE, 7),
        #             Tile(BLUE, 7)]
        #         ),
        #     ],
        #     True
        # ),
    ])
    def test_valid_sets(self, sets, expected):
        # data
        for id, set_tile in enumerate(sets):
            self.board.temp_sets.update({id: set_tile})
        # process
        result = self.board.valid_sets()
        # assert
        self.assertEqual(result, expected)

    def test_board_format(self):
        self.board.temp_sets = {
            1: SetTiles([Tile(RED, 5), Tile(BLUE, 5), Tile(YELLOW, 5)]),
            2: SetTiles(
                [
                    Tile(RED, 3), Tile(BLUE, 3),
                    Tile(YELLOW, 3), Tile(GREEN, 3)
                ]
            ),
            3: SetTiles(
                [
                    Tile(RED, 3), Tile(RED, 4),
                    Tile(RED, 5), Tile(RED, 6)
                ]
            ),
        }

        board_str = (
            "1: L[ 0:{}5 1:{}5 2:{}5 ]\n"
            "2: L[ 0:{}3 1:{}3 2:{}3 3:{}3 ]\n"
            "3: S[ 0:{}3 1:{}4 2:{}5 3:{}6 ]".format(
                RED,
                BLUE,
                YELLOW,
                RED,
                BLUE,
                YELLOW,
                GREEN,
                RED,
                RED,
                RED,
                RED
            )
        )

        self.assertEqual(self.board.get_board(), board_str)

    @parameterized.expand([
        (
            SetTiles(
                [Tile(RED, 3), Tile(RED, 4), Tile(RED, 5), Tile(RED, 6)]
            ),
            3,
            Tile(RED, 6)
        ),
    ])
    @patch.object(SetTiles, 'extract_one_tile', return_value=Tile(RED, 6))
    def test_give_one_tile_from_board(
        self, set_tile, index, chosen_tile, mock
    ):
        self.board.temp_sets = {
            1: set_tile,
        }
        self.board.give_one_tile_from_board(1, index)

        self.assertEqual(self.board.reused_tiles, [chosen_tile])

    def test_get_reused_tiles(self):
        # data
        self.board.reused_tiles = [Tile(RED, 3), Tile(RED, 4), Tile(RED, 5)]
        start_index = 5
        expected = '5:{}3   6:{}4   7:{}5'.format(RED, RED, RED)
        # process
        result = self.board.get_reused_tiles(start_index)
        # assert
        self.assertEqual(result, expected)

    @parameterized.expand([
        (False, 0),
        (True, 32),
    ])
    @patch.object(SetTiles, 'get_set_value', return_value=32)
    def test_place_new_set(
        self,
        is_first_move,
        current_play_score,
        m_get_set_value
    ):
        tiles_array = [
            Tile(RED, 3),
            Tile(RED, 4),
            Tile(RED, 5),
            Tile(RED, 6),
            Tile(RED, 7),
            Tile(RED, 8),
        ]
        expected_sets = {
            1: SetTiles(tiles_array)
        }
        self.board.place_new_set(tiles_array, is_first_move)
        if(is_first_move):
            m_get_set_value.assert_called_once_with()
        self.assertEqual(self.board.current_play_score, current_play_score)
        for index in range(len(tiles_array)):
            self.assertEqual(
                self.board.temp_sets[1].tiles[index],
                expected_sets[1].tiles[index]
            )

    def test_validate_turn(self):
        tiles = [Tile(RED, 3), Tile(RED, 4), Tile(RED, 5), Tile(RED, 6)]
        size = len(tiles)
        self.board.temp_sets = {1: SetTiles(tiles)}

        self.board.validate_turn()

        self.assertNotEqual(self.board.temp_board, self.board.sets)
        for i in range(size):
            self.assertEqual(
                self.board.temp_sets[1].tiles[i],
                self.board.sets[1].tiles[i]
            )

    def test_get_a_reused_tile(self):
        # data
        self.board.reused_tiles = [
            Tile(RED, 5), Tile(BLUE, 5), Tile(YELLOW, 5)
        ]
        index = 1
        expected = Tile(BLUE, 5)
        # process
        result = self.board.get_a_reused_tile(index)
        # assert
        self.assertEqual(result, expected)

    @parameterized.expand([
        # (index, expected)
        (0, [2, 3, 4, 5]),
        (4, [1, 2, 3, 4]),
        (2, [1, 2, 4, 5]),
    ])
    def test_remove_reused_tile(self, index, expected):
        # data
        self.board.reused_tiles = list(range(1, 6))
        # process
        self.board.remove_reused_tile(index)
        # assert
        self.assertEqual(self.board.reused_tiles, expected)

    @parameterized.expand([
        ([1, 2, 3], False),
        ([], True),
        ([1], False),
    ])
    def test_all_reused_tiles(self, lenght, expected):
        self.board.reused_tiles = lenght
        result = self.board.all_reused_tiles()
        self.assertEqual(result, expected)

    @patch.object(SetTiles, 'put_tile')
    def test_put_a_tile_calls(self, mock):
        tile = Tile(RED, 5)
        set_id = 1
        index = 3
        self.board.temp_sets = {
            1: SetTiles([Tile(RED, 3), Tile(RED, 4), Tile(RED, 5), Tile(RED, 6)])
        }
        self.board.put_a_tile(tile, set_id, index)
        mock.assert_called_once_with(tile, index)

    @parameterized.expand([
        # (set_id, index, expected)
        (1, 3, True),  # Valid set, in the valid max index
        (1, 4, False),  # Valid set, in the invalid max index
        (3, 1, False),  # non-existent set
        (2, 0, True),  # Valid set, valid index 0
        (2, -1, False),  # Valid set, invalid index below 0
    ])
    def test_valid_set_index(self, set_id, index, expected):
        self.board.temp_sets = {
            1: SetTiles([Tile(RED, 3), Tile(RED, 4), Tile(RED, 5), Tile(RED, 6)]),
            2: SetTiles([Tile(RED, 7), Tile(BLUE, 7), Tile(GREEN, 7)]),
        }
        message = self.board.valid_set_index(set_id, index)
        result = True if 'Error' not in message else False
        self.assertEqual(result, expected)
