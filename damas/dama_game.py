from game_base import (GameBase,
                       GameWithTurns)


class DamaGameStart(GameBase, GameWithTurns):

    name = 'Damas'
    input_args = 4
    player_one = 'White'
    player_two = 'Black'

    def __init__(self):
        super(DamaGameStart, self).__init__()
        self.board_status = [
            ['b', ' ', 'b', ' ', 'b', ' ', 'b', ' '],
            [' ', 'b', ' ', 'b', ' ', 'b', ' ', 'b'],
            ['b', ' ', 'b', ' ', 'b', ' ', 'b', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', 'w', ' ', 'w', ' ', 'w', ' ', 'w'],
            ['w', ' ', 'w', ' ', 'w', ' ', 'w', ' '],
            [' ', 'w', ' ', 'w', ' ', 'w', ' ', 'w']]
        self.winner = ''
        self.moves = []

    def play_white(self, x, y, w, z):
        if self.board_status[x][y] == 'w' or self.board_status[x][y] == 'W':
            if (w == x - 1 or w == x + 1):
                if (z == y - 1 or z == y + 1):
                    if w == 0:
                        self.move(x, y, w, z, 'W')
                        return 'you became a dama!'
                    else:
                        return self.move(x, y, w, z, self.board_status[x][y])
                else:
                    return 'you cant reach that place!'
            # si hay un espacio en la posicion destino
            elif((self.board_status[w][z]) == ' ' and (w == abs(x - 2))):
                # si va para dcha
                if(y < z):
                    k = x - 1
                    t = y + 1
                else:
                    k = x - 1
                    t = y - 1
                if(self.board_status[k][t] == 'b' or
                        self.board_status[k][t] == 'B'):
                    self.eat_piece(k, t)
                    return self.move(x, y, w, z, self.board_status[x][y])
                else:
                    return 'you cant reach that place!'
            return 'you cant reach that place!'
        else:
            return 'No white piece here to move !'

    def eat_piece(self, k, t):
        self.board_status[k][t] = ' '
        self.check_if_has_won()

    def check_if_has_won(self):
        if self._playing:
            count = 0
            if (self._turn == self.player_one):
                for x in range(0, 8):
                    for y in range(0, 8):
                        board_pos = self.board_status[x][y]
                        if(board_pos == 'b' or board_pos == 'B'):
                            count += 1
                if (count == 0):
                    self.finish()
                    self.winner = self.player_one
            else:
                for x in range(0, 8):
                    for y in range(0, 8):
                        board_pos = self.board_status[x][y]
                        if (board_pos == 'w' or board_pos == 'W'):
                            count += 1
                if (count == 0):
                    self.finish()
                    self.winner = 'Black'

    def play_black(self, x, y, w, z):
        if self.board_status[x][y] == 'b' or self.board_status[x][y] == 'B':
            if (w == x + 1 or w == x - 1):
                if (z == y - 1 or z == y + 1):
                    if w == 7:
                        self.move(x, y, w, z, 'B')
                        return 'you became a dama!'
                    else:
                        return self.move(x, y, w, z, self.board_status[x][y])
                else:
                    return 'you cant reach that place!'
            elif((self.board_status[w][z]) == ' ' and (w == abs(x + 2))):
                    # si va para dcha
                if(y < z):
                    k = x + 1
                    t = y + 1
                else:
                    k = x + 1
                    t = y - 1
                if(self.board_status[k][t] == 'w' or
                        self.board_status[k][t] == 'W'):
                    self.eat_piece(k, t)
                    return self.move(x, y, w, z, self.board_status[x][y])
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
            if (self._turn == self.player_one):
                return "Plays White"
            else:
                return "Plays Black"
        else:
            return self.winner + " wins."

    @property
    def board(self):
        result = ' 01234567\n'
        for x in xrange(0, 8):
            result += str(x)
            for y in xrange(0, 8):
                result += self.board_status[x][y]
            result += '\n'
        return result

    def move(self, x, y, w, z, pieza):
        self.board_status[x][y] = ' '
        self.board_status[w][z] = pieza
        self.change_turn()

    def valid_movement_inside_board(self, x1, y1, x2, y2):
        return (x1 < 0 or x1 > 7 or x2 < 0 or x2 > 7 or
                y1 < 0 or y1 > 7 or y2 < 0 or y2 > 7)
