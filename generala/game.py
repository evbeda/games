from .player import Player
from .utils import check_throw
from .throw import Throw
from game_base import GameBase, GameWithTurns


class Generala(GameBase, GameWithTurns):

    name = 'Generala'
    input_args = 2
    input_are_ints = False

    def __init__(self, name='Santi', name2='Beto'):
        super(Generala, self).__init__(Player(name), Player(name2))
        self.dados = []
        self.dados_desordenados = []
        self.round = 1
        self.which_to_roll = [0, 1, 2, 3, 4, ]
        self.throw = Throw()

    def next_turn(self):
        if self.is_playing:
            return self.should_keep_rolling()
        else:
            return 'Game over'

    def finished(self):
        if self.player_one.score >= 3000:
            return True

        if self.player_two.score >= 3000:
            return True

        for key, value in self.player_one.combinations.items():
            if self.player_one.combinations[key] == '':
                return False
        for key, value in self.player_two.combinations.items():
            if self.player_two.combinations[key] == '':
                return False
        return True

    def should_keep_rolling(self):
        if self.throw.is_possible_to_roll():
            return '{}\nYour throw: {} \nEnter CROSSOUT (CATEGORY), KEEP\
(1,2..) or THROW NOW\n'.format(
                self.actual_player.name,
                str(self.throw.dice),
            )
        else:
            return (
                '{}\nYour throw: {} \nPick a category\n\
to cross out (e.g.: POKER, GENERALA, ETC.)'.format(
                    self.actual_player.name,
                    self.throw.dice,
                )
            )

    def play(self, text_input, value):

        if (self.is_playing):
            if 'KEEP' == text_input:
                dados_a_conservar = value.split(',')
                self.which_to_roll = [0, 1, 2, 3, 4, ]
                for dado_index in dados_a_conservar:
                    dice_to_check = int(dado_index)
                    if dice_to_check in self.which_to_roll:
                        self.which_to_roll.remove(dice_to_check)
                self.throw.roll(self.which_to_roll)

            elif 'THROW' == text_input:
                self.should_keep_rolling()
                self.throw.roll([0, 1, 2, 3, 4, ])
            elif 'CROSSOUT' == text_input:
                categoria = value
                possible_categories = [
                    'GENERALA',
                    'DOUBLEGENERALA',
                    'POKER',
                    'FULL',
                    'STAIR',
                    'SERVEDGENERALA',
                    'SERVEDFULL',
                    'SERVEDSTAIR',
                    'ONE',
                    'TWO',
                    'THREE',
                    'FOUR',
                    'FIVE',
                    'SIX',
                ]
                if categoria in possible_categories:
                    your_dices = self.throw.dice
                    points = check_throw(
                        your_dices, categoria,
                        self.throw.number,
                    )
                    is_possible = self.actual_player.choose_combination(
                        categoria,
                        points,
                    )
                    if is_possible:
                        self.next_turn()
                        self.dados = []
                        self.throw = Throw()
                        self.change_turn()
                        self.actual_player.tirada = 1
                        self.round += 1
                        if self.finished():
                            self.finish()
                        return 'YOU CROSSED OUT: {} - SCORE: {}'.format(
                            categoria,
                            str(points),
                        )
                    else:
                        return '\n***That category has already been '\
                            'crossed out.***\n'
                else:
                    return '\n***That category does not exist.***\n'
            else:
                return 'Enter CROSSOUT (CATEGORY), KEEP (1,2..) or THROW NOW'

    @property
    def board(self):
        return '{} HAS {} POINTS \n{} HAS {} POINTS\nROUND {}'.format(
            self.player_one.name,
            self.player_one.score,
            self.player_two.name,
            self.player_two.score,
            self.round,
        )
