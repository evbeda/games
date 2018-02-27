class TableroReversi(object):
    """docstring for TableroReversi"""
    def __init__(self):
        super(TableroReversi, self).__init__()
        self.matrix_tablero = [[0 for x in range(8)]for y in range(8)]
        self.matrix_tablero[4][4] = 1
        self.matrix_tablero[5][5] = 1
        self.matrix_tablero[4][5] = 2
        self.matrix_tablero[5][4] = 2
