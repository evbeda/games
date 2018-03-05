class ReversiGame(object):

    name = 'Reversi'
    input_args = 2

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

    # # validador maestro, valida si el movimiento esta permitido o no
    # def validMove(self, x, y):
    #     if self.tablero[x][y] !=

    def validate(self, x, y):
        lista = [
            self.validate_empty(x, y),
            self.validate_occupied(x, y),

        ]

        if (False in lista):
            return False
        else:
            return True

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

    def find_possibility_pieces(self, x, y):
        a = y
        b = x
        positions = []
        direction = []
        if self.playingBlack is True:
            piece_to_change = 'W'
            my_piece = 'B'
        else:
            piece_to_change = 'B'
            my_piece = 'W'

        if self.playing:
            while self.tablero[x][y - 1] == piece_to_change:
                direction.append((x, y - 1, piece_to_change))
                y -= 1
            if direction and self.tablero[x][y - 1] == my_piece:
                positions.append(direction)

            y = a
            x = b
            direction = []
            while self.tablero[x][y + 1] == piece_to_change:
                direction.append((x, y + 1, piece_to_change))
                y += 1
            if direction and self.tablero[x][y + 1] == my_piece:
                positions.append(direction)

            y = a
            x = b
            direction = []
            while self.tablero[x - 1][y] == piece_to_change:
                direction.append((x - 1, y, piece_to_change))
                x -= 1
            if direction and self.tablero[x - 1][y] == my_piece:
                positions.append(direction)

            y = a
            x = b
            direction = []
            while self.tablero[x + 1][y] == piece_to_change:
                direction.append((x + 1, y, piece_to_change))
                x += 1
            if direction and self.tablero[x + 1][y] == my_piece:
                positions.append(direction)

            y = a
            x = b
            direction = []
            while self.tablero[x - 1][y + 1] == piece_to_change:
                direction.append((x - 1, y + 1, piece_to_change))
                x -= 1
                y += 1
            if direction and self.tablero[x - 1][y + 1] == my_piece:
                positions.append(direction)

            y = a
            x = b
            direction = []
            while self.tablero[x - 1][y - 1] == piece_to_change:
                direction.append((x - 1, y - 1, piece_to_change))
                x -= 1
                y -= 1
            if direction and self.tablero[x - 1][y - 1] == my_piece:
                positions.append(direction)

            y = a
            x = b
            direction = []
            while self.tablero[x + 1][y - 1] == piece_to_change:
                direction.append((x + 1, y - 1, piece_to_change))
                x += 1
                y -= 1
            if direction and self.tablero[x + 1][y - 1] == my_piece:
                positions.append(direction)

            y = a
            x = b
            direction = []
            while self.tablero[x + 1][y + 1] == piece_to_change:
                direction.append((x + 1, y + 1, piece_to_change))
                x += 1
                y += 1
            if direction and self.tablero[x + 1][y + 1] == my_piece:
                positions.append(direction)
        return positions

    def reverse_posibles(self, posibles):
        for direction in posibles:
            for x, y, piece in direction:
                self.tablero[x][y] = 'B' if self.playingBlack else 'W'

    def play(self, x, y):
        if not(self.validate(x, y)):
            return 'Movimiento no permitido'
        else:
            posibles = self.find_possibility_pieces(x, y)
            if posibles == []:
                return 'No hay posibilidades'
            else:
                self.reverse_posibles(posibles)
                self.tablero[x][y] = 'B' if self.playingBlack else 'W'

    @property
    def board(self):
        result = ''
        result += '  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |\n'
        result += '--+---+---+---+---+---+---+---+---+\n'
        for x in xrange(0, 8):
            result += str(x) + ' |'
            for y in xrange(0, 8):
                result += ' ' + self.tablero[x][y] + ' |'
            result += '\n'
            result += '--+---+---+---+---+---+---+---+---+\n'
        return result
