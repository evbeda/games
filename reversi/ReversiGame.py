class ReversiGame(object):

    def __init__(self):
        super(ReversiGame, self).__init__()
        self.playing = True
        self.playingBlack = True
        self.tablero = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', 'B', 'W', ' ', ' ', ' '],
            [' ', ' ', ' ', 'W', 'B', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ]

    def next_turn(self):
        if self.playing:
            if self.playingBlack:
                self.playingBlack = False
                return 'Turn of the whiteones'
            else:
                self.playingBlack = True
                return 'Turn of the blackones'
        else:
            return 'Game Over'

    # validador maestro, valida si el movimiento esta permitido o no
    def validate(self, x, y):
        lista = [
            self.validate_empty(x, y),
            self.validate_occupied(x, y),

        ]

        if (False in lista):
            return False
        else:
            return True

    def play(self, x, y):
        if not(self.validate(x, y)):
            return 'Movimiento no permitido'
        else:
            return 'Correcto'

    # Valida si la casilla esta ocupada o no
    def validate_occupied(self, x, y):
        if(self.tablero[x][y] != ' '):
            return False
        else:
            return True

    # Valida si la casilla esta vacia o no
    # la lista posibilidades son todas los casilleros alrededor del punto (x,y)
    def validate_empty(self, x, y):
        posibilidades = [
            (x - 1, y - 1),
            (x - 1, y),
            (x - 1, y + 1),
            (x, y - 1),
            (x, y + 1),
            (x + 1, y - 1),
            (x + 1, y),
            (x + 1, y + 1),
        ]
        count = 0
        for i in posibilidades:
            a, b = i
            casilla = self.tablero[a][b]
            if casilla == ' ':
                count += 1
        if count == 8:
            return False
        else:
            return True

    def get_directions(self, x, y):
        positions = []
        a, b = x, y
        if self.playingBlack is True:
            player = 'B'
            opponent = 'W'
        else:
            player = 'W'
            opponent = 'B'
 
        direction = []
        while self.tablero[x][y - 1] == opponent:
            direction.append((x, y - 1, opponent))
            y -= 1
        if direction and self.tablero[x][y - 1] == player:
            positions.append(direction)

        x, y = a, b
        direction = []
        while self.tablero[x + 1][y - 1] == opponent:
            direction.append((x + 1, y - 1, opponent))
            x += 1
            y -= 1
        if direction and self.tablero[x + 1][y - 1] == player:
            positions.append(direction)
 
        x, y = a, b
        direction = []
        while self.tablero[x + 1][y] == opponent:
            direction.append((x + 1, y, opponent))
            x += 1
        if direction and self.tablero[x + 1][y] == player:
            positions.append(direction)
 
        x, y = a, b
        direction = []
        while self.tablero[x + 1][y + 1] == opponent:
            direction.append((x + 1, y + 1, opponent))
            x += 1
            y += 1
        if direction and self.tablero[x + 1][y + 1] == player:
                positions.append(direction)
 
        x, y = a, b
        direction = []
        while self.tablero[x][y + 1] == opponent:
            direction.append((x, y + 1, opponent))
            y += 1
        if direction and self.tablero[x][y + 1] == player:
            positions.append(direction)

        x, y = a, b
        direction = []
        while self.tablero[x - 1][y + 1] == opponent:
            direction.append((x - 1, y + 1, opponent))
            x -= 1
            y += 1
        if direction and self.tablero[x - 1][y + 1] == player:
            positions.append(direction)
 
        x, y = a, b
        direction = []
        while self.tablero[x - 1][y] == opponent:
            direction.append((x - 1, y, opponent))
            x -= 1
        if direction and self.tablero[x - 1][y] == player:
            positions.append(direction)

        x, y = a, b
        direction = []
        while self.tablero[x - 1][y - 1] == opponent:
            direction.append((x - 1, y - 1, opponent))
            x -= 1
            y -= 1
        if direction and self.tablero[x - 1][y - 1] == player:
            positions.append(direction)

        return positions
