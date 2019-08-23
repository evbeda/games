from .exceptions.exceptions import NotANumberException, \
    UnplayableCardException


class HandPlayer:
    def __init__(self, player, cards=None):
        self.cards_to_play = cards if cards else [1, 2, 3, 4, 5]
        self.player = player
        self.last_card_played = None
        self.chosen_card = 0

    def play(self, chosen_card=None):
        if self.validate(chosen_card):
            self.cards_to_play.remove(self.chosen_card)
            self.last_card_played = self.chosen_card

    def validate(self, chosen_card):
        try:
            self.chosen_card = int(chosen_card)
        except ValueError:
            raise NotANumberException()
        if self.chosen_card not in self.cards_to_play:
            raise UnplayableCardException(f'You can\'t play a {chosen_card} again')
        return True
