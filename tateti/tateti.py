class Tateti(object):

    tablero = []
    fila = [0, 0, 0]
    col = 3
    row = 3

    def create_tablero(self):
        for x in range(0, self.row):
            self.tablero.append(self.fila)
        return self.tablero
