from .board import show_board
from .bet import BetCreator
from .croupier import Croupier
from .player import Player
from . import (
    SUCCESS_MESSAGE,
    NOT_ENOUGH_CASH_MESSAGE,
    INVALID_BET_MESSAGE,
    INVALID_BET_TYPE_MESSAGE,
    BYE_MESSAGE,
    END_GAME_COMMAND,
    GO_COMMAND,
    GO_END_COMMAND
)

# Exceptions
from .exceptions.out_of_cash_exception import OutOfCashException
from .exceptions.invalid_bet_exception import InvalidBetException
from .exceptions.invalid_bet_type_exception import InvalidBetTypeException


class GameRoulette:
    name = 'Roulette'
    input_args = (1, 3)

    def __init__(self):
        self.is_playing = True
        self.croupier = Croupier(Player(100))

    def next_turn(self):
        return BetCreator.list_bets() + GO_END_COMMAND

    def play(self, *command):
        '''
        command is like:
        BET_SIMPLE 36 100
        BET...
        GO
        QUIT
        '''
        if command[0] == END_GAME_COMMAND:
            self.is_playing = False
            return BYE_MESSAGE
        elif command[0] == GO_COMMAND:
            return self.croupier.play()
        elif 'BET' in command[0] and len(command) == 3:
            try:
                bet_type, bet_values, amount = (
                    command[0], command[1], int(command[2]))
                self.croupier.add_bet(
                    BetCreator.create(bet_type, bet_values, amount))
                return SUCCESS_MESSAGE
            except OutOfCashException:
                return NOT_ENOUGH_CASH_MESSAGE
            except InvalidBetException:
                return INVALID_BET_MESSAGE
            except InvalidBetTypeException:
                return INVALID_BET_TYPE_MESSAGE

    def resolve_command(self, command):
        list_string = command.split()
        bet_type = list_string[0]
        BetCreator.validate_bet_type(bet_type)
        bet_values = [int(number) for number in list_string[1:-1]]
        ammount = int(list_string[-1])
        return (bet_type, bet_values, ammount)

    @property
    def board(self):
        board = show_board() + \
            "Player Money: " + self.croupier.show_player_money() + "\n" + \
            "Placed Bets: " + "\n" + self.croupier.show_placed_bets()
        return board
