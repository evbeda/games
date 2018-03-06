class ReversiGame(object):

    name = 'Reversi'
    input_args = 2
    max = 8
    min = 0

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
        if(self.tablero[x][y] == ' '):
            return True
        else:
            return False

    def in_board(self, x, y):
        if isinstance(x, int) and isinstance(y, int):
            return not(
                self.max <= x or
                self.min > x or
                self.max <= y or
                self.min > y
            )
        else:
            return False

    def has_piece_to_change(self, x, y, piece_to_change):
        if (self.in_board(x, y) and self.tablero[x][y] == piece_to_change):
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
            while self.has_piece_to_change(x, y - 1, piece_to_change):
                direction.append((x, y - 1, piece_to_change))
                y -= 1
            if direction and self.tablero[x][y - 1] == my_piece:
                positions.append(direction)

            y = a
            x = b
            direction = []
            while self.has_piece_to_change(x, y + 1, piece_to_change):
                direction.append((x, y + 1, piece_to_change))
                y += 1
            if direction and self.tablero[x][y + 1] == my_piece:
                positions.append(direction)

            y = a
            x = b
            direction = []
            while self.has_piece_to_change(x - 1, y, piece_to_change):
                direction.append((x - 1, y, piece_to_change))
                x -= 1
            if direction and self.tablero[x - 1][y] == my_piece:
                positions.append(direction)

            y = a
            x = b
            direction = []
            while self.has_piece_to_change(x + 1, y, piece_to_change):
                direction.append((x + 1, y, piece_to_change))
                x += 1
            if direction and self.tablero[x + 1][y] == my_piece:
                positions.append(direction)

            y = a
            x = b
            direction = []
            while self.has_piece_to_change(x - 1, y + 1, piece_to_change):
                direction.append((x - 1, y + 1, piece_to_change))
                x -= 1
                y += 1
            if direction and self.tablero[x - 1][y + 1] == my_piece:
                positions.append(direction)

            y = a
            x = b
            direction = []
            while self.has_piece_to_change(x - 1, y - 1, piece_to_change):
                direction.append((x - 1, y - 1, piece_to_change))
                x -= 1
                y -= 1
            if direction and self.tablero[x - 1][y - 1] == my_piece:
                positions.append(direction)

            y = a
            x = b
            direction = []
            while self.has_piece_to_change(x + 1, y - 1, piece_to_change):
                direction.append((x + 1, y - 1, piece_to_change))
                x += 1
                y -= 1
            if direction and self.tablero[x + 1][y - 1] == my_piece:
                positions.append(direction)

            y = a
            x = b
            direction = []
            while self.has_piece_to_change(x + 1, y + 1, piece_to_change):
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
