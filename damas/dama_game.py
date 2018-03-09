from game_base import GameBase
from game_base import GameWithBoard
from game_base import GameWithTurns


class DamaGameStart(GameWithBoard, GameWithTurns, GameBase):
    name = 'Damas'
    minimum = 0
    _col = 8
    _row = 8
    input_args = 4
    player_one = 'White'
    player_two = 'Black'

    def __init__(self):
        super(DamaGameStart, self).__init__()

        self.set_board([
            ['b', ' ', 'b', ' ', 'b', ' ', 'b', ' '],
            [' ', 'b', ' ', 'b', ' ', 'b', ' ', 'b'],
            ['b', ' ', 'b', ' ', 'b', ' ', 'b', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', 'w', ' ', 'w', ' ', 'w', ' ', 'w'],
            ['w', ' ', 'w', ' ', 'w', ' ', 'w', ' '],
            [' ', 'w', ' ', 'w', ' ', 'w', ' ', 'w']])

    # fixme-damas-9: many actions split them up, don't name var as  x, y, w, z, k, t
    def play_white(self, x1, y1, x2, y2):
        if self.get_value(x1, y1) == 'w' or self.get_value(x1, y1) == 'W':
            if (x2 == x1 - 1 or x2 == x1 + 1):
                if (y2 == y1 - 1 or y2 == y1 + 1):
                    if x2 == 0:
                        self.move(x1, y1, x2, y2, 'W')
                        return 'you became a dama!'
                    else:
                        # fixme-damas-8: dont return two things
                        return self.move(x1, y1, x2, y2, self.get_value(x1, y1))
                else:
                    return 'you cant reach that place!'
            # si hay un espacio en la posicion destino
            elif((self.get_value(x2, y2)) == ' ' and (x2 == abs(x1 - 2))):
                # si va para dcha
                if(y1 < y2):
                    cord_x = x1 - 1
                    cord_y = y1 + 1
                else:
                    cord_x = x1 - 1
                    cord_y = y1 - 1

                if(self.get_value(cord_x, cord_y) == 'b' or
                        self.get_value(cord_x, cord_y) == 'B'):
                    self.eat_piece(cord_x, cord_y)
                    return self.move(x1, y1, x2, y2, self.get_value(x1, y1))
                else:
                    return 'you cant reach that place!'
            return 'you cant reach that place!'
        else:
            return 'This position is outside our board'

    def eat_piece(self, x, y):
        self.set_value(x, y, ' ')
        self.check_if_has_won()

    def check_if_has_won(self):
        if self._playing:
            count = 0
            if (self._turn == self.player_one):
                # fixme-damas-6: use attributes _col _row
                for x in range(0, 8):
                    for y in range(0, 8):
                        board_pos = self.get_value(x, y)
                        if(board_pos == 'b' or board_pos == 'B'):
                            count += 1
                if (count == 0):
                    self.finish()
            else:
                # fixme-damas-6: use attributes _col _row
                for x in range(0, 8):
                    for y in range(0, 8):
                        board_pos = self.get_value(x, y)
                        # fixme-damas-7: DRY attrinute board_pos
                        if (board_pos == 'w' or board_pos == 'W'):
                            count += 1
                if (count == 0):
                    self.finish()

    # fixme-damas-9: many actions split them up
    def play_black(self, x1, y1, x2, y2):
        if self.get_value(x1, y1) == 'b' or self.get_value(x1, y1) == 'B':
            if (x2 == x1 + 1 or x2 == x1 - 1):
                if (y2 == y1 - 1 or y2 == y1 + 1):
                    if x2 == 7:
                        self.move(x1, y1, x2, y2, 'B')
                        return 'you became a dama!'
                    else:
                        # fixme-damas-8: dont return two things
                        return self.move(x1, y1, x2, y2, self.get_value(x1, y1))
                else:
                    return 'This position is outside our board'

            elif((self.get_value(x2, y2)) == ' ' and (x2 == abs(x1 + 2))):
                    # si va para dcha
                if(y1 < y2):
                    cord_x = x1 + 1
                    cord_y = y1 + 1
                else:
                    cord_x = x1 + 1
                    cord_y = y1 - 1
                if(self.get_value(cord_x, cord_y) == 'w' or
                        self.get_value(cord_x, cord_y) == 'W'):
                    self.eat_piece(cord_x, cord_y)
                    return self.move(x1, y1, x2, y2, self.get_value(x1, y1))
                else:
                    return 'you cant reach that place!'
        else:
            return 'No black piece here to move !'

    def play(self, x1, y1, x2, y2):
        if not self.in_board(x1, y1) or not self.in_board(x2, y2):
            if(
                self.actual_player == self.player_one and
                self._playing
            ):
                return self.play_white(x1, y1, x2, y2)
            elif(
                self.actual_player == self.player_two and
                self._playing
            ):
                return self.play_black(x1, y1, x2, y2)
        else:
            return "This position is outside our board"

    def next_turn(self):
        if self._playing:
            return self._turn

    @property
    def board(self):
        result = ' 01234567\n'
        for x in xrange(0, self._col):
            result += str(x)
            for y in xrange(0, self._row):
                result += self.get_value(x, y)
            result += '\n'
        return result

    def move(self, x, y, w, z, pieza):
        self.set_value(x, y, ' ')
        self.set_value(w, z, pieza)
        self.change_turn()
