class Player:
    def __init__(self, name='', character=None):
        self.name = ''
        self.character = character[0] if character else ''
        self.wounds = character[1] if character else 0
        self.gold = character[2] if character else 0

    def add_wounds(self, wounds):
        self.wounds += wounds

    def add_gold(self, gold):
        self.gold += gold

    @property
    def status(self):
        return f'{self.character}, wounds: {self.wounds}, gold: {self.gold}'
