from guess_number_game.guess_number_game import GuessNumberGame
from tateti.tateti import Tateti
from buscaminas.buscaminas import Buscaminas
from connect_four_game.connect_four_game import ConnectFourGame
from damas.dama_game import DamaGameStart
from reversi.ReversiGame import ReversiGame
from four_number.four_number import FourNumber
from generala.game import Generala
from blackjack.blackjack_game import BlackJackGame
from battleship.game import GameBattleship

class Game(object):

    def __init__(self):
        super(Game, self).__init__()
        self.games = [
            GuessNumberGame,
            Tateti,
            Buscaminas,
            ConnectFourGame,
            DamaGameStart,
            ReversiGame,
            FourNumber,
            Generala,
            BlackJackGame,
            GameBattleship,
        ]

    def output(self, text):
        print text

    def get_input(self, text):
        return raw_input(text)

    def game_inputs(self):
        game_inputs = 'Select Game\n'
        option_number = 0
        for game in self.games:
            game_inputs += '{}: {}\n'.format(
                option_number,
                game.name,
            )
            option_number += 1
        game_inputs += '99: to quit\n'
        return game_inputs

    def get_turn_input(self, text):
        input_args = ''
        expecting_str = (
            'commands separated with spaces'
            if self.active_game.input_args > 1 else 'number'
        )
        while True:

            inputs = self.get_input('{} (expecting {} {})\n'.format(
                text,
                self.active_game.input_args,
                expecting_str,
            ))
            try:
                if self.active_game.input_are_ints:
                    input_args = [
                        int(simple_arg)
                        for simple_arg in inputs.split(' ')
                    ]
                else:
                    input_args = inputs.split(' ')
                if len(input_args) == self.active_game.input_args:
                    break
                else:
                    self.output(
                        'Wrong input count, expecting {} values'.format(
                            self.active_game.input_args
                        )
                    )
            except Exception:
                self.output('Wrong input, try again!')
        return input_args

    def select_game(self):
        result = ''
        while(not result.isdigit()):
            result = self.get_input(self.game_inputs())
        return int(result)

    def play(self):
        while True:
            game_selection = self.select_game()
            if game_selection == 99:
                break
            if game_selection < len(self.games):
                self.active_game = self.games[game_selection]()
                try:
                    while (
                        (
                            hasattr(self.active_game, 'playing') and
                            self.active_game.playing
                        ) or (
                            hasattr(self.active_game, 'is_playing') and
                            self.active_game.is_playing
                        )
                    ):
                        self.output(self.active_game.board)
                        game_input = self.get_turn_input(
                            self.active_game.next_turn(),
                        )
                        self.output(self.active_game.play(*game_input))
                except Exception, e:
                    self.output('Sorry... {}'.format(e))


if __name__ == '__main__':
    Game().play()
