from game_base import GameBase
from game_base import GameWithBoard
from game_base import GameWithTurns


class ReversiGame(GameBase, GameWithTurns, GameWithBoard):

    name = 'Reversi'
    input_args = 2

    cols = 8
    rows = 8
    player_one = 'White'
    player_two = 'Black'

    def __init__(self, *args, **kwargs):
        super(ReversiGame, self).__init__(*args, **kwargs)
        self.create_board(' ')
        self.set_value(3, 3, 'B')
        self.set_value(3, 4, 'W')
        self.set_value(4, 4, 'B')
        self.set_value(4, 3, 'W')
        self.whites = 0
        self.blacks = 0

    def next_turn(self):
        return self.actual_player

    def validate(self, x, y):
        if not self.in_board(x, y):
            return 'Values must be between 0 and 7'
        else:
            if self.get_value(x, y) == ' ':
                return True
            return False

    def has_piece_to_change(self, x, y, piece):
        if (self.in_board(x, y) and
                self.get_value(x, y) == piece):
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
                if self.player_one == self.actual_player:
                    self.set_value(x, y, 'W')
                else:
                    self.set_value(x, y, 'B')

    def play(self, x, y):
        if not self.check_can_play():
            self.change_turn()
            if not self.check_can_play():
                self.finish()
                return 'Game over!'
            return 'No possible moves, turn changes'
        if not self.validate(x, y):
            return 'Movement not allowed. Try again.'
        else:
            possibles = self.find_possibility_pieces(x, y)
            if possibles == []:
                return 'No possibilities. Try again.'
            else:
                self.reverse_possibles(possibles)
                if self.player_one == self.actual_player:
                    self.set_value(x, y, 'W')
                else:
                    self.set_value(x, y, 'B')
                self.whites = 0
                self.blacks = 0
                if not self.check_empty():
                    self.finish()
                    result = self.show_result_finish()
                else:
                    self.change_turn()
                    result = self.show_partial_results()
                return result

    def check_can_play(self):
        result = []
        for x in xrange(8):
            for y in xrange(8):
                if self.get_value(x, y) == ' ':
                    if self.find_possibility_pieces(x, y):
                        result.append(self.find_possibility_pieces(x, y))
        return result

    def check_empty(self):
        has_empty = False
        for rows in self.get_board:
            for cell in rows:
                if cell == 'W':
                    self.whites += 1
                elif cell == 'B':
                    self.blacks += 1
                if cell == ' ':
                    has_empty = True
        return has_empty

    def show_result_finish(self):
        if self.whites > self.blacks:
            result = 'Whites win ' \
                + str(self.whites) + ' to ' + str(self.blacks)
        elif self.blacks > self.whites:
            result = 'Blacks win ' \
                + str(self.blacks) + ' to ' + str(self.whites)
        else:
            result = "It's a tie! --- Whites: " \
                + str(self.whites) + "; Blacks: "\
                + str(self.blacks)
        return result

    def show_partial_results(self):
        if self.whites > self.blacks:
            result = 'Whites are going ahead ' \
                + str(self.whites) + ' a ' + str(self.blacks)
        else:
            result = 'Blacks are going ahead ' \
                + str(self.blacks) + ' to ' + str(self.whites)
        return result

    @property
    def board(self):
        result = ''
        result += '  |'
        for x in xrange(self.cols):
            result += ' ' + str(x) + ' |'
        result += '\n--+'
        for y in xrange(self.cols):
            result += '---+'
        result += '\n'
        for x in xrange(0, 8):
            result += str(x) + ' |'
            for y in xrange(0, 8):
                result += ' ' + self.get_value(x, y) + ' |'
            result += '\n'
            result += '--+---+---+---+---+---+---+---+---+\n'
        return result
