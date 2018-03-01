from guess_number_game.guess_number_game import GuessNumberGame


class Game(object):

    def __init__(self):
        super(Game, self).__init__()
        self.games = [
            GuessNumberGame,
        ]

    def output(self, text):
        print text

    def get_input(self, text):
        result = ''
        while(not result.isdigit()):
            result = raw_input(text)
        return int(result)

    def game_inputs(self):
        game_inputs = 'Select Game\n'
        option_number = 0
        for game in self.games:
            game_inputs += '{}: {}\n'.format(
                option_number,
                game.name,
            )
            option_number += 1
        game_inputs += '9: to quit\n'
        return game_inputs

    def play(self):
        while True:
            game_selection = self.get_input(self.game_inputs())
            if game_selection == 9:
                break
            if game_selection < len(self.games):
                active_game = self.games[game_selection]()
                try:
                    while active_game.playing:
                        self.output(active_game.board)
                        game_input = self.get_input(active_game.next_turn())
                        self.output(active_game.play(game_input))
                except Exception:
                    self.output('Sorry... ')


if __name__ == '__main__':
    Game().play()
