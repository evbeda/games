
WIN = 'WIN'
LOSE = 'LOSE'
COL = 15
ROW = 8
GOLD_QUANTITY = 8
SWORDS_QUANTITY = 10
WUMPUS_QUANTITY = 8
HOLES_QUANTITY = 8
GOLD = "G"
WUMPUS = "W"
HOLES = "O"
PLAYER = "J"
SIGNAL_WUMPUS = "+"
SIGNAL_HOLE = "~"
PLAYER = "J"
ALL_ELEMENTS = "GWOJ+~J"
ITEMS_DICTIONARY = {"O": "~", "W": "+"}

SCORE_GAME = {"move": -10, "gold_wumpus": 1000, "lost_shoot": -50}
MOVES = {"shoot": "z", "move": "m"}

MOVES_DIRECTION = {"north": "w", "west": "a", "east": "d", "south": "s"}

VISITED_CELL = ' '
VISITED_CELL_USER = '   '
HIDE_CELL = '###'
PLAYER_CELL = ' J '
EMPTY_CELL = ''

MESSAGE_NEXT_TURN = "Please select your next move. \n"\
                    " Use 'z' for shoot a row or 'm' to move \n"\
                    " And 'a', 'w', 's', 'd' to select the direction \n"

MESSAGE_GAME_OVER = "Bad Luck! You lose. Your final score is "
