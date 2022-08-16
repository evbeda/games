from game_base import GameBase
from .player import Player
from .hand import Hand
from .poker import (
    CALL,
    BET,
    FOLD,
    RAISE,
    PLAYER,
    CPU
)


class PokerGame(GameBase):
    name = 'Poker'
    input_args = 1
    input_are_ints = False

    def __init__(self, *args, **kwargs):
        super(PokerGame, self).__init__(*args, **kwargs)
        self.player = Player(100)
        self.cpu = Player(100)
        self.hand = Hand([self.player, self.cpu])

    def next_turn(self):
        if self.player_no_money():
            return self.player_no_money()
        if self._playing:
            actions = self.hand.possibles_actions()
            if self.hand.turn == PLAYER:
                if self.hand.stage < 5:
                    return_string = ''
                    for action in actions:
                        return_string += ' ' + action
                        if action == BET or action == RAISE:
                            return_string += ',your bet'
                        return_string += '\n'
                    return_string += 'q to quit'
                    return return_string
                else:
                    return self.show_down()
                    # TODO: VER SI LA CPU SI TIENE PLATA PARA EL RAISE

    def play(self, command):
        if self._playing:
            if command == 'q':
                self._playing = False
                return 'You quit the game'
            possibles_actions = self.hand.possibles_actions()
            if self.hand.turn == PLAYER:
                if self.hand.stage < 5:
                    splited_command = command.split(',')
                    if splited_command[0] in possibles_actions:
                        if (
                            splited_command[0] == BET
                            or splited_command[0] == RAISE
                        ):

                            try:
                                bet = int(splited_command[1])
                                result = PLAYER + ': ' + self.hand.take_action(
                                    splited_command[0], bet)
                                result = result + '\n' + CPU + ': ' +\
                                    self.hand.play_as_cpu()
                                return result
                            except Exception:
                                return 'Please enter a number to bet'
                        elif (
                            splited_command[0] == FOLD
                            or splited_command[0] == CALL
                        ):
                            result = self.hand.take_action(splited_command[0])
                            return result
                        else:
                            result = PLAYER + ': ' + self.hand.take_action(
                                splited_command[0])
                            result = result + '\n' + CPU + ': ' +\
                                self.hand.play_as_cpu()
                            return result
                    else:
                        return 'Invalid action'

    @property
    def board(self):
        if self.hand.stage < 5:
            return ('\nPOT: {pot}'
                    '\nPLAYER: {player_cards} \n'
                    'COMMON CARDS: {common_cards} \n'
                    'PLAYER MONEY: {money_player} \n'
                    'CPU MONEY: {money_cpu} \n\n').format(
                pot=self.hand.pot,
                player_cards=self.hand.player_cards,
                common_cards=self.hand.common_cards,
                money_player=self.player.money,
                money_cpu=self.cpu.money,
            )

    def show_down(self):
        return ('\nWINNER: {winner}'
                '\nPOT: {pot}'
                '\nPLAYER: {player_cards} \n'
                '\nCPU: {cpu_cards} \n'
                'COMMON CARDS: {common_cards} \n'
                'PLAYER MONEY: {money_player} \n'
                'CPU MONEY: {money_cpu} \n\n').format(
            winner=self.hand.winner,
            pot=self.hand.pot,
            player_cards=self.hand.player_cards,
            cpu_cards=self.hand.cpu_cards,
            common_cards=self.hand.common_cards,
            money_player=self.player.money,
            money_cpu=self.cpu.money,
        )

    def player_no_money(self):
        if self.player.money == 0:
            # self._playing = False
            return 'Player loses'
        elif self.cpu.money == 0:
            # self._playing = False
            return 'CPU loses'
        return False
