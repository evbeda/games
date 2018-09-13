import random
from .deck import Deck
from .poker import PREFLOP, FLOP, TURN, RIVER
from .poker import CHECK, CALL, BET, RAISE, FOLD, NONE
from .poker import (
    transform_cards_to_str,
    combine_card,
    better_hand,
    find_straight_flush,
    find_royal_flush,
    find_repeated_cards,
    find_flush,
    find_cards_suits,
    find_straight,
    sort_cards_by_number,
    get_value,
    PLAYER, CPU,
)


class Hand():
    def __init__(self, players, first = PLAYER):
        self.pot = 0
        self.deck = Deck()
        self.stage = 1
        self.player_cards = self.deck.deal(2)
        self.cpu_cards = self.deck.deal(2)
        self.common_cards = []
        self.first = first
        self.turn = first
        self.last_action = NONE
        self.last_bet = 0
        self.players = players
        self.all_in_value = False
        self.winner = None


    def deal_cards(self):
        if self.stage == FLOP:
            self.common_cards = self.deck.deal(3)
        elif self.stage == TURN or self.stage == RIVER:
            self.common_cards.append(self.deck.deal(1)[0])

    def possibles_actions(self):
        if self.all_in_value:
            return [CALL, FOLD]
        elif self.last_action == NONE or self.last_action == CHECK or self.last_action == CALL:
            return [CHECK, BET]
        elif self.last_action == BET or self.last_action == RAISE:
            return [CALL, RAISE, FOLD]

    def next_stage(self):
        if self.stage < 5:
            self.stage += 1
            self.turn = self.first
            self.deal_cards()
            self.last_action = NONE
            self.last_bet = 0
        else:
            a = transform_cards_to_str(self.player_cards) + transform_cards_to_str(self.common_cards)
            b = transform_cards_to_str(self.cpu_cards) + transform_cards_to_str(self.common_cards)
            player_game = better_hand(combine_card(a))
            cpu_game = better_hand(combine_card(b))
            self.winner = PLAYER
            return [player_game, cpu_game]

    def take_action(self, action, bet=0):
        if action == CHECK:
            if self.last_action == CHECK:
                result = self.next_stage()
                if result:
                    return result
            else:
                self.last_action = action
                self.turn = PLAYER if (self.turn == CPU) else CPU
        elif action == BET:
            if self.last_action == RAISE:
                return "You can't bet now"
            elif self.turn == PLAYER and self.players[0].money < bet:
                return "You don't have enough money"
            else:
                self.last_action = action
                self.pot += bet
                self.last_bet = bet
                if self.turn == PLAYER:
                    if self.players[0].money == bet:
                        self.all_in_value = True
                        self.players[0].money -= bet
                        self.turn = PLAYER if (self.turn == CPU) else CPU
                        return 'All In Done'
                    else:
                        self.players[0].money -= bet
                else:
                    self.players[1].money -= bet
                self.turn = PLAYER if (self.turn == CPU) else CPU

        elif action == CALL:
            if self.last_action == BET or self.last_action == RAISE:
                if self.turn == PLAYER:
                    self.players[0].money -= self.last_bet
                elif self.turn == CPU:
                    self.players[1].money -= self.last_bet
                self.pot += self.last_bet
                if self.all_in_value:
                    self.all_in()
                else:
                    result = self.next_stage()
                    if result:
                        return result
            else:
                return "You can't CALL now"
        elif action == FOLD:
            if self.last_action == BET or self.last_action == RAISE:
                if self.turn == CPU:
                    self.players[0].money += self.pot
                elif self.turn == PLAYER:
                    self.players[1].money += self.pot
                return "the {} win".format(PLAYER if (self.turn == CPU) else CPU)
            else:
                return "You can't FOLD now"
        elif action == RAISE:
            if self.last_action == BET or self.last_action == RAISE:
                turn_money = None
                if self.turn == PLAYER:
                    turn_money == self.players[0].money
                else:
                    turn_money == self.players[1].money

                if self.turn == PLAYER and self.players[0].money < bet:
                    return "You don't have enough money"
                elif bet >= (2 * self.last_bet):
                    self.last_action = action
                    self.pot += bet
                    self.last_bet = bet - self.last_bet
                    if self.turn == PLAYER:
                        self.players[0].money -= bet
                    else:
                        self.players[1].money -= bet
                    self.turn = PLAYER if (self.turn == CPU) else CPU
                elif bet < (2 * self.last_bet) and bet == turn_money:
                    self.last_action = action
                    self.pot += turn_money
                    self.last_bet = turn_money
                    if self.turn == PLAYER:
                        self.players[0].money -= turn_money
                    else:
                        self.players[1].money -= turn_money
                    self.all_in()
                else:
                    return "You must raise at least twice last bet"
        return action + ' done!'

    def play_as_cpu(self):
        amount = 0
        cpu_action = random.choice(self.possibles_actions())
        if cpu_action == BET:
            amount = random.randint(1, self.players[1].money)
        elif cpu_action == RAISE:
            min_raise = self.last_bet * 2
            if min_raise < self.players[1].money:
                amount = self.last_bet + random.randint(min_raise, self.players[1].money)
            else:
                amount = self.players[1].money
        return self.take_action(cpu_action, amount)

    def all_in(self):
        self.all_in_value = True
        while self.stage < 5:
            result = self.next_stage()

        return 'All In' + result
