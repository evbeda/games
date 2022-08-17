from . import cardsDictionary


class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.counter_as = 0
        self.counter_as_discounted = 0
        self.dictionary_values = {
            1: [0, 11],
            2: [12, 22],
            3: [13, 23],
            4: [14, 24],
        }

    def subtract_points(self, value_without_as, value_sum_1, value_sum_2):
        if (
            (value_without_as + value_sum_2 == self.value or
             value_without_as + value_sum_1 == self.value) and
            self.value > 21
        ):
            self.value -= 10

    def deal_card(self, cards):
        # sumar valor
        total_value = self.value
        cards_without_as = []
        for card in self.cards:
            if not ('A' in card):
                cards_without_as.append(card)
        for card in cards:
            self.cards.append(card)
            if not ('A' in card):
                cards_without_as.append(card)
            else:
                self.counter_as += 1
            total_value += cardsDictionary[card[0]]
        self.value = total_value
        # sumar valor sin ases
        value_without_as = 0
        for card in cards_without_as:
            value_without_as += cardsDictionary[card[0]]
        if self.counter_as > 0:
            value_1, value_2 = self.dictionary_values[self.counter_as]
            self.subtract_points(value_without_as, value_1, value_2)
