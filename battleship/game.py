import sys
sys.path.insert(0, '../')
from player import PlayerCPU, PlayerHuman
from game_base import GameBase, GameWithBoard
from board import Board


game_states = ['init', 'war', 'cpu_win', 'player_win']
possible_turn = ['human', 'cpu']
messages_player_human = {
    'init': 'pone el barco (x y boat horizontal/vertical)',
    'shoot': 'shoot (x y)',
    'cpu_win': 'gano el cpu',
    'player_win': 'ganaste',
}


class GameBattleship(GameBase, GameWithBoard):

    name = 'Battleship'

    rows = 10
    cols = 10

    def __init__(self):
        super(GameBattleship, self).__init__()
        self.turn = possible_turn[0]
        self.player_cpu = PlayerCPU()
        self.player_human = PlayerHuman()
        self.state = game_states[0]
        self.input_args = 4
        self.input_are_ints = False

    def get_players(self):
        return [self.player_cpu, self.player_human]

    def set_boat(self, text_input):
        params = text_input
        if len(params) == 4:
            try:
                result = self.player_human.put_boat_own_board(
                    int(params[0]),
                    int(params[1]),
                    int(params[2]),
                    params[3],
                )
                # Si ya seteo todos los barcos de su tablero inicial
                if self.player_human.board_own.is_ready_to_war():
                    # Llenar el tablero de la cpu
                    self.player_cpu.fill_own_board()
                    if self.is_ready_to_war():
                        self.state = game_states[1]
                if result:
                    return "Your boat of {} was set in {}, {} .".format(
                        params[2],
                        params[0],
                        params[1],
                    )
                else:
                    return "Your boat could not be set in that position"
            except Exception:
                return "error"
        else:
            return "error, mas parametros de los requeridos (4)"

    def war_human(self, text_input):
        params = text_input
        self.player_human.messages = []
        self.player_cpu.messages = []
        if len(params) == 2:
            #import ipdb; ipdb.set_trace()
            result = self.player_cpu.board_own.shoot(
                int(params[0]),
                int(params[1])
            )
            if result == 'water':
                self.player_human.board_opponent.mark_shoot(
                    int(params[0]),
                    int(params[1]),
                    False
                )
                self.turn = possible_turn[1]
                self.player_human.messages.append(
                    'You only hit water! CPU turn')
                self.war_cpu()
                for message in self.player_cpu.messages:
                    self.player_human.messages.append(message)
                result = self.player_human.messages
            elif result == 'already shoot':
                self.player_human.messages.append('You already shoot in this place. Try again')
                result = self.player_human.messages
            elif result == 'sunked':
                self.player_human.board_opponent.mark_shoot(
                    int(params[0]),
                    int(params[1]),
                    True
                )
                self.player_human.messages.append(
                    'Congratulations! You sunk a boat.')
                result = self.player_human.messages
            elif result == 'hit':
                self.player_human.board_opponent.mark_shoot(
                    int(params[0]),
                    int(params[1]),
                    True
                )
                self.player_human.messages.append('You hit a boat')
                result = self.player_human.messages
                if not self.player_cpu.board_own.there_are_boats():
                    self.state = game_states[3]
                    self.player_human.messages.append('You Win')
                    result = self.player_human.messages
                    self.finish()
            return result
        else:
            return "error, mas parametros de los requeridos (2)"

    def war_cpu(self):
        coordenate = self.player_cpu.pick_coordenate()
        result = self.player_human.board_own.shoot(*coordenate)
        #import ipdb; ipdb.set_trace()
        if result == 'water':
            self.player_cpu.board_opponent.mark_shoot(
                False,
                *coordenate
            )
            self.turn = possible_turn[0]
            self.player_cpu.messages.append('Water! Now is your turn.')
            result = self.player_cpu.messages
            return result
        elif result == 'sunked':
            self.player_cpu.board_opponent.mark_shoot(
                True,
                *coordenate
            )
            self.player_cpu.messages.append('Your boat was sunk.')
            result = self.player_cpu.messages
            #import ipdb; ipdb.set_trace()
            if not self.player_human.board_own.there_are_boats():
                self.state = game_states[2]
                self.player_cpu.messages.append('You lose.')
                result = self.player_cpu.messages
                self.finish()
                return result
            return result
        elif result == 'hit':
            self.player_cpu.board_opponent.mark_shoot(
                True,
                *coordenate
            )
            self.player_cpu.messages.append('Your boat was hit.')
            result = self.player_cpu.messages
            self.war_cpu()
            return result
        else:
            return result

    def is_ready_to_war(self):
        if (
            self.player_cpu.board_own.is_ready_to_war() and
            self.player_human.board_own.is_ready_to_war()
        ):
            return True

    def next_turn(self):
        if self.is_playing:
            if self.state == game_states[0] and self.turn == possible_turn[0]:
                return messages_player_human['init']
            elif self.state == game_states[1] and self.turn == possible_turn[0]:
                self.input_args = 2
                self.input_are_ints = True
                return messages_player_human['shoot']

    def play(self, lat=0, lon=0, boat=0, orientation=0):
        if self.state == game_states[0]:
            return self.set_boat([lat, lon, boat, orientation])
        elif self.state == game_states[1] and self.turn == possible_turn[0]:
            return self.war_human([lat, lon])
        elif self.state == game_states[1] and self.turn == possible_turn[1]:
            return self.war_cpu()

    @property
    def board(self):
        output = ''
        output += "\n"
        output += "Own Board (Player)"
        output += "\n"
        output += " y 0 1 2 3 4 5 6 7 8 9\n"
        output += "x  \n"
        for y in range(0, self.cols):
            for x in range(0, self.rows):
                casilla = str(self.player_human.board_own.board[y][x])

                if x % 10 == 0:
                    output += str(y) + ' '

                if casilla == '32':
                    casilla = '3'
                    output += '|' + casilla

                elif casilla == '31':
                    casilla = '3'
                    output += '|' + casilla

                else:
                    output += '|' + casilla

                if(x == 9):
                    output += '|' + '\n'

        output += "\n"
        output += "Opponent Board (CPU)"
        output += "\n"
        output += " y 0 1 2 3 4 5 6 7 8 9\n"
        output += "x  \n"
        for y in range(0, self.cols):
            for x in range(0, self.rows):
                casilla = str(self.player_human.board_opponent.board[y][x])

                if x % 10 == 0:
                    output += str(y) + ' '

                if casilla == '32':
                    casilla = '3'
                    output += '|' + casilla

                elif casilla == '31':
                    casilla = '3'
                    output += '|' + casilla

                else:
                    output += '|' + casilla

                if(x == 9):
                    output += '|' + '\n'

        return output
