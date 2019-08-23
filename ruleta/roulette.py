from random import randint


class Roulette:

    def __init__(self):
        self.last_numbers = []

    def generate_number(self):
        number = randint(0, 36)
        self.last_numbers.append(number)
        return number

    def get_last_numbers(self):
        return self.last_numbers
