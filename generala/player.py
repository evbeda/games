
class Player(object):
    def __init__(self, name):
        self.name = name
        self.tirada = 1
        self.combinations = {
            'ONE': '',
            'TWO': '',
            'THREE': '',
            'FOUR': '',
            'FIVE': '',
            'SIX': '',
            'STAIR': '',
            'FULL': '',
            'POKER': '',
            'GENERALA': '',
            'DOUBLEGENERALA': '',
            'SERVEDSTAIR': '',
            'SERVEDFULL': '',
            'SERVEDPOKER': '',
        }
        self.score = 0

    def choose_combination(self, combination, value):
        # Verificar si es posible la combinacion y setearle el value
        if self.combinations[combination] == '':
            self.combinations[combination] = value
            self.add_score(value)
            return True
        else:
            return False

    def add_score(self, points):
        self.score += points
