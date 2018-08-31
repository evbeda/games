from .player import Player
from .utils import check_throw
from .throw import Throw
from game_base import GameBase
import random


class Generala(GameBase):

    name = 'Generala'
    input_args = 2
    input_are_ints = False

    def __init__(self, name='Santi', name2='Beto'):
        super(Generala, self).__init__()
        self.player1 = Player(name)
        self.player2 = Player(name2)
        self.turno = self.player1
        self.dados = []
        self.dados_desordenados = []
        #self.is_playing = True
        self.round = 1
        self.which_to_roll = [0, 1, 2, 3, 4, ]
        self.throw = Throw()

    def next_turn(self):
        if self.is_playing:
            return self.should_keep_rolling()
        else:
            return 'Game over'

    def finished(self):
        if self.player1.score >= 3000:
                return True

        if self.player2.score >= 3000:
                return True

        for key, value in self.player1.combinations.items():
            if self.player1.combinations[key] == '':
                return False
        for key, value in self.player2.combinations.items():
            if self.player2.combinations[key] == '':
                return False
        return True

    def should_keep_rolling(self):
        if self.throw.is_possible_to_roll():
            return '{}\nTu tirada: {} \nIngrese CONSERVAR X, ANOTAR CATEGORIA\
 o TIRAR YA\nx'.format(
                self.turno.name,
                str(self.throw.dice),
            )
        else:
            return (
                '{}\nTu tirada: {} \nElija la categoria\n\
                 que desea llenar (Ej: POKER, GENERALA, ETC.)'.format(
                    self.turno.name,
                    self.throw.dice,
                )
            )

    def play(self, text_input, value):
        if (self.is_playing):
            if 'CONSERVAR' == text_input:
                dados_a_conservar = value.split(',')
                #import ipdb; ipdb.set_trace()
                self.which_to_roll = [0, 1, 2, 3, 4, ]
                for dado_index in dados_a_conservar:
                    dice_to_check = int(dado_index)
                    if dice_to_check in self.which_to_roll:
                        self.which_to_roll.remove(dice_to_check)
                self.throw.roll(self.which_to_roll)

            elif 'TIRAR' == text_input:
                self.should_keep_rolling()
                self.throw.roll([0, 1, 2, 3, 4, ])
            elif 'ANOTAR' == text_input:
                categoria = value
                your_dices = self.throw.dice
                points = check_throw(your_dices, categoria, self.throw.number)
                is_possible = self.turno.choose_combination(categoria, points)
                if is_possible:
                    self.next_turn()
                    self.dados = []
                    self.throw = Throw()
                    self.turno.tirada = 1
                    if self.turno == self.player1:
                        self.turno = self.player2
                    else:
                        self.turno = self.player1
                    self.round += 1
                    if self.finished():
                        self.finish()
                    return 'ANOTADO EN: {} - PUNTAJE: {}'.format(
                        categoria,
                        str(points),
                    )
                else:
                    return 'Categoria ya asignada'
            else:
                return 'Ingrese ANOTAR (TIRADA), CONSERVAR (1,2..), o TIRAR'

    @property
    def board(self):
        return '{} TIENE {} PUNTOS \n{} TIENE {} PUNTOS\nRONDA {}'.format(
            self.player1.name,
            self.player1.score,
            self.player2.name,
            self.player2.score,
            self.round,
        )

