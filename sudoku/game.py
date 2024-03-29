from game_base import GameBase
from . import (
    NUMBER_ADDED,
    PLACE_A_NUMBER,
    GAME_OVER,
    YOU_WIN,
    INVALID_INPUT_COLUMN,
    INVALID_INPUT_ROW,
    INVALID_INPUT_VALUE,
)
from .board import Board
from .api import fetch_board
from .invalid_input_exception import InvalidInputException


class SudokuGame(GameBase):

    name = 'Sudoku Game'
    input_args = 3
    input_are_ints = False

    def __init__(self, board=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not board:
            board = fetch_board()
        self.game_board = Board(board)

    def next_turn(self):
        if self.is_playing:
            return PLACE_A_NUMBER
        else:
            return GAME_OVER

    # user_input = "a 1 4"
    def play(self, row, column, value):
        try:
            self.validate_input(row, column, value)
            self.game_board.place((row, int(column)), int(value))
            if self.game_board.is_finished():
                self.finish()
                return YOU_WIN
            return NUMBER_ADDED
        except InvalidInputException as e:
            return str(e)
        except Exception as e:
            return str(e)        

    @property
    def board(self):
        return self.game_board.show_board()

    def validate_input(self, row, column, value):
        errors = ""
        if 'a' <= value.lower() < 'z' or not 0 < int(value) <= 9:
            errors += INVALID_INPUT_VALUE + '\n'
        if 'a' <= column.lower() < 'z' or not 0 < int(column) <= 9:
            errors += INVALID_INPUT_COLUMN + '\n'
        if not 'a' <= row.lower() <= 'z':
            errors += INVALID_INPUT_ROW + '\n'
        if errors:
            raise InvalidInputException(errors)
