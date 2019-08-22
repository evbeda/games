from .turn import Turn
from .bet import BetCreator
from .exceptions.invalid_bet_type_exception import InvalidBetTypeException
from .exceptions.out_of_cash_exception import OutOfCashException
from .exceptions.invalid_bet_turn_exception import InvalidBetTurnException
from .constants import (
    PLAYER_LOST,
    PLAYER_WON,
    WON_MESSAGE,
    LOST_MESSAGE,
    BET_MESSAGE,
    BET_PLACED,
    INVALID_BET_TYPE,
    OUT_OF_CASH,
    CAN_NOT_LEAVE,
    INVALID_TURN_BET,
    GO_COMMAND,
    NO_COMMAND,
    GAME_OVER,
    GAME_IN_PROGRESS,
    GAME_STARTED,
    SHOOT_DICE_MESSAGE,
    BET_AGAIN_OR_GO,
)


class CrapsGame:

    name = 'Craps Game'
    input_args = (1, 2, 3)

    def __init__(self):
        self.turn = Turn()
        self.is_playing = True
        self.money = 1000

    def next_turn(self):
        if self.turn.state == PLAYER_LOST:
            return LOST_MESSAGE
        if self.turn.state == PLAYER_WON:
            return WON_MESSAGE

        if self.turn.state == GAME_STARTED:
            return BET_AGAIN_OR_GO if self.turn.bets \
                else BetCreator.list_bets(self.turn.state) + BET_MESSAGE

        if self.turn.state == GAME_IN_PROGRESS:
            return SHOOT_DICE_MESSAGE

    def play(self, *user_input):
        # In case of the user wants to finish his turn
        if user_input[0] == NO_COMMAND:
            if self.turn.state == PLAYER_LOST or self.turn.state == PLAYER_WON:
                self.is_playing = False
                return GAME_OVER
            else:
                return CAN_NOT_LEAVE + BET_MESSAGE
        # If anybody has won or lost, the actual turn is done
        # So we have to create a new one, otherwise we use the old one
        if self.turn.state == PLAYER_LOST or self.turn.state == PLAYER_WON:
            self.turn = Turn()
        # The player wants to shoot the dices
        # and determine if he has won or not
        if user_input[0] == GO_COMMAND:
            self.money += self.turn.shoot()
            return self.turn.dice

        try:
            # bet_type, amount, bet_values = \
            #     CrapsGame.resolve_command(user_input)
            bet_type = user_input[0]
            amount = int(user_input[1])
            bet_values = user_input[2] if len(user_input) == 3 else None
            # Create the bet, decrease money
            # Append the new bet to list of bets
            bet = BetCreator.create(bet_type, amount, self.turn, bet_values)
            self.decrease_money(amount)
            self.turn.bets.append(bet)
            return BET_PLACED + bet_type
        except InvalidBetTypeException:
            return INVALID_BET_TYPE
        except OutOfCashException:
            return OUT_OF_CASH
        except InvalidBetTurnException:
            return INVALID_TURN_BET

    def decrease_money(self, amount):
        if amount > self.money:
            raise OutOfCashException()
        self.money -= amount

    @property
    def board(self):
        ret = ''
        ret += self.turn.build_board()
        ret += 'Money: {}'.format(self.money)
        return ret
