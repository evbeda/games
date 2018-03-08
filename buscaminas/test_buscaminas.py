import unittest
from buscaminas import Buscaminas


class TestBuscamina(unittest.TestCase):

    def setUp(self):
        self.game = Buscaminas()
        self.game.bombs = [
            (1, 1, ), (2, 4, ), (1, 2, ),
            (3, 4, ), (4, 3, ), (2, 1, ),
            (5, 3, ), (3, 5, ), (6, 1, ),
            (7, 2, ),
        ]
        #fixme-buscaminas-13: no need to call it from here
        self.game.generate_board()

    def test_initial_status(self):
        self.game.bombs = []
        self.assertTrue(self.game.is_playing)
        self.assertEqual(10, self.game.generate_bombs())

    def test_check_lose(self):
        buscaminas = Buscaminas()
        buscaminas.bombs = [(2, 2,)]
        # fixme-26:
        self.assertTrue(buscaminas.check_lose(2, 2))
        self.assertFalse(buscaminas.check_lose(1, 2))

    def test_check_win(self):
        mock_bomb = [(2, 2,), (1, 1,)]
        buscaminas = Buscaminas()
        self.assertTrue(buscaminas.check_win(1, 3, mock_bomb))
        self.assertFalse(buscaminas.check_win(2, 3, mock_bomb))

    def test_check_keep_playing(self):
        buscaminas = Buscaminas()
        buscaminas.clicks = [(1, 1,), (1, 2,)]
        buscaminas.number_clicks = 0
        buscaminas.count = 0
        mock_movements = [True, False, True]

        buscaminas.keep_playing(1, 1, mock_movements)
        self.assertEqual(1, len(buscaminas.clicks))
        self.assertEqual((1, 2,), buscaminas.clicks[0])
        self.assertEqual(1, buscaminas.number_clicks)
        self.assertEqual(2, buscaminas.count)
        self.assertEqual("2", buscaminas._board[1][1])
        self.assertEqual("Keep playing", self.game.play(2, 2))

    def test_board(self):
        result = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', 'B', 'B', ' ', ' ', ' ', ' ', ' '],
            [' ', 'B', ' ', ' ', 'B', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', 'B', 'B', ' ', ' '],
            [' ', ' ', ' ', 'B', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', 'B', ' ', ' ', ' ', ' '],
            [' ', 'B', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'B', ' ', ' ', ' ', ' ', ' '],
        ]

        self.assertEqual(result, self.game.check_board())

    def test_click(self):
        result = [
            (0, 0, ), (0, 1, ), (0, 2, ),
            (0, 3, ), (0, 4, ), (0, 5, ),
            (0, 6, ), (0, 7, ), (1, 0, ),
            (1, 1, ), (1, 2, ), (1, 3, ),
            (1, 4, ), (1, 5, ), (1, 6, ),
            (1, 7, ), (2, 0, ), (2, 1, ),
            (2, 2, ), (2, 3, ), (2, 4, ),
            (2, 5, ), (2, 6, ), (2, 7, ),
            (3, 0, ), (3, 1, ), (3, 2, ),
            (3, 3, ), (3, 4, ), (3, 5, ),
            (3, 6, ), (3, 7, ), (4, 0, ),
            (4, 1, ), (4, 2, ), (4, 3, ),
            (4, 4, ), (4, 5, ), (4, 6, ),
            (4, 7, ), (5, 0, ), (5, 1, ),
            (5, 2, ), (5, 3, ), (5, 4, ),
            (5, 5, ), (5, 6, ), (5, 7, ),
            (6, 0, ), (6, 1, ), (6, 2, ),
            (6, 3, ), (6, 4, ), (6, 5, ),
            (6, 6, ), (6, 7, ), (7, 0, ),
            (7, 1, ), (7, 2, ), (7, 3, ),
            (7, 4, ), (7, 5, ), (7, 6, ),
            (7, 7, ),
        ]
        self.assertEqual(result, self.game.possible_clicks())

    def test_two_clicks_7_7_place(self):
        self.game.play(7, 7,)

    def test_two_clicks_same_place(self):
        self.game.play(1, 3,)
        self.assertEqual('Position selected yet', self.game.play(1, 3, ))

    def test_multiple_clicks(self):
        self.game.play(2, 2, )
        result = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', 'B', 'B', ' ', ' ', ' ', ' ', ' '],
            [' ', 'B', '3', ' ', 'B', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', 'B', 'B', ' ', ' '],
            [' ', ' ', ' ', 'B', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', 'B', ' ', ' ', ' ', ' '],
            [' ', 'B', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'B', ' ', ' ', ' ', ' ', ' '],
        ]

        self.assertEquals(result, self.game.check_board())

    def test_check_invalid_movement(self):
        with self.assertRaises(Exception) as e:
            self.game.play(-1, 8)
            self.assertEqual(e.exception.message, "Movement not allowed.",)

    def test_output_board(self):
        # result = "|1|2|2|1|0| | | |\n"
        # result += "| | |*| | | | | |\n"
        # result += "| | | | | | | | |\n"
        # result += "| | | | | | | | |\n"
        # result += "| | | | | | | | |\n"
        # result += "| | | | | | | | |\n"
        # result += "| | | | | | | | |\n"
        # result += "| | | | | | | | |\n"

        self.game.play(0, 0, )

        # Bomb
        # self.game.play(1, 1, )

        # bomb
        # self.game.play(1, 1, )
        self.game.play(1, 0, )
        self.game.play(2, 0, )
        self.game.play(3, 0, )
        self.game.play(4, 0, )
        # bomb
        self.game.play(2, 1, )

        # bomba
        self.game.play(6, 1, )

        # bomb
        # self.game.play(4, 3, )

        # bomb
        # self.game.play(2, 4, )

        # self.assertEquals(result, board_)


if __name__ == "__main__":
    unittest.main()
