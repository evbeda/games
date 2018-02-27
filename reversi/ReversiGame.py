from tablero_reversi import TableroReversi


class ReversiGame(object):

    def __init__(self):
        super(ReversiGame, self).__init__()
        self.playing = True
        self.playingWhites = True
        self.tablero = TableroReversi()

    def next_turn(self):
        if self.playing:
            if self.playingWhites:
                return 'Turn of the whiteones'
            else:
                return 'Turn of the blackones'
        else:
            return 'Game Over'

#    def play(self, column, row):
#        if self.validate_empty(column, row):

    def validate_empty(self, column, row):
        return self.tablero.matrix_tablero[column][row] == 0

#esto es para ver si se puede poner la ficha en la posicion indicada
    def validate_enemy_position(self, column, row):
        searching = 1
        validated = False
        if self.playingWhites:
            searching = 2

        if column+1 <= 8:
            if self.tablero.matrix_tablero[column+1][row] == searching:
                return True
        elif column-1 >= 1:
            if self.tablero.matrix_tablero[column-1][row] == searching:
                return True
        if row+1 <= 8:
            if self.tablero.matrix_tablero[column][row+1] == searching:
                return True
        elif row-1 >= 1:
            if self.tablero.matrix_tablero[column][row-1] == searching:
                return True















