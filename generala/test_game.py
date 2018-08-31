#from unittest.mock import patch
#from mock import patch
import mock
import unittest
from .game import Generala


class test_generala(unittest.TestCase):
    def test_game_finished_true(self):
        game = Generala("Santi", "Beto")
        game.player1.combinations = {
            'UNO': 1,
            'DOS': 2,
            'TRES': 3,
            'CUATRO': 4,
            'CINCO': 5,
            'SEIS': 6,
            'ESCALERA': 20,
            'FULL': 30,
            'POKER': 40,
            'GENERALA': 50,
            'GENERALA DOBLE': 60,
        }
        game.player2.combinations = {
            'UNO': 1,
            'DOS': 2,
            'TRES': 3,
            'CUATRO': 4,
            'CINCO': 5,
            'SEIS': 6,
            'ESCALERA': 20,
            'FULL': 30,
            'POKER': 40,
            'GENERALA': 50,
            'GENERALA DOBLE': 60,
        }
        self.assertTrue(game.finished())

    def test_game_finished_p1_false(self):
        game = Generala("Santi", "Beto")
        game.player1.combinations = {
            'UNO': '',
            'DOS': '',
            'TRES': 3,
            'CUATRO': 4,
            'CINCO': 5,
            'SEIS': 6,
            'ESCALERA': 20,
            'FULL': 30,
            'POKER': 40,
            'GENERALA': 50,
            'GENERALA DOBLE': 60,
        }
        game.player2.combinations = {
            'UNO': '',
            'DOS': '',
            'TRES': 3,
            'CUATRO': 4,
            'CINCO': 5,
            'SEIS': 6,
            'ESCALERA': 20,
            'FULL': 30,
            'POKER': 40,
            'GENERALA': 50,
            'GENERALA DOBLE': 60,
        }
        self.assertFalse(game.finished())

    def test_game_finished_p2_false(self):
        game = Generala("Santi", "Beto")
        game.player1.combinations = {
            'UNO': 3,
            'DOS': 4,
            'TRES': 3,
            'CUATRO': 4,
            'CINCO': 5,
            'SEIS': 6,
            'ESCALERA': 20,
            'FULL': 30,
            'POKER': 40,
            'GENERALA': 50,
            'GENERALA DOBLE': 60,
        }
        game.player2.combinations = {
            'UNO': '',
            'DOS': '',
            'TRES': 3,
            'CUATRO': 4,
            'CINCO': 5,
            'SEIS': 6,
            'ESCALERA': 20,
            'FULL': 30,
            'POKER': 40,
            'GENERALA': 50,
            'GENERALA DOBLE': 60,
        }
        self.assertFalse(game.finished())

    def test_game_finished_p1_servida(self):
        game = Generala("Santi", "Beto")
        game.throw.dice = [1, 1, 1, 1, 1]
        game.play('ANOTAR', 'GENERALA')
        self.assertTrue(game.finished())

    def test_game_finished_p2_servida(self):
        game = Generala("Santi", "Beto")
        game.play('ANOTAR', 'POKER')
        game.throw.dice = [1, 1, 1, 1, 1]
        game.play('ANOTAR', 'GENERALA')
        self.assertTrue(game.finished())


    #@mock.patch('builtins.input')
    @mock.patch('random.randint')
    def test_tirar_select_1(self, mock_rand_int):
        #mock_input.return_value = 1
        mock_rand_int.return_value = 1
        result = [1, 1, 1, 1, 1]
        game = Generala("Santi", "Beto")
        game.should_keep_rolling()
        game.throw.roll([0, 1, 2, 3, 4, ])
        self.assertEqual(game.throw.dice, result)

    #@mock.patch('builtins.input')
    @mock.patch('random.randint')
    def test_should_keep_rolling_possible(self, mock_rand_int):
        #mock_input.return_value = 1
        mock_rand_int.return_value = 1
        result = [1, 1, 1, 1, 1]
        game = Generala("Santi", "Beto")
        game.throw.roll([0, 1, 2, 3, 4, ])
        self.assertEqual(game.should_keep_rolling(), '{}\nTu tirada: {} \nIngrese CONSERVAR X, ANOTAR CATEGORIA\
 o TIRAR YA\nx'.format(
            game.turno.name,
            game.throw.dice,
        ))

    #@mock.patch('builtins.input')
    @mock.patch('random.randint')
    def test_should_keep_rolling_not_possible(self, mock_rand_int):
        #mock_input.return_value = 1
        mock_rand_int.return_value = 1
        game = Generala("Santi", "Beto")
        game.throw.roll([0, 1, 2, 3, 4, ])
        game.throw.number = 5
        result = game.should_keep_rolling()
        self.assertEqual(result, '{}\nTu tirada: {} \nElija la categoria\n\
                 que desea llenar (Ej: POKER, GENERALA, ETC.)'.format(game.turno.name, game.throw.dice,))

    def test_conservar_1(self):
        game = Generala("Santi", "Beto")
        game.throw.dice = [3, 5, 2, 4, 2]
        game.play('CONSERVAR', '1')
        # with mock.patch('random.randint', return_value=2):
        #     self.assertEqual(
        #         game.should_keep_rolling(),
        #         'Santi Tu tirada: [1, 2, 2, 2, 2] INGRESE CONSERVAR X, Y O ANOTAR CATEGORIA'
        #     )
        self.assertEqual(game.throw.dice[1], 5)

    #@mock.patch('builtins.input')
    @mock.patch('random.randint')
    def test_tirar_ya(self, mock_rand_int):
        #mock_input.return_value = 1
        mock_rand_int.return_value = 1
        game = Generala("Santi", "Beto")
        game.throw.dice = [3, 5, 2, 4, 2]
        game.play('TIRAR', 'YA')
        self.assertEqual(game.throw.dice, [1, 1, 1, 1, 1])

    #@mock.patch('builtins.input')
    @mock.patch('random.randint')
    def test_anotar_generala(self, mock_rand_int):
        #mock_input.return_value = 1
        mock_rand_int.return_value = 1
        game = Generala("Santi", "Beto")
        game.throw.dice = [1, 1, 1, 1, 1]
        game.throw.number = 2
        game.play('ANOTAR', 'GENERALA')
        self.assertEqual(game.player1.score, 50)
        game.play('ANOTAR', 'POKER')
        #import ipdb; ipdb.set_trace()
        self.assertEqual(
            game.play('ANOTAR', 'GENERALA'),
            'Categoria ya asignada'
        )

    def test_random_comand(self):
        game = Generala("Santi", "Beto")
        self.assertEqual(
            game.play('HOLAQUETAL', 'POKER'),
            'Ingrese ANOTAR (TIRADA), CONSERVAR (1,2..), o TIRAR',
        )

    # def test_board(self):
    #     game = Generala("Santi", "Beto")
    #     self.assertEqual(
    #         game.board(),
    #         'Santi TIENE 0 PUNTOS \nBeto TIENE 0 PUNTOS\nRONDA 1',
    #     )


if __name__ == '__main__':
    unittest.main()
