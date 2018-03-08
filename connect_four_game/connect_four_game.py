from game_base import GameBase
from game_base import GameWithTurns


class ConnectFourGame(GameBase, GameWithTurns):

    name = 'Cuatro en linea'
    input_args = 1
    player_one = 'White'
    player_two = 'Black'

    def __init__(self):
        super(ConnectFourGame, self).__init__()

        # fixme-connectfour-2: Spanish?
        self.ficha = ''
        # fixme-connectfour-2: Spanish?
        self.filas = 6
        self.min = 0
        # fixme-connectfour-2: Spanish?
        self.columnas = 7
        # fixme-connectfour-1: Change E's for ' '
        self.board_status = [
            ['E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E'],
        ]

    def play(self, column):
        # fixme-connectfour-4: Remove is_playing condition. Never used.
        if(self.is_playing):
            # fixme-connectfour-3: Should be after 'set_board'
            if(self.empate()):
                self.finish()
                # fixme-connectfour-2: Spanish?
                return 'Empate'
            elif(self.in_board(column)):
                if(
                    self.board_status[0][column] != 'W' and
                    self.board_status[0][column] != 'B'
                ):

                    self.set_board(column)

                    if self.check_win():
                        self.finish()
                        return 'You win'

                    return 'Keep playing'

                else:
                    return 'Full column'
            else:
                # fixme-connectfour-2: Spanish?
                return 'Movimiento no permitido'
        # fixme-connectfour-4: Remove is_playing condition. Never used.
        else:
            return 'Game Over'

    def in_board(self, column):
        # fixme-connectfour-5: Remove isinstance condition.
        # It's already checked in game.py.
        if isinstance(column, int):
            return (
                self.min <= column <= self.columnas
            )
        else:
            return False

    # fixme-connectfour-2: Spanish?
    def empate(self):
        # fixme-connectfour-6: Remove not self.check_win() condition.
        # If check_win executed before 'empate()' in play() it's not necessary.
        if (not self.check_win()):
            count = 0
            for col in range(self.columnas):
                if (
                    self.board_status[0][col] != 'E'
                ):
                    count += 1
            if (count == self.columnas):
                return True
            else:
                return False
        else:
            return False

    # fixme-connectfour-7: Method name is not clear.
    # Does it set the whole board?
    def set_board(self, column):
        # fixme-connectfour-8: for loops VERY similar. Could be refactorized.
        if self.actual_player == self.player_one:
            for x in xrange(5, -1, -1):
                if self.board_status[x][column] == 'E':
                    self.board_status[x][column] = 'W'
                    self.ficha = 'W'
                    self.change_turn()
                    break
        else:
            for x in xrange(5, -1, -1):
                if self.board_status[x][column] == 'E':
                    self.board_status[x][column] = 'B'
                    self.ficha = 'B'
                    self.change_turn()
                    break

    # fixme-connectfour-2: Spanish?
    def win_diagonal_izquierdo(self):
        # fixme-connectfour-2: Spanish?
        for fila in range(self.filas):
            for col in range(self.columnas):
                if(
                    3 <= fila <= 5 and 0 <= col <= 3 and
                    self.board_status[fila][col] == self.ficha and
                    self.board_status[fila - 1][col + 1] == self.ficha and
                    self.board_status[fila - 2][col + 2] == self.ficha and
                    self.board_status[fila - 3][col + 3] == self.ficha
                ):
                    return True
        return False

    # fixme-connectfour-2: Spanish?
    def win_diagonal_derecho(self):
        # fixme-connectfour-2: Spanish?
        for fila in range(self.filas):
            for col in range(self.columnas):
                if(
                    3 <= fila <= 5 and 3 <= col <= 6 and
                    self.board_status[fila][col] == self.ficha and
                    self.board_status[fila - 1][col - 1] == self.ficha and
                    self.board_status[fila - 2][col - 2] == self.ficha and
                    self.board_status[fila - 3][col - 3] == self.ficha
                ):
                    return True
        return False

    def win_horizontal(self):
        # fixme-connectfour-2: Spanish?
        for fila in range(self.filas):
            for col in range(self.columnas):
                if(
                    col <= 3 and
                    self.board_status[fila][col] == self.ficha and
                    self.board_status[fila][col + 1] == self.ficha and
                    self.board_status[fila][col + 2] == self.ficha and
                    self.board_status[fila][col + 3] == self.ficha
                ):
                    return True
        return False

    def win_vertical(self):
        # fixme-connectfour-2: Spanish?
        for fila in range(self.filas):
            for col in range(self.columnas):
                if(
                    fila <= 2 and
                    self.board_status[fila][col] == self.ficha and
                    self.board_status[fila + 1][col] == self.ficha and
                    self.board_status[fila + 2][col] == self.ficha and
                    self.board_status[fila + 3][col] == self.ficha
                ):
                    return True
        return False

    def poster(self):
        poster = "\n"
        poster += "   __ __  _______   ____    _____   ___________ \n"
        poster += "  / // / / ____/ | / / /   /  _/ | / / ____/   |\n"
        poster += " / // /_/ __/ /  |/ / /    / //  |/ / __/ / /| |\n"
        poster += "/__  __/ /___/ /|  / /____/ // /|  / /___/ ___ |\n"
        poster += "  /_/ /_____/_/ |_/_____/___/_/ |_/_____/_/  |_|\n"

        return poster

    def next_turn(self):
            return self.actual_player + ' plays'

    # fixme-connectfour-11: Can get better! Columns indistinguishable.
    @property
    def board(self):
        result = ''
        for x in xrange(0, 6):
            for y in xrange(0, 7):
                result += self.board_status[x][y]
            result += '\n'
        return result

    def check_win(self):
        return (self.win_diagonal_izquierdo() or
                self.win_diagonal_derecho() or
                self.win_horizontal() or
                self.win_vertical()
                )
