from ..score import Score
from ..spot import Spot
from ..tile import Tile
from ..board import Board
import unittest
from unittest.mock import patch
from parameterized import parameterized
from copy import deepcopy


class TestScore(unittest.TestCase):

    def setUp(self):
        self.b = Board()

    @parameterized.expand([
        (
            [
                (1, 'c', False),
            ],
            'a',
            1,
        ),
        (
            [
                (1, 'c', False),
                (1, 'c', False),
                (1, 'c', False),
                (2, 'l', True),
            ],
            'hola',
            8,
        ),
        (
            [
                (1, 'c', False),
                (1, 'c', False),
                (1, 'c', False),
                (2, 'w', True),
            ],
            'hola',
            14,
        ),
        (
            [
                (1, 'c', False),
                (1, 'c', False),
                (1, 'c', False),
                (2, 'w', False),
            ],
            'hola',
            7,
        ),
        (
            [
                (1, 'c', True),
                (1, 'c', False),
                (1, 'c', False),
                (2, 'w', False),
            ],
            'hola',
            7,
        ),
    ])
    def test_multiply_score(self, spot_values, word, expected):
        spots = []
        for m_value, m_type, m_not_used in spot_values:
            spot = Spot(m_value, m_type)
            spot.mult_not_used = m_not_used
            spots.append(spot)

        for spot, letter in zip(spots, word):
            spot.set_tile(Tile(letter))

        score = Score.multiply_score(spots)
        self.assertEqual(score, expected)

        for spot in spots:
            self.assertEqual(spot.mult_not_used, False)

    @parameterized.expand([
        ('hola', 6, 7),
    ])
    @patch.object(Score, 'search_horiz_word')
    def test_search_horiz_letter(self, word, row, col, mock_search_horiz_word):
        self.b.spots[6][7].set_tile(Tile('h'))
        self.b.spots[7][7].set_tile(Tile('o'))
        self.b.spots[8][7].set_tile(Tile('l'))
        self.b.spots[9][7].set_tile(Tile('a'))
        self.b.spots[7][6].set_tile(Tile('r'))
        self.b.spots[9][8].set_tile(Tile('r'))
        Score.search_horiz_letter(word, row, col, self.b.spots)
        mock_search_horiz_word.assert_called()

    @parameterized.expand([
        ('hola', 6, 7),
    ])
    @patch.object(Score, 'search_vert_word')
    def test_search_vert_letter(self, word, row, col, mock_search_vert_word):
        self.b.spots[6][7].set_tile(Tile('h'))
        self.b.spots[6][8].set_tile(Tile('o'))
        self.b.spots[6][9].set_tile(Tile('l'))
        self.b.spots[6][10].set_tile(Tile('a'))
        self.b.spots[5][7].set_tile(Tile('r'))
        Score.search_vert_letter(word, row, col, self.b.spots)
        mock_search_vert_word.assert_called()

    @parameterized.expand([
        (7, 6, 'roca'),
    ])
    def test_search_horiz_word(self, row, col, expected_word):
        expected = []
        for letter in expected_word:
            spot = Spot(1, 'c')
            spot.set_tile(Tile(letter))
            expected.append(spot)
        self.b.spots[7][6] = expected[0]
        self.b.spots[7][7] = expected[1]
        self.b.spots[7][8] = expected[2]
        self.b.spots[7][9] = expected[3]
        self.assertEqual(Score.search_horiz_word(row, col, self.b.spots), expected)

    @parameterized.expand([
        (5, 7, 'roca'),
    ])
    def test_search_vert_word(self, row, col, expected_word):
        expected = []
        for letter in expected_word:
            spot = Spot(1, 'c')
            spot.set_tile(Tile(letter))
            expected.append(spot)
        self.b.spots[5][7] = expected[0]
        self.b.spots[6][7] = expected[1]
        self.b.spots[7][7] = expected[2]
        self.b.spots[8][7] = expected[3]

        self.assertEqual(Score.search_vert_word(row, col, self.b.spots), expected)

    @parameterized.expand([
        (True, True),
        (False, False),
    ])
    @patch.object(Score, 'search_horiz_letter')
    @patch.object(Score, 'search_vert_letter')
    def test_define_direction(
        self, direction, expected, mock_search_vert_letter, mock_search_horiz_letter
    ):

        Score.define_direction('word', 1, 3, direction, 'spots')
        if expected:
            mock_search_vert_letter.assert_called()
        else:
            mock_search_horiz_letter.assert_called()

    @parameterized.expand([
        (
            [
                'hola',
                'sol',
                'gato',
            ],
            15,
        ),
    ])
    @patch.object(Score, 'define_direction')
    def test_get_score(self, words_str, expected, define_direction_patched):
        words = []
        for word_str in words_str:
            word = []
            for letter in word_str:
                spot = Spot(1, 'c')
                spot.set_tile(Tile(letter))
                word.append(spot)
            words.append(word)

        with patch.object(Score, 'filter_unchanged', return_value=words):
            score = Score.get_score(
                'word',
                'col', 'row',
                'direction',
                'spots',
                'spots_orig'
            )
            self.assertEqual(score, expected)

    def test_filter_unchanged(self):
        board = Board()
        board.set_spots()
        board.spots[7][7].set_tile(Tile('h'))
        board.spots[7][8].set_tile(Tile('o'))
        board.spots[7][9].set_tile(Tile('l'))
        board.spots[7][10].set_tile(Tile('a'))
        board.spots_orig = deepcopy(board.spots)
        board.spots[6][8].set_tile(Tile('s'))
        board.spots[8][8].set_tile(Tile('l'))
        words = [
            [board.spots[row][col] for row, col in [(7, 7), (7, 8), (7, 9), (7, 10)]],
            [board.spots[row][col] for row, col in [(6, 8), (7, 8), (8, 8)]],
        ]
        changed_words = Score.filter_unchanged(words, board.spots_orig)
        expected = [
            [board.spots[row][col] for row, col in [(6, 8), (7, 8), (8, 8)]],
        ]
        self.assertEqual(changed_words, expected)
