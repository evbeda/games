from copy import deepcopy
from wumpus.constants import (
    COL,
    HIDE_CELL,
    HOLES,
    LOSE,
    ROW,
    GOLD_QUANTITY,
    GOLD,
    VISITED_CELL,
    WIN,
    WUMPUS_QUANTITY,
    WUMPUS,
    SWORDS_QUANTITY,
    PLAYER,
    SCORE_GAME,
    MOVES,
    MESSAGE_NEXT_TURN,
)
import random


class WumpusGame:

    name = 'Wumpus . An unforgettable Adventure'
    input_args = 2
    input_are_ints = False

    def __init__(self) -> None:
        self.is_playing = True
        self._board = [['' for j in range(COL)] for i in range(ROW)]
        self.place_player()

        self.place_item(GOLD, GOLD_QUANTITY)
        self.place_item(WUMPUS, WUMPUS_QUANTITY)
        self.place_item(HOLES, WUMPUS_QUANTITY)
        self.swords = SWORDS_QUANTITY
        self.collected_gold = 0
        self.visited = ()
        self.score = 0
        self.result_of_game = str()
        self.message_game_over = str()
        self.memory = {}

    def place_player(self):
        self._board[0][0] = PLAYER

    def place_item(self, item, quantity):
        for _ in range(quantity):
            while True:  # busca hasta encontrar una posicion libre
                row = random.randint(0, ROW - 1)
                col = random.randint(0, COL - 1)
                if self._is_valid(row, col, item):
                    self._board[row][col] = item
                    break

    def _is_valid(self, row, col, item) -> bool:
        valid = self.check_is_empty(row, col)
        if item == HOLES and valid:
            valid = self._valid_hole(row, col)
        return valid

    def position_finder(self, item):
        position_list = []
        for i in range(ROW):
            for j in range(COL):
                if self._board[i][j] == item:
                    position_list.append((i, j))
        return position_list

    def check_is_empty(self, row, col):
        cell = self._board[row][col]
        return cell == ''

    def move_player_transaction(self, new_row, new_col):

        row, col = self.position_finder(PLAYER)[0]
        self._board[row][col] = VISITED_CELL
        self._board[new_row][new_col] = PLAYER
        self.modify_score(SCORE_GAME["move"])

    def there_is_item(self, item, row: int, col: int) -> bool:
        return (row, col) in self.position_finder(item)

    def there_is_gold(self, row: int, col: int) -> bool:
        return (row, col) in self.position_finder(GOLD)

    def delete_item_on_position(self, item, row, col):
        self._board[row][col] = self._board[row][col].replace(item, '')

    def _posible_position(self, row, col):
        positions = {
            "nort": (row - 1, col),
            "sout": (row + 1, col),
            "east": (row, col + 1),
            "west": (row, col - 1)
        }

        if row - 1 < 0:
            del (positions['nort'])
        if row + 1 >= ROW:
            del (positions['sout'])
        if col + 1 >= COL:
            del (positions['east'])
        if col - 1 < 0:
            del (positions['west'])

        return list(positions.values())

    def move_and_win_gold(self, row, col):
        self.delete_item_on_position(GOLD, row, col)
        self.move_player_transaction(row, col)
        self.modify_score(SCORE_GAME["gold_wumpus"])
        self.count_golds()

    def move_and_game_over(self, reason):

        player_row, player_col = self.position_finder(PLAYER)[0]
        self._board[player_row][player_col] = VISITED_CELL
        self.game_over(LOSE, reason)

    def modify_score(self, score_to_modify):
        self.score += score_to_modify

    def game_over(self, result: str, reason: str = ''):

        self.is_playing = False
        self.result_of_game = result

        message = "Bad Luck! You lose. "

        if result == WIN:
            message = 'CONGRATS!! You WIN!!! '
        elif reason == WUMPUS:
            message += "You have eaten by a Wumpus. "

        if reason == HOLES:
            message += "You falled into a hole. "

        message += "Your final score is "

        self.message_game_over = message

    def shoot_arrow(self, row, col):
        if self.swords > 0:
            if WUMPUS in self._board[row][col]:
                self._board[row][col] = VISITED_CELL
                self.modify_score(SCORE_GAME["gold_wumpus"])
            else:
                self.modify_score(SCORE_GAME["lost_shoot"])
            self.swords -= 1
        else:
            raise Exception("Error. You don't have any arrow")

    def move_player(self, row: int, col: int):

        if self.there_is_item(GOLD, row, col):
            self.move_and_win_gold(row, col)

        elif self.there_is_item(WUMPUS, row, col):
            self.move_and_game_over(WUMPUS)

        elif self.there_is_item(HOLES, row, col):
            self.move_and_game_over(HOLES)

        else:
            self.move_player_transaction(row, col)

    def find_coord(self, coord):
        row, col = self.position_finder(PLAYER)[0]
        result = ()
        if coord == "w" and row - 1 >= 0:
            result = (row - 1, col)
        elif coord == "s" and row + 1 <= 7:
            result = (row + 1, col)
        elif coord == "a" and col - 1 >= 0:
            result = (row, col - 1)
        elif coord == "d" and col + 1 <= 7:
            result = (row, col + 1)
        return result

    def manager_move(self, action, direction):
        directions = self.find_coord(direction)
        if action == MOVES['move'] and directions:
            self.move_player(directions[0], directions[1])
        elif action == MOVES['shoot'] and directions:
            self.shoot_arrow(directions[0], directions[1])
        else:
            raise Exception("Out of range move")

    def find_signal(self, item, row, col):
        item_array = list(item)
        positions = self._posible_position(row, col)
        wumpus_flag = False
        hole_flag = False
        for p_row, p_col in positions:

            if WUMPUS in self._board[p_row][p_col]:
                wumpus_flag = True
            if HOLES in self._board[p_row][p_col]:
                hole_flag = True
        if wumpus_flag:
            item_array[2] = "+"
        if hole_flag:
            item_array[0] = "~"
        return "".join(item_array)

    def parse_cell(self, row: int, col: int) -> str:
        cell = self._board[row][col]

        if cell == PLAYER or cell == VISITED_CELL:
            cell = ' ' + cell + ' '
            cell = self.find_signal(cell, row, col)

        else:
            cell = HIDE_CELL

        return cell

    def next_turn(self):
        result = ""
        if self.is_playing:
            result = MESSAGE_NEXT_TURN
        else:
            result = self.message_game_over + str(self.score)

        return result

    @property
    def board(self):
        user_board = str()

        for row in range(ROW):
            for col in range(COL):
                user_board += self.parse_cell(row, col)

            user_board += '\n'

        return user_board

    def count_golds(self):
        golds = self.position_finder(GOLD)
        if not golds:
            self.game_over(WIN)

    def _find_posible_moves_gold(self, row, col, board):
        positions = self._posible_position(row, col)
        final_positions = []
        for row, col in positions:
            if HOLES not in board[row][col]:
                final_positions.append((row, col))
        final_positions.sort()
        return final_positions

    def _find_gold_recursive(self, row, col, gold_position, board, visited):
        visited.append((row, col,))
        if (row, col) == gold_position:
            return True
        possible_moves = self._posible_position(row, col)
        for row_next, col_next in possible_moves:
            if (
                (row_next, col_next) not in visited and
                board[row_next][col_next] != HOLES and
                self._find_gold_recursive(row_next, col_next, gold_position, board, visited)
            ):
                return True
        return False

    def _valid_hole(self, row, col) -> bool:

        aux_board = deepcopy(self._board)
        aux_board[row][col] = HOLES
        golds = self.position_finder(GOLD)
        for gold_position in golds:
            if not self._find_gold_recursive(0, 0, gold_position, aux_board, []):
                return False
        return True

    def play(self, action, direction):
        try:
            self.manager_move(action, direction)
            result = f"Your score is {str(self.score)}"
            if not self.is_playing:
                result = self.message_game_over + str(self.score)
        except Exception:
            return "Bad move"
        return result
