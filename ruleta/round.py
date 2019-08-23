class Round:
    def __init__(self):
        self.bets = []

    def add_bet(self, bet):
        self.bets.append(bet)

    def calculate_total_award(self, chosen_number):
        return sum([bet.calculate_award(chosen_number) for bet in self.bets])

    def show_bets(self):
        if not self.bets:
            return "No bets"
        # stringify each bet
        bets_str = [str(bet) for bet in self.bets]
        return "\n".join(bets_str)
