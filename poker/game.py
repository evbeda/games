import random
from .player import Player
from .hand import Hand
from .poker import (
    CHECK,
    CALL,
    BET,
    FOLD,
    RAISE,
)


class PokerGame(object):
    def __init__(self):
        self.player = Player(100)
        self.cpu = Player(100)
        self.is_playing = True
        self.hand = Hand([self.player, self.cpu])

    def next_turn(self):
        if self.player_no_money():
            return self.player_no_money()
        if self.is_playing:
            actions = self.hand.possibles_actions()
            if self.hand.turn == 'player':
                if self.hand.stage < 5:
                    return_string = ''
                    for action in actions:
                        return_string += ' ' + action
                        if action == BET or action == RAISE:
                            return_string += ' your bet'
                        return_string += '\n'
                    return return_string
                else:
                    return 'Show Down!'
                    # TODO VER SI LA CPU SI TIENE PLATA PARA EL RAISE

    def play(self, command):
        if self.is_playing:
            possibles_actions = hand.possibles_actions()
            if self.hand.turn == 'player':
                if self.hand.stage < 5:
                    splited_command = command.split(' ')
                    if splited_command[0] in possibles_actions:
                        if splited_command[0] == 'bet' or splited_command[0] == 'raise':
                            try:
                                bet = int(splited_command[1])
                                return self.hand.take_action(splited_command[0], splited_command[1])
                            except Exception:
                                raise 'Please enter a number to bet'
                        else:
                            return self.hand.take_action(splited_command[0])
            else:
                cpu_action = random.choice(possibles_actions)
                if cpu_action == BET
                    amount = random.randint(1, self.hand.player[1].money)
                    self.play('bet {}'.format(amount))
                elif cpu_action == RAISE
                    amount = self.hand.last_bet * 2
                    if amount > self.hand.player[1].money:
                        self.play('ra {}'.format(random.randint(self.hand.last_bet, self.hand.player[1].money)))
                    else:
                        self.play('ra {}'.format(self.hand.player[1].money))

    def player_no_money(self):
        if self.player.money == 0:
            return 'Player loses'
        elif self.cpu.money == 0:
            return 'CPU loses'
        return False


