import random
from .constants import GAME_STARTED, GAME_IN_PROGRESS, PLAYER_LOST
from .constants import PLAYER_WON, LOSING_SCORES, WINNING_SCORES


class Turn:
    def __init__(self):
        self.state = GAME_STARTED
        self.point = None
        self.bets = []
        self.dice = None

    def get_next_state(self):
        score = sum(self.dice)
        if self.state == GAME_STARTED:
            if score in LOSING_SCORES:
                return PLAYER_LOST
            if score in WINNING_SCORES:
                return PLAYER_WON
            return GAME_IN_PROGRESS
        if self.state == GAME_IN_PROGRESS:
            if score == self.point:
                return PLAYER_WON
            if score == 7:
                return PLAYER_LOST
            return GAME_IN_PROGRESS

    # It return the amount of the bet
    def shoot(self):
        # Throws two dice, returns their values and changes the state.
        self.dice = tuple(random.sample(range(1, 7), k=2))
        self.state = self.get_next_state()
        # Determine if setting points
        if not self.point and self.state == GAME_IN_PROGRESS:
            self.point = sum(self.dice)
        return self.pay_bets()

    def check_bets(self):
        activated_bets = [bet for bet in self.bets if bet.check(self)]
        # self.bets = [bet for bet in self.bets if bet not in activated_bets]
        return activated_bets

    def pay_bets(self):
        # activated_bets = self.check_bets()
        return sum([bet.pay(self) for bet in self.bets])

    def build_board(self):
        board = ''
        board += 'Point: {}\n'.format(self.point) if self.point else 'Point: -\n'
        board += 'Dice: {}\n'.format(self.dice) if self.dice else 'Dice: No dices played\n'
        # board += 'Bet:\n'
        for bet in self.bets:
            board += 'Bet:{}'.format(bet)
        return board
