from game_base import (GameBase,
                       GameWithTurns,
                       GameWithBoard)


class DamaGameStart(GameWithTurns,  GameBase, GameWithBoard):
    _row = 8
    _col = 8
    name = 'Damas'
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
    def play_white(self, x, y, w, z):
        if self.get_value(x, y) == 'w' or self.get_value(x, y) == 'W':
            if (w == x - 1 or w == x + 1):
                if (z == y - 1 or z == y + 1):
                    if w == 0:
                        self.move(x, y, w, z, 'W')
                        return 'you became a dama!'
                    else:
                        # fixme-damas-8: dont return two things
                        return self.move(x, y, w, z, self._board[x][y])
                else:
                    return 'you cant reach that place!'
            # si hay un espacio en la posicion destino
            elif((self.get_value(w, z)) == ' ' and (w == abs(x - 2))):
                # si va para dcha
                if(y < z):
                    k = x - 1
                    t = y + 1
                else:
                    k = x - 1
                    t = y - 1
                if(self.get_value(k, t) == 'b' or
                        self.get_value(k, t) == 'B'):
                    self.eat_piece(k, t)
                    return self.move(x, y, w, z, self.get_value(x, y))
                else:
                    return 'you cant reach that place!'
            return 'you cant reach that place!'
        else:
            return 'No white piece here to move !'

    def eat_piece(self, k, t):
        self.set_value(k, t, ' ')
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
    def play_black(self, x, y, w, z):
        if self.get_value(x, y) == 'b' or self.get_value(x, y) == 'B':
            if (w == x + 1 or w == x - 1):
                if (z == y - 1 or z == y + 1):
                    if w == 7:
                        self.move(x, y, w, z, 'B')
                        return 'you became a dama!'
                    else:
                        # fixme-damas-8: dont return two things
                        return self.move(x, y, w, z, self._board[x][y])
                else:
                    return 'you cant reach that place!'
            elif((self.get_value(w, z)) == ' ' and (w == abs(x + 2))):
                    # si va para dcha
                if(y < z):
                    k = x + 1
                    t = y + 1
                else:
                    k = x + 1
                    t = y - 1
                if(self.get_value(k, t) == 'w' or
                        self.get_value(k, t) == 'W'):
                    self.eat_piece(k, t)
                    return self.move(x, y, w, z, self.get_value(x, y))
                else:
                    return 'you cant reach that place!'
        else:
            return 'No black piece here to move !'

    def play(self, x, y, w, z):
        if not self.valid_movement_inside_board(x, y, w, z):
            if(
                self._turn == self.player_one and
                self._playing
            ):
                return self.play_white(x, y, w, z)
            elif(
                self._turn == self.player_two and
                self._playing
            ):
                return self.play_black(x, y, w, z)
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

    # fixme-damas-10: change metod with GameWithBoard's in_board
    def valid_movement_inside_board(self, x1, y1, x2, y2):
        return (x1 < 0 or x1 > 7 or x2 < 0 or x2 > 7 or
                y1 < 0 or y1 > 7 or y2 < 0 or y2 > 7)
