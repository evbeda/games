from game_base import (
    GameBase,
    GameWithBoard,
    GameWithTurns,
)


class ReversiGame(GameWithTurns, GameWithBoard, GameBase):

    name = 'Reversi'
    input_args = 2

    cols = 8
    rows = 8
    player_one = 'White'
    player_two = 'Black'

    def __init__(self, *args, **kwargs):
        super(ReversiGame, self).__init__(name=self.player_one, name2=self.player_two, *args, **kwargs)
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

    def all_directions(self):
        return (
            (x_sign_dir, y_sign_dir)
            for x_sign_dir in range(-1, 2)
            for y_sign_dir in range(-1, 2)
            if x_sign_dir != 0 or y_sign_dir != 0
        )

    def string_from(self, x, y, dx, dy):
        while True:
            x += dx
            y += dy
            if not self.in_board(x, y):
                break
            if self.get_value(x, y) == ' ':
                break
            yield {
                'x': x,
                'y': y,
                'value': self.get_value(x, y),
            }

    def longest_capture_prefix(self, positions, target):
        captured = []
        for position in positions:
            if position['value'] == target:
                captured.append(position)
            else:
                return captured
        return []

    def captures(self, x, y, target):
        captured = []
        for dx, dy in self.all_directions():
            captured.extend(
                self.longest_capture_prefix(
                    self.string_from(x, y, dx, dy),
                    target,
                )
            )
        return captured

    def find_possibility_pieces(self, x, y):
        if self.player_one == self.actual_player:
            piece_to_change = 'B'
        else:
            piece_to_change = 'W'
        return self.captures(x, y, piece_to_change)

    def reverse_possibles(self, possibles):
        for possible in possibles:
            piece = 'W' if self.player_one == self.actual_player else 'B'
            self.set_value(
                possible['x'],
                possible['y'],
                piece,
            )

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
        for x in range(8):
            for y in range(8):
                if self.get_value(x, y) == ' ':
                    if self.find_possibility_pieces(x, y):
                        return True
        return False

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

    def poster(self):
        poster = ''
        poster += ' _______  _______           _______  _______  _______ _________\n'
        poster += '(  ____ )(  ____ \|\     /|(  ____ \(  ____ )(  ____ \\__   __/\n'
        poster += '| (    )|| (    \/| )   ( || (    \/| (    )|| (    \/   ) (   \n'
        poster += '| (____)|| (__    | |   | || (__    | (____)|| (_____    | |   \n'
        poster += '|     __)|  __)   ( (   ) )|  __)   |     __)(_____  )   | |   \n'
        poster += '| (\ (   | (       \ \_/ / | (      | (\ (         ) |   | |   \n'
        poster += '| ) \ \__| (____/\  \   /  | (____/\| ) \ \__/\____) |___) (___\n'
        poster += '|/   \__/(_______/   \_/   (_______/|/   \__/\_______)\_______/\n'

    @property
    def board(self):
        result = ''
        result += '  |'
        for x in range(self.cols):
            result += ' ' + str(x) + ' |'
        result += '\n--+'
        for y in range(self.cols):
            result += '---+'
        result += '\n'
        for x in range(0, 8):
            result += str(x) + ' |'
            for y in range(0, 8):
                result += ' ' + self.get_value(x, y) + ' |'
            result += '\n'
            result += '--+---+---+---+---+---+---+---+---+\n'
        return result
