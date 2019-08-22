import math
from . import (
    NOT_MODIFIABLE,
    REPEATED_ON_COLUMN,
    REPEATED_ON_ROW,
    REPEATED_ON_REGION,
)


class Board:
    def __init__(self, board):
        self.board = self.build_board(board)

    def build_board(self, board):
        return {
            "a": [
                {"val": i, "mod": True} if i == " "
                else {"val": i, "mod": False}
                for i in board[0:9]
            ],
            "b": [
                {"val": i, "mod": True} if i == " "
                else {"val": i, "mod": False}
                for i in board[9:18]
            ],
            "c": [
                {"val": i, "mod": True} if i == " "
                else {"val": i, "mod": False}
                for i in board[18:27]
            ],
            "d": [
                {"val": i, "mod": True} if i == " "
                else {"val": i, "mod": False}
                for i in board[27:36]
            ],
            "e": [
                {"val": i, "mod": True} if i == " "
                else {"val": i, "mod": False}
                for i in board[36:45]
            ],
            "f": [
                {"val": i, "mod": True} if i == " "
                else {"val": i, "mod": False}
                for i in board[45:54]
            ],
            "g": [
                {"val": i, "mod": True} if i == " "
                else {"val": i, "mod": False}
                for i in board[54:63]
            ],
            "h": [
                {"val": i, "mod": True} if i == " "
                else {"val": i, "mod": False}
                for i in board[63:72]
            ],
            "i": [
                {"val": i, "mod": True} if i == " "
                else {"val": i, "mod": False}
                for i in board[72:81]
            ],
        }

    def is_modifiable(self, row, column):
        board_row = self.board[row.lower()]
        board_colum = int(column - 1)
        return board_row[board_colum]["mod"]

    def validate_row(self, row, value):
        board_row = self.board[row.lower()]
        board_row_numbers = [cell["val"] for cell in board_row]
        return str(value) not in board_row_numbers

    def validate_column(self, column, value):
        board_column_numbers = [
            row[column - 1]["val"]
            for row in self.board.values()]
        return str(value) not in board_column_numbers

    def get_region(self, row, column):
        # column_region is like 1, 2, 3
        column_region = math.ceil(column / 3)
        # column_keys is like [1,2,3], [4,5,6], [7,8,9]
        column_keys = [
            key for key in range(1, 10) if math.ceil(key / 3) == column_region
        ]

        # row_region is like 1, 2, 3
        row_region = math.ceil(self.letter_to_number(row) / 3)
        # row_keys is like ['a','b','c'], ['d','e','f'], ['g','h','i']
        row_keys = [
            self.number_to_letter(key)
            for key in range(1, 10)
            if math.ceil(key / 3) == row_region
        ]

        region_numbers = [
            self.board[r][c - 1]["val"] for r in row_keys for c in column_keys
        ]
        return region_numbers

    def validate_region(self, row, column, value):
        board_region_numbers = self.get_region(row, column)
        return str(value) not in board_region_numbers

    def letter_to_number(self, letter):
        return ord(letter.lower()) - 96

    def number_to_letter(self, number):
        return chr(number + 96)

    def validate_number(self, coordinates, value):
        row, column = coordinates
        errors = []
        if not self.is_modifiable(row, column):
            errors.append(NOT_MODIFIABLE)
        if not self.validate_row(row, value):
            errors.append(REPEATED_ON_ROW)
        if not self.validate_column(column, value):
            errors.append(REPEATED_ON_COLUMN)
        if not self.validate_region(row, column, value):
            errors.append(REPEATED_ON_REGION)
        if errors:
            raise Exception(', '.join(errors))

    def place(self, coordinates, value):
        value = str(value)
        row, column = coordinates
        self.validate_number(coordinates, value)
        self.board[row][column - 1]["val"] = value

    def is_finished(self):
        return all(
            column['val'] != ' '
            for row in self.board
            for column in self.board[row])

    def show_board(self):
        ret = ""
        for k, row in self.board.items():
            for index, item in enumerate(row):
                ret += item["val"] + " "
                if index in [2, 5]:
                    ret += "|"
            ret += "\n"
            if k in ['c', 'f']:
                ret += "------+------+------\n"
        return ret
