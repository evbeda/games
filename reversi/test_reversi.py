import unittest
from ReversiGame import ReversiGame


class TestReversi(unittest.TestCase):

    def setUp(self):
        self.game = ReversiGame()

    def test_initial_status(self):
        self.assertTrue(self.game.playing)
        self.assertEquals(self.game.tablero[3][3], 'B')
        self.assertEquals(self.game.tablero[3][4], 'W')
        self.assertEquals(self.game.tablero[4][3], 'W')
        self.assertEquals(self.game.tablero[4][4], 'B')

    def test_initial_next_turn_whites(self):
        self.assertEquals(
            self.game.next_turn(),
            'Turn of the whiteones',
        )

    def test_wrong_movement_empty(self):
        self.assertEquals(self.game.play(1, 1), 'Movimiento no permitido')

    def test_wrong_movement_occupied(self):
        self.assertEquals(self.game.play(3, 4), 'Movimiento no permitido')


    def test_valid_move(self):
        self.assertEquals(self.game.play(3, 5), 'Correcto')

    # # Solucionar: es un movimiento incorrecto, pero devuelve correcto
    # def test_valid_move_2(self):
    #     self.assertEquals(self.game.play(4, 5), 'Movimiento no permitido')

    # def test_get_directions(self):
    #     # las tuplas representan la cantidad de casilleros en una direccion
    #     # y que ficha contiene ese casillero
    #     # las listas representan las direcciones posibles para mover la ficha
    #     # se pretende ordenar, primero la direccion vertical superior
    #     #  en sentido horario
    #     # Por cada lista hay que evaluar si es correcto o incorrecto el
    #     # movimiento dependiendo del turno
    #     self.assertEquals(self.game.get_directions(4,5),
    #         [(4,4,'B'),(4,3,'W')],
    #         [(4,3,'W')]
    #         )


if __name__ == "__main__":
        unittest.main()
