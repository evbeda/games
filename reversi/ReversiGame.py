from game_base import GameBase
from game_base import GameWithTurns


class ReversiGame(GameBase, GameWithTurns):

    name = 'Reversi'
    input_args = 2
    max = 8
    min = 0
    player_one = 'White'
    player_two = 'Black'

    def __init__(self):
        super(ReversiGame, self).__init__()
        self.matrix_board = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', 'B', 'W', ' ', ' ', ' '],
            [' ', ' ', ' ', 'W', 'B', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ]
        self.moves = []

    def next_turn(self):
        if self.actual_player == self.player_one:
            return 'White'
        else:
            return 'Black'

    # # validador maestro, valida si el movimiento esta permitido o no
    # def validMove(self, x, y):
    #     if self.matrix_board[x][y] !=

    def validate(self, x, y):
        if x > 7 or x < 0 or y > 7 or y < 0:
            return 'Values must be between 0 and 7'
        else:
            if(self.matrix_board[x][y] == ' '):
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

    def has_piece_to_change(self, x, y, piece):
        if (self.in_board(x, y) and
                self.matrix_board[x][y] == piece):
            return True

    def find_possibility_pieces(self, x, y):
        a = y
        b = x
        positions = []
        direction = []
        if self.player_one == self.actual_player:
            piece_to_change = 'B'
            my_piece = 'W'
        else:
            piece_to_change = 'W'
            my_piece = 'B'

        while self.has_piece_to_change(x, y - 1, piece_to_change):
            direction.append((x, y - 1, piece_to_change))
            y -= 1
        if y - 1 >= 0:
            if direction and self.has_piece_to_change(x, y - 1, my_piece):
                positions.append(direction)

        y = a
        x = b
        direction = []
        while self.has_piece_to_change(x, y + 1, piece_to_change):
            direction.append((x, y + 1, piece_to_change))
            y += 1
        if direction and self.has_piece_to_change(x, y + 1, my_piece):
            positions.append(direction)

        y = a
        x = b
        direction = []
        while self.has_piece_to_change(x - 1, y, piece_to_change):
            direction.append((x - 1, y, piece_to_change))
            x -= 1
        if direction and self.has_piece_to_change(x - 1, y, my_piece):
            positions.append(direction)

        y = a
        x = b
        direction = []
        while self.has_piece_to_change(x + 1, y, piece_to_change):
            direction.append((x + 1, y, piece_to_change))
            x += 1
        if direction and self.has_piece_to_change(x + 1, y, my_piece):
            positions.append(direction)

        y = a
        x = b
        direction = []
        while self.has_piece_to_change(x - 1, y + 1, piece_to_change):
            direction.append((x - 1, y + 1, piece_to_change))
            x -= 1
            y += 1
        if direction and self.has_piece_to_change(x - 1, y + 1, my_piece):
            positions.append(direction)

        y = a
        x = b
        direction = []
        while self.has_piece_to_change(x - 1, y - 1, piece_to_change):
            direction.append((x - 1, y - 1, piece_to_change))
            x -= 1
            y -= 1
        if direction and self.has_piece_to_change(x - 1, y - 1, my_piece):
            positions.append(direction)

        y = a
        x = b
        direction = []
        while self.has_piece_to_change(x + 1, y - 1, piece_to_change):
            direction.append((x + 1, y - 1, piece_to_change))
            x += 1
            y -= 1
        if direction and self.has_piece_to_change(x + 1, y - 1, my_piece):
            positions.append(direction)

        y = a
        x = b
        direction = []
        while self.has_piece_to_change(x + 1, y + 1, piece_to_change):
            direction.append((x + 1, y + 1, piece_to_change))
            x += 1
            y += 1
        if direction and self.has_piece_to_change(x + 1, y + 1, my_piece):
            positions.append(direction)

        return positions

    def reverse_possibles(self, possibles):
        for direction in possibles:
            for x, y, piece in direction:
                self.matrix_board[x][y] = 'W' \
                    if self.player_one == self.actual_player else 'B'

    def play(self, x, y):
        if not(self.validate(x, y)):
            return 'Movement not allowed. Try again.'
        else:
            possibles = self.find_possibility_pieces(x, y)
            if possibles == []:
                return 'No possibilities. Try again.'
            else:
                self.reverse_possibles(possibles)
                self.matrix_board[x][y] = 'W' \
                    if self.player_one == self.actual_player else 'B'
                has_empty = False
                whites = 0
                blacks = 0
                for rows in self.matrix_board:
                    for cell in rows:
                        if cell == 'W':
                            whites += 1
                        elif cell == 'B':
                            blacks += 1
                        if cell == ' ':
                            has_empty = True
                if not has_empty:
                    self.finish()
                    if whites > blacks:
                        result = 'Whites win ' \
                            + str(whites) + ' to ' + str(blacks)
                    elif blacks > whites:
                        result = 'Blacks win ' \
                            + str(blacks) + ' to ' + str(whites)
                    else:
                        result = "It's a tie! --- Whites: " \
                            + str(whites) + "; Blacks: " + str(blacks)
                else:
                    self.change_turn()
                    if whites > blacks:
                        result = 'Whites are going ahead ' \
                            + str(whites) + ' a ' + str(blacks)
                    else:
                        result = 'Blacks are going ahead ' \
                            + str(blacks) + ' to ' + str(whites)
                self.moves.append((x, y, ))
                return result

    @property
    def board(self):
        result = ''
        result += '  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |\n'
        result += '--+---+---+---+---+---+---+---+---+\n'
        for x in xrange(0, 8):
            result += str(x) + ' |'
            for y in xrange(0, 8):
                result += ' ' + self.matrix_board[x][y] + ' |'
            result += '\n'
            result += '--+---+---+---+---+---+---+---+---+\n'
        return result
