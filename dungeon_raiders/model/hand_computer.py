from random import choice as choice


class HandComputer:
    def __init__(self, player=None):
        self.cards_to_play = [1, 2, 3, 4, 5]
        self.player = player
        self.last_card_played = None

    def play(self, chosen_card=None):
        chosen_card = self.select_card(self.cards_to_play)
        self.cards_to_play.remove(chosen_card)
        self.last_card_played = chosen_card

    def select_card(self, cards):
        if not cards:
            self.cards_to_play = cards = [1, 2, 3, 4, 5]
        return choice(cards)
