

class ConnectFourGame(object):

    def __init__(self):
        super(ConnectFourGame, self).__init__()
        self.playing = True
        self.turn = 0
        self.ficha = ''
        self.filas = 6
        self.min = 0
        self.columnas = 7
        self.board_status = [
            ['E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E', 'E', 'E'],
        ]

    def play(self, column):
        if(self.playing):
            if(self.empate()):
                self.playing = False
                return 'Empate'
            elif(self.in_board(column)):
                if(
                    self.board_status[0][column] != 'W' and
                    self.board_status[0][column] != 'B'
                ):

                    self.set_board(column)

                    if (self.win_diagonal_izquierdo()):
                        self.playing = False
                        return 'You win'
                    elif (self.win_diagonal_derecho()):
                        self.playing = False
                        return 'You win'
                    elif(self.win_horizontal()):
                        self.playing = False
                        return 'You win'
                    elif(self.win_vertical()):
                        self.playing = False
                        return 'You win'

                    return 'Keep playing'

                else:
                    return 'Full column'
            else:
                return 'Movimiento no permitido'
        else:
            return 'Game Over'

    def in_board(self, column):
        if isinstance(column, int):
            return not(
                self.columnas < column or
                self.min > column
            )
        else:
            return False

    def empate(self):
        if (
            not self.win_diagonal_izquierdo() and
            not self.win_diagonal_derecho() and
            not self.win_horizontal() and
            not self.win_vertical()
        ):
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

    def set_board(self, column):
        if self.turn == 0:
            for x in xrange(5, -1, -1):
                if self.board_status[x][column] == 'E':
                    self.board_status[x][column] = 'W'
                    self.ficha = 'W'
                    self.turn = 1
                    break
        else:
            for x in xrange(5, -1, -1):
                if self.board_status[x][column] == 'E':
                    self.board_status[x][column] = 'B'
                    self.ficha = 'B'
                    self.turn = 0
                    break

    def win_diagonal_izquierdo(self):
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

    def win_diagonal_derecho(self):
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

    def playingW(self, turn):
        if self.turn == 0:
            return 'White plays'
        else:
            return 'Black plays'

    @property
    def board(self):
            result = ''
            for x in xrange(0, 6):
                for y in xrange(0, 7):
                    result += self.board_status[x][y]
                result += '\n'
            return result
