from .round import Round
from .roulette import Roulette

# Messages
from . import WON_MESSAGE, LOST_MESSAGE

# Exceptions
from .exceptions.out_of_cash_exception import OutOfCashException


class Croupier:
    def __init__(self, player):
        self.player = player
        self.round = Round()
        self.roulette = Roulette()

    def discount_money_from_player(self, ammount):
        if ammount > self.player.money:
            raise OutOfCashException()
        self.player.money -= ammount

    def add_bet(self, bet):
        self.discount_money_from_player(bet.amount)
        self.round.add_bet(bet)

    def play(self):
        chosen_number = self.roulette.generate_number()
        award = self.distribute_awards(chosen_number)
        self.round = Round()
        if award > 0:
            return WON_MESSAGE + str(award) + ' chips' + \
                '\nRANDOM NUMBER: ' + str(chosen_number)
        else:
            return LOST_MESSAGE + '\nRANDOM NUMBER: ' + str(chosen_number)

    def distribute_awards(self, chosen_number):
        total_award = self.round.calculate_total_award(chosen_number)
        self.player.money += total_award
        return total_award

    def show_player_money(self):
        return "$" + str(self.player.money)

    def show_placed_bets(self):
        return self.round.show_bets()
