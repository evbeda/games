from unittest.mock import patch
import unittest
from .game import Generala


class test_generala(unittest.TestCase):
    def test_game_finished_true(self):
        game = Generala("Santi", "Beto")
        game.player_one.combinations = {
            'ONE': 1,
            'TWO': 2,
            'THREE': 3,
            'FOUR': 4,
            'FIVE': 5,
            'SIX': 6,
            'STAIR': 20,
            'FULL': 30,
            'POKER': 40,
            'GENERALA': 50,
            'DOUBLEGENERALA': 60,
        }
        game.player_two.combinations = {
            'ONE': 1,
            'TWO': 2,
            'THREE': 3,
            'FOUR': 4,
            'FIVE': 5,
            'SIX': 6,
            'STAIR': 20,
            'FULL': 30,
            'POKER': 40,
            'GENERALA': 50,
            'DOUBLEGENERALA': 60,
        }
        self.assertTrue(game.finished())

    def test_game_finished_p1_false(self):
        game = Generala("Santi", "Beto")
        game.player_one.combinations = {
            'ONE': '',
            'TWO': '',
            'THREE': 3,
            'FOUR': 4,
            'FIVE': 5,
            'SIX': 6,
            'STAIR': 20,
            'FULL': 30,
            'POKER': 40,
            'GENERALA': 50,
            'DOUBLEGENERALA': 60,
        }
        game.player_two.combinations = {
            'ONE': '',
            'TWO': '',
            'THREE': 3,
            'FOUR': 4,
            'FIVE': 5,
            'SIX': 6,
            'STAIR': 20,
            'FULL': 30,
            'POKER': 40,
            'GENERALA': 50,
            'DOUBLEGENERALA': 60,
        }
        self.assertFalse(game.finished())

    def test_game_finished_p2_false(self):
        game = Generala("Santi", "Beto")
        game.player_one.combinations = {
            'ONE': 3,
            'TWO': 4,
            'THREE': 3,
            'FOUR': 4,
            'FIVE': 5,
            'SIX': 6,
            'STAIR': 20,
            'FULL': 30,
            'POKER': 40,
            'GENERALA': 50,
            'DOUBLEGENERALA': 60,
        }
        game.player_two.combinations = {
            'ONE': '',
            'TWO': '',
            'THREE': 3,
            'FOUR': 4,
            'FIVE': 5,
            'SIX': 6,
            'STAIR': 20,
            'FULL': 30,
            'POKER': 40,
            'GENERALA': 50,
            'DOUBLEGENERALA': 60,
        }
        self.assertFalse(game.finished())

    def test_game_finished_p1_servida(self):
        game = Generala("Santi", "Beto")
        game.throw.dice = [1, 1, 1, 1, 1]
        game.play('CROSSOUT', 'GENERALA')
        self.assertTrue(game.finished())

    def test_game_finished_p2_servida(self):
        game = Generala("Santi", "Beto")
        game.play('CROSSOUT', 'POKER')
        game.throw.dice = [1, 1, 1, 1, 1]
        game.play('CROSSOUT', 'GENERALA')
        self.assertTrue(game.finished())

    @patch('random.randint')
    def test_tirar_select_1(self, mock_rand_int):
        mock_rand_int.return_value = 1
        result = [1, 1, 1, 1, 1]
        game = Generala("Santi", "Beto")
        game.should_keep_rolling()
        game.throw.roll([0, 1, 2, 3, 4, ])
        self.assertEqual(game.throw.dice, result)

    @patch('random.randint')
    def test_should_keep_rolling_possible(self, mock_rand_int):
        mock_rand_int.return_value = 1
        game = Generala("Santi", "Beto")
        game.throw.roll([0, 1, 2, 3, 4, ])
        self.assertEqual(game.should_keep_rolling(), '{}\nYour throw: {} \nEnter CROSSOUT (CATEGORY), KEEP\
(1,2..) or THROW NOW\n'.format(
            game.actual_player.name,
            game.throw.dice,
        ))

    @patch('random.randint')
    def test_should_keep_rolling_not_possible(self, mock_rand_int):
        mock_rand_int.return_value = 1
        game = Generala("Santi", "Beto")
        game.throw.roll([0, 1, 2, 3, 4, ])
        game.throw.number = 5
        result = game.should_keep_rolling()
        self.assertEqual(result, '{}\nYour throw: {} \nPick a category\n\
to cross out (e.g.: POKER, GENERALA, ETC.)'.format(game.actual_player.name, game.throw.dice,))

    def test_conservar_1(self):
        game = Generala("Santi", "Beto")
        game.throw.dice = [3, 5, 2, 4, 2]
        game.play('KEEP', '1')
        self.assertEqual(game.throw.dice[1], 5)

    @patch('random.randint')
    def test_tirar_ya(self, mock_rand_int):
        mock_rand_int.return_value = 1
        game = Generala("Santi", "Beto")
        game.throw.dice = [3, 5, 2, 4, 2]
        game.play('THROW', 'NOW')
        self.assertEqual(game.throw.dice, [1, 1, 1, 1, 1])

    def test_board(self):
        game = Generala("Santi", "Beto")
        self.assertEqual(
            game.board,
            'Santi HAS 0 POINTS \nBeto HAS 0 POINTS\nROUND 1',
        )

    @patch('random.randint')
    def test_anotar_generala(self, mock_rand_int):
        mock_rand_int.return_value = 1
        game = Generala("Santi", "Beto")
        game.throw.dice = [1, 1, 1, 1, 1]
        game.throw.number = 2
        game.play('CROSSOUT', 'GENERALA')
        self.assertEqual(game.player_one.score, 50)
        game.play('CROSSOUT', 'POKER')
        self.assertEqual(
            game.play('CROSSOUT', 'GENERALA'),
            '\n***That category has already been crossed out.***\n'
        )

    def test_random_comand(self):
        game = Generala("Santi", "Beto")
        self.assertEqual(
            game.play('HOLAQUETAL', 'POKER'),
            'Enter CROSSOUT (CATEGORY), KEEP (1,2..) or THROW NOW',
        )

    def test_keep_bad_comand(self):
        game = Generala("Santi", "Beto")
        self.assertEqual(
            game.play('CROSSOUT', 'WEFWEFW'),
            '\n***That category does not exist.***\n',
        )


if __name__ == '__main__':
    unittest.main()
