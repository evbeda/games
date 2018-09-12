from game_base import GameWithBoard


class Board(GameWithBoard):

    board_states = ['empty', 'ready_to_war', 'in_war']

    def __init__(self):
        super(Board, self).__init__()
        self.sunked = []
        self.boats = [0, 0, 0, 0, 0]
        self.cols = 10
        self.rows = 10
        self.create_board(0)
        self.state = self.board_states[0]

    @property
    def board(self):
        return self.get_board

    def set_boat(self, row, column, boat, orientation):
        if (
                (column >= 0 and column < 10) and
                (row >= 0 and row < 10) and
                self.check_position(row, column, boat, orientation)
        ):
            if (orientation == "horizontal") and ((boat + column) <= 10):
                value = self.check_boat(boat)
                # import ipdb; ipdb.set_trace()
                if value == 9:
                    return False
                else:
                    for index in range(0, boat):
                        self.set_value(row, column + index, value)
                    return True
            elif (orientation == "vertical") and ((boat + row) <= 10):
                value = self.check_boat(boat)
                if value == 9:
                    return False
                else:
                    for index in range(0, boat):
                        self.set_value(row + index, column, value)
                    return True
        else:
            return False

    def check_boat(self, boat):
        if boat == 1:
            if self.boats[0] == 0:
                self.boats[0] = 1
                return 1
            else:
                return 9
        elif boat == 2:
            if self.boats[1] == 0:
                self.boats[1] = 1
                return 2
            else:
                return 9
        elif boat == 3:
            if self.boats[2] == 0:
                self.boats[2] = 1
                return 31
            elif self.boats[2] == 1:
                self.boats[2] = 2
                return 32
            else:
                return 9
        elif boat == 4:
            if self.boats[3] == 0:
                self.boats[3] = 1
                return 4
            else:
                return 9
        elif boat == 5:
            if self.boats[4] == 0:
                self.boats[4] = 1
                return 5
            else:
                return 9

    def check_position(self, row, column, boat, orientation):
        if (column >= 0 and column < 10) and (row >= 0 and row < 10):
            if (orientation == "horizontal") and ((boat + column) <= 10):
                for index in range(0, boat):
                    if self.get_value(row, column + index) != 0:
                        return False
                return True
            elif (orientation == "vertical") and ((boat + row) <= 10):
                for index in range(0, boat):
                    if self.get_value(row + index, column) != 0:
                        return False
                return True
        else:
            return False

    def check_cross(self, value):
        self.sunked.append(value)
        if value == 1:
            return "sunked"
        elif value == 2:
            if self.sunked.count(value) == 2:
                return "sunked"
            else:
                return "hit"
        elif value == 31:
            if self.sunked.count(value) == 3:
                return "sunked"
            else:
                return "hit"
        elif value == 32:
            if self.sunked.count(value) == 3:
                return "sunked"
            else:
                return "hit"
        elif value == 4:
            if self.sunked.count(value) == 4:
                return "sunked"
            else:
                return "hit"
        elif value == 5:
            if self.sunked.count(value) == 5:
                return "sunked"
            else:
                return "hit"

    def shoot(self, row, column):
        #import ipdb; ipdb.set_trace()
        if self.get_value(row, column) == 0:
            self.set_value(row, column, '-')
            return "water"
        elif self.get_value(row, column) == 9 or self.get_value(row, column) == "-":
            return "already shoot"
        elif self.get_value(row, column) != 0 and self.get_value(row, column) != 9:
            result = self.check_cross(self.get_value(row, column))
            self.set_value(row, column, 9)
            return result

    def turn_decision_hit(self, result):
        if result == 'hit':
            return True
        return False

    def is_ready_to_war(self):
        if self.boats == [1, 1, 2, 1, 1]:
            self.state = self.board_states[1]
            return True
        else:
            return False

    def mark_shoot(self, row, column, is_hit):
        if self.get_value(row, column) == 0:
            if is_hit:
                character = 'x'
            else:
                character = '-'
            self.set_value(row, column, character)

    def there_are_boats(self):
        for i in range(self.rows):
            for x in range(self.cols):
                # import pdb; pdb.set_trace()
                if self.get_value(i, x) in [1, 2, 31, 32, 4, 5]:
                    return True
        return False
