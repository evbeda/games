from .constants import GOLD, HOLES, PLAYER, ROW, COL, VISITED_CELL, WUMPUS
from copy import deepcopy

SCENARIO_1 = [['' for j in range(COL)] for i in range(ROW)]
SCENARIO_1[0][0] = "J"

SCENARIO_2 = [['' for j in range(COL)] for i in range(ROW)]
SCENARIO_2[1][3] = "J"

SCENARIO_3 = [['' for j in range(COL)] for i in range(ROW)]
SCENARIO_3[3][5] = "J"

SCENARIO_4 = [['' for j in range(COL)] for i in range(ROW)]

SCENARIO_5 = [['' for j in range(COL)] for i in range(ROW)]
SCENARIO_5[2][4] = "J"

SCENARIO_TEST_GOLD = [['' for j in range(COL)] for i in range(ROW)]
SCENARIO_TEST_GOLD[2][4] = GOLD
SCENARIO_TEST_GOLD[4][5] = GOLD
SCENARIO_TEST_GOLD[7][14] = GOLD
SCENARIO_TEST_GOLD[3][4] = GOLD
SCENARIO_TEST_GOLD[6][4] = GOLD
SCENARIO_TEST_GOLD[5][5] = GOLD


SCENARIO_TEST_DELETE = [['' for j in range(COL)] for i in range(ROW)]
SCENARIO_TEST_DELETE[5][5] = GOLD
SCENARIO_TEST_DELETE[7][8] = WUMPUS
SCENARIO_TEST_DELETE[7][14] = WUMPUS
SCENARIO_TEST_DELETE[2][10] = GOLD
SCENARIO_TEST_DELETE[3][4] = PLAYER

# include in this scenario the signal of danger when they are already encoded
SCENARIO_DANGER_SIGNAL_HOLES = [["" for j in range(COL)] for i in range(ROW)]
SCENARIO_DANGER_SIGNAL_HOLES[0][0] = "J"
SCENARIO_DANGER_SIGNAL_HOLES[1][1] = "O"

SCENARIO_DANGER_LEFT_DOWN = [["" for j in range(COL)] for i in range(ROW)]
SCENARIO_DANGER_LEFT_DOWN[0][0] = "J"
SCENARIO_DANGER_LEFT_DOWN[7][0] = "O"

SCENARIO_DANGER_RIGTH_DOWN = [["" for j in range(COL)] for i in range(ROW)]
SCENARIO_DANGER_RIGTH_DOWN[0][0] = "J"
SCENARIO_DANGER_RIGTH_DOWN[7][7] = "O"

SCENARIO_DANGER_RIGTH_UP = [["" for j in range(COL)] for i in range(ROW)]
SCENARIO_DANGER_RIGTH_UP[0][0] = "J"
SCENARIO_DANGER_RIGTH_UP[0][7] = "O"

SCENARIO_DANGER_LEFT = [["" for j in range(COL)] for i in range(ROW)]
SCENARIO_DANGER_LEFT[0][0] = "J"
SCENARIO_DANGER_LEFT[4][0] = "O"

SCENARIO_DANGER_RIGTH = [["" for j in range(COL)] for i in range(ROW)]
SCENARIO_DANGER_RIGTH[0][0] = "J"
SCENARIO_DANGER_RIGTH[4][7] = "O"

SCENARIO_DANGER_UP = [["" for j in range(COL)] for i in range(ROW)]
SCENARIO_DANGER_UP[0][0] = "J"
SCENARIO_DANGER_UP[0][4] = "O"

SCENARIO_DANGER_DOWN = [["" for j in range(COL)] for i in range(ROW)]
SCENARIO_DANGER_DOWN[0][0] = "J"
SCENARIO_DANGER_DOWN[7][4] = "O"

SCENARIO_WIN_GOLD = [['' for j in range(COL)] for i in range(ROW)]
SCENARIO_WIN_GOLD[5][5] = PLAYER
SCENARIO_WIN_GOLD[5][4] = GOLD
SCENARIO_WIN_GOLD[5][6] = GOLD
SCENARIO_WIN_GOLD[4][5] = GOLD
SCENARIO_WIN_GOLD[6][5] = GOLD


SCENARIO_DANGER_COMPLETE_INIT = [["" for j in range(COL)] for i in range(ROW)]
SCENARIO_DANGER_COMPLETE_INIT[0][0] = "J"
SCENARIO_DANGER_COMPLETE_INIT[1][1] = "O"

SCENARIO_DANGER_COMPLETE_FINAL = deepcopy(SCENARIO_DANGER_COMPLETE_INIT)
SCENARIO_DANGER_COMPLETE_FINAL[0][1] = "~"
SCENARIO_DANGER_COMPLETE_FINAL[2][1] = "~"
SCENARIO_DANGER_COMPLETE_FINAL[1][2] = "~"
SCENARIO_DANGER_COMPLETE_FINAL[1][0] = "~"

SCENARIO_DANGER_LEFT_DOWN_INIT = [["" for j in range(COL)] for i in range(ROW)]
SCENARIO_DANGER_LEFT_DOWN_INIT[0][0] = "J"
SCENARIO_DANGER_LEFT_DOWN_INIT[0][7] = "W"

SCENARIO_DANGER_LEFT_DOWN_FINAL = deepcopy(SCENARIO_DANGER_LEFT_DOWN_INIT)
SCENARIO_DANGER_LEFT_DOWN_FINAL[0][6] = "+"
SCENARIO_DANGER_LEFT_DOWN_FINAL[0][8] = "+"
SCENARIO_DANGER_LEFT_DOWN_FINAL[1][7] = "+"

SCENARIO_DANGER_RIGTH_DOWN_INI = [["" for j in range(COL)] for i in range(ROW)]
SCENARIO_DANGER_RIGTH_DOWN_INI[0][0] = "J"
SCENARIO_DANGER_RIGTH_DOWN_INI[7][7] = "W"

SCENARIO_DANGER_RIGTH_DOWN_FINAL = deepcopy(SCENARIO_DANGER_RIGTH_DOWN_INI)
SCENARIO_DANGER_RIGTH_DOWN_FINAL[7][6] = "+"
SCENARIO_DANGER_RIGTH_DOWN_FINAL[7][8] = "+"
SCENARIO_DANGER_RIGTH_DOWN_FINAL[6][7] = "+"

SCENARIO_DANGER_DOWN_INITI = [["" for j in range(COL)] for i in range(ROW)]
SCENARIO_DANGER_DOWN_INITI[0][0] = "J"
SCENARIO_DANGER_DOWN_INITI[7][4] = "W"

SCENARIO_DANGER_DOWN_FINAL = deepcopy(SCENARIO_DANGER_DOWN_INITI)
SCENARIO_DANGER_DOWN_FINAL[7][3] = "+"
SCENARIO_DANGER_DOWN_FINAL[6][4] = "+"
SCENARIO_DANGER_DOWN_FINAL[7][5] = "+"


SCENARIO_CROSS_ELEMENT_INIT = [["" for j in range(COL)] for i in range(ROW)]
SCENARIO_CROSS_ELEMENT_INIT[0][0] = "J"
SCENARIO_CROSS_ELEMENT_INIT[4][4] = "W"
SCENARIO_CROSS_ELEMENT_INIT[4][6] = "W"

SCENARIO_CROSS_ELEMENT_FINAL = deepcopy(SCENARIO_CROSS_ELEMENT_INIT)
SCENARIO_CROSS_ELEMENT_FINAL[3][4] = "+"
SCENARIO_CROSS_ELEMENT_FINAL[3][6] = "+"
SCENARIO_CROSS_ELEMENT_FINAL[4][3] = "+"
SCENARIO_CROSS_ELEMENT_FINAL[4][5] = "+"
SCENARIO_CROSS_ELEMENT_FINAL[4][7] = "+"
SCENARIO_CROSS_ELEMENT_FINAL[5][4] = "+"
SCENARIO_CROSS_ELEMENT_FINAL[5][6] = "+"

SCENARIO_CROSS_DIF_ELEMENT_INI = [["" for j in range(COL)] for i in range(ROW)]
SCENARIO_CROSS_DIF_ELEMENT_INI[0][0] = "J"
SCENARIO_CROSS_DIF_ELEMENT_INI[4][4] = "W"
SCENARIO_CROSS_DIF_ELEMENT_INI[4][6] = "O"

SCENARIO_CROSS_DIF_ELEMENT_FIN = deepcopy(SCENARIO_CROSS_DIF_ELEMENT_INI)
SCENARIO_CROSS_DIF_ELEMENT_FIN[3][4] = "+"
SCENARIO_CROSS_DIF_ELEMENT_FIN[3][6] = "~"
SCENARIO_CROSS_DIF_ELEMENT_FIN[4][3] = "+"
SCENARIO_CROSS_DIF_ELEMENT_FIN[4][5] = "~+"
SCENARIO_CROSS_DIF_ELEMENT_FIN[4][7] = "~"
SCENARIO_CROSS_DIF_ELEMENT_FIN[5][4] = "+"
SCENARIO_CROSS_DIF_ELEMENT_FIN[5][6] = "~"

SCENARIO_SHOOT_WUMPUS_INIT = [["" for j in range(COL)] for i in range(ROW)]
SCENARIO_SHOOT_WUMPUS_INIT[4][4] = "W"

SCENARIO_SHOOT_WUMPUS_FINAL = deepcopy(SCENARIO_SHOOT_WUMPUS_INIT)
SCENARIO_SHOOT_WUMPUS_FINAL[4][4] = VISITED_CELL

SCENARIO_SHOOT_WUMPUS_SIGNAL_INIT = [["" for j in range(COL)]
                                     for i in range(ROW)]
SCENARIO_SHOOT_WUMPUS_SIGNAL_INIT[4][4] = "~+W"

SCENARIO_SHOOT_WUMPUS_SIGNAL_FIN = deepcopy(SCENARIO_SHOOT_WUMPUS_SIGNAL_INIT)
SCENARIO_SHOOT_WUMPUS_SIGNAL_FIN[4][4] = VISITED_CELL

SCENARIO_SHOOT_FAIL_INIT = [["" for j in range(COL)] for i in range(ROW)]
SCENARIO_SHOOT_FAIL_INIT[4][4] = ""


SCENARIO_FALL_IN_HOLES = [['' for j in range(COL)] for i in range(ROW)]
SCENARIO_FALL_IN_HOLES[5][5] = PLAYER
SCENARIO_FALL_IN_HOLES[5][4] = HOLES
SCENARIO_FALL_IN_HOLES[5][6] = HOLES
SCENARIO_FALL_IN_HOLES[4][5] = HOLES
SCENARIO_FALL_IN_HOLES[6][5] = HOLES

SCENARIO_EATEN_BY_WUMPUS = [['' for j in range(COL)] for i in range(ROW)]
SCENARIO_EATEN_BY_WUMPUS[5][5] = PLAYER
SCENARIO_EATEN_BY_WUMPUS[5][4] = WUMPUS
SCENARIO_EATEN_BY_WUMPUS[5][6] = WUMPUS
SCENARIO_EATEN_BY_WUMPUS[4][5] = WUMPUS
SCENARIO_EATEN_BY_WUMPUS[6][5] = WUMPUS


SCENARIO_MOVE_ACTION = [['' for j in range(COL)] for i in range(ROW)]

SCENARIO_MOVE_ACTION[5][5] = PLAYER
SCENARIO_MOVE_ACTION[5][4] = WUMPUS
SCENARIO_MOVE_ACTION[5][6] = HOLES
SCENARIO_MOVE_ACTION[4][5] = GOLD
SCENARIO_MOVE_ACTION[6][5] = ''
SCENARIO_MOVE_ACTION[7][5] = VISITED_CELL


SCENARIO_SIGNAL_HOLE = [['' for j in range(COL)] for i in range(ROW)]
SCENARIO_SIGNAL_HOLE[1][1] = HOLES

SCENARIO_SIGNAL_WUMPUS = [['' for j in range(COL)] for i in range(ROW)]
SCENARIO_SIGNAL_WUMPUS[2][1] = WUMPUS

SCENARIO_SIGNAL_WUMPUS_HOLE = [['' for j in range(COL)] for i in range(ROW)]
SCENARIO_SIGNAL_WUMPUS_HOLE[4][5] = HOLES
SCENARIO_SIGNAL_WUMPUS_HOLE[5][6] = WUMPUS

SCENARIO_SIGNAL_EMPTY = [['' for j in range(COL)] for i in range(ROW)]

SCENARIO_SIGNAL_HOLE_J = [['' for j in range(COL)] for i in range(ROW)]
SCENARIO_SIGNAL_HOLE_J[4][3] = HOLES

SCENARIO_SIGNAL_WUMPUS_J = [['' for j in range(COL)] for i in range(ROW)]
SCENARIO_SIGNAL_WUMPUS_J[4][3] = WUMPUS

SCENARIO_SIGNAL_WUMPUS_HOLE_J = [['' for j in range(COL)] for i in range(ROW)]
SCENARIO_SIGNAL_WUMPUS_HOLE_J[4][5] = HOLES
SCENARIO_SIGNAL_WUMPUS_HOLE_J[5][6] = WUMPUS

SCENARIO_SIGNAL_J_EMPTY = [['' for j in range(COL)] for i in range(ROW)]


SCENARIO_CELL_PARSE_1 = [['' for j in range(COL)] for i in range(ROW)]

SCENARIO_CELL_PARSE_1[5][5] = PLAYER
SCENARIO_CELL_PARSE_1[5][4] = WUMPUS
SCENARIO_CELL_PARSE_1[5][6] = HOLES
SCENARIO_CELL_PARSE_1[4][5] = GOLD
SCENARIO_CELL_PARSE_1[6][5] = ''
SCENARIO_CELL_PARSE_1[7][5] = VISITED_CELL

SCENARIO_CELL_PARSE_2 = [

    [' ', ' ', ' ', ' ', ' ', 'O', '', '', '', '', '', '', '', '', ''],
    ['', 'W', 'O', '', 'J', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
]

SCENARIO_CELL_PARSE_3 = [['' for j in range(COL)] for i in range(ROW)]
SCENARIO_CELL_PARSE_3[5][5] = PLAYER
SCENARIO_CELL_PARSE_3[5][4] = WUMPUS

SCENARIO_CELL_PARSE_4 = [['' for j in range(COL)] for i in range(ROW)]
SCENARIO_CELL_PARSE_4[5][5] = PLAYER
SCENARIO_CELL_PARSE_4[5][4] = HOLES

SCENARIO_CELL_PARSE_5 = [['' for j in range(COL)] for i in range(ROW)]
SCENARIO_CELL_PARSE_5[5][5] = PLAYER

SCENARIO_CELL_PARSE_1_USER_VIEW = \
    '#############################################\n'\
    '#############################################\n'\
    '#############################################\n'\
    '#############################################\n'\
    '#############################################\n'\
    '###############~J+###########################\n'\
    '#############################################\n'\
    '###############   ###########################\n'

SCENARIO_CELL_PARSE_2_USER_VIEW = \
    "     +~     ~  ##############################\n"\
    "############ J ##############################\n"\
    "#############################################\n"\
    "#############################################\n"\
    "#############################################\n"\
    "#############################################\n"\
    "#############################################\n"\
    "#############################################\n"

SCENARIO_CELL_PARSE_3_USER_VIEW = \
    "#############################################\n"\
    "#############################################\n"\
    "#############################################\n"\
    "#############################################\n"\
    "#############################################\n"\
    "############### J+###########################\n"\
    "#############################################\n"\
    "#############################################\n"

SCENARIO_CELL_PARSE_4_USER_VIEW = \
    "#############################################\n"\
    "#############################################\n"\
    "#############################################\n"\
    "#############################################\n"\
    "#############################################\n"\
    "###############~J ###########################\n"\
    "#############################################\n"\
    "#############################################\n"

SCENARIO_CELL_PARSE_5_USER_VIEW = \
    "#############################################\n"\
    "#############################################\n"\
    "#############################################\n"\
    "#############################################\n"\
    "#############################################\n"\
    "############### J ###########################\n"\
    "#############################################\n"\
    "#############################################\n"


SCENARIO_WITH_OUT_GOLD = [['' for j in range(COL)] for i in range(ROW)]
SCENARIO_WITH_OUT_GOLD[5][5] = PLAYER

SCENARIO_FIND_POSITION = [['' for j in range(COL)] for i in range(ROW)]

SCENARIO_FIND_POSITION_HOLES = [['' for j in range(COL)] for i in range(ROW)]
SCENARIO_FIND_POSITION_HOLES[4][5] = HOLES
SCENARIO_FIND_POSITION_HOLES[5][4] = HOLES
SCENARIO_FIND_POSITION_HOLES[5][6] = HOLES
SCENARIO_FIND_POSITION_HOLES[6][5] = HOLES


SCENARIO_FIND_POSITION_H_BORDER = [['' for j in range(COL)]
                                   for i in range(ROW)]
SCENARIO_FIND_POSITION_H_BORDER[1][5] = HOLES

SCENARIO_FIND_POS_H_BOR_LEFT = [['' for j in range(COL)] for i in range(ROW)]
SCENARIO_FIND_POS_H_BOR_LEFT[1][0] = HOLES
SCENARIO_FIND_POS_H_BOR_LEFT[3][0] = HOLES


SCENARIO_DELETE = [['' for j in range(COL)] for i in range(ROW)]
SCENARIO_DELETE[5][5] = PLAYER
SCENARIO_DELETE[5][4] = WUMPUS
SCENARIO_DELETE[5][6] = WUMPUS
SCENARIO_DELETE[4][4] = WUMPUS
SCENARIO_DELETE[6][5] = WUMPUS
SCENARIO_DELETE[7][3] = HOLES
SCENARIO_DELETE[7][4] = HOLES
SCENARIO_DELETE[7][5] = HOLES
SCENARIO_DELETE[7][6] = HOLES

MEMORY_TEST = {
    (0, 0): [],
    (1, 0): [(1, 1)],
    (4, 5): [(3, 5), (5, 5), (4, 5)],
    (3, 4): [(2, 4), (4, 4), (3, 5), (3, 3)],
    (6, 6): [],
}

INITIAL_SIMPLE_BOARD = [['' for j in range(COL)] for i in range(ROW)]
INITIAL_SIMPLE_BOARD[0][1] = GOLD

INITIAL_FAIL_BOARD = [['' for j in range(COL)] for i in range(ROW)]
INITIAL_FAIL_BOARD[4][3] = HOLES
INITIAL_FAIL_BOARD[4][5] = HOLES
INITIAL_FAIL_BOARD[3][4] = HOLES
INITIAL_FAIL_BOARD[5][4] = HOLES

INITIAL_BIG_FAIL_BOARD = [['' for j in range(COL)] for i in range(ROW)]
INITIAL_BIG_FAIL_BOARD[0][4] = HOLES
INITIAL_BIG_FAIL_BOARD[1][4] = HOLES
INITIAL_BIG_FAIL_BOARD[2][4] = HOLES
INITIAL_BIG_FAIL_BOARD[3][4] = HOLES
INITIAL_BIG_FAIL_BOARD[4][4] = HOLES
INITIAL_BIG_FAIL_BOARD[5][4] = HOLES
INITIAL_BIG_FAIL_BOARD[6][4] = HOLES
INITIAL_BIG_FAIL_BOARD[7][4] = HOLES


RECURSIVE = [['' for j in range(COL)] for i in range(ROW)]
RECURSIVE[0][1] = GOLD


RECURSIVE_SIDE = [['' for j in range(COL)] for i in range(ROW)]
RECURSIVE_SIDE[1][7] = HOLES
RECURSIVE_SIDE[2][6] = HOLES
RECURSIVE_SIDE[3][7] = HOLES

VALID_HOLE_SCENARIO = deepcopy(INITIAL_BIG_FAIL_BOARD)
VALID_HOLE_SCENARIO[7][4] = ""
VALID_HOLE_SCENARIO[4][10] = GOLD

RECURSIVE_SIDE_BORDER = [['' for j in range(COL)] for i in range(ROW)]
RECURSIVE_SIDE_BORDER[6][0] = HOLES
RECURSIVE_SIDE_BORDER[7][1] = HOLES
SCENARIO_PLAY_MOVE = [['' for j in range(COL)] for i in range(ROW)]
SCENARIO_PLAY_MOVE[5][5] = PLAYER

SCENARIO_PLAY_MOVE_FINAL = [['' for j in range(COL)] for i in range(ROW)]
SCENARIO_PLAY_MOVE_FINAL[4][5] = PLAYER
SCENARIO_PLAY_MOVE_FINAL[5][5] = VISITED_CELL

SCENARIO_PLAY_SHOOT = [['' for j in range(COL)] for i in range(ROW)]
SCENARIO_PLAY_SHOOT[5][5] = PLAYER

SCENARIO_PLAY_SHOOT_OK = [['' for j in range(COL)] for i in range(ROW)]
SCENARIO_PLAY_SHOOT_OK[5][5] = PLAYER
SCENARIO_PLAY_SHOOT_OK[4][5] = WUMPUS

SCENARIO_PLAY_SHOOT_OK_F = [['' for j in range(COL)] for i in range(ROW)]
SCENARIO_PLAY_SHOOT_OK_F[5][5] = PLAYER
SCENARIO_PLAY_SHOOT_OK_F[4][5] = VISITED_CELL

SCENARIO_PLAY_LAST_GOLD = [['' for j in range(COL)] for i in range(ROW)]
SCENARIO_PLAY_LAST_GOLD[5][5] = PLAYER
SCENARIO_PLAY_LAST_GOLD[4][5] = GOLD

SCENARIO_PLAY_LAST_GOLD_FIN = [['' for j in range(COL)] for i in range(ROW)]
SCENARIO_PLAY_LAST_GOLD_FIN[5][5] = VISITED_CELL
SCENARIO_PLAY_LAST_GOLD_FIN[4][5] = PLAYER

SCENARIO_PLAY_WIN_GOLD = [['' for j in range(COL)] for i in range(ROW)]
SCENARIO_PLAY_WIN_GOLD[5][5] = PLAYER
SCENARIO_PLAY_WIN_GOLD[4][5] = GOLD
SCENARIO_PLAY_WIN_GOLD[1][5] = GOLD

SCENARIO_PLAY_WIN_GOLD_F = [['' for j in range(COL)] for i in range(ROW)]
SCENARIO_PLAY_WIN_GOLD_F[5][5] = VISITED_CELL
SCENARIO_PLAY_WIN_GOLD_F[1][5] = GOLD
SCENARIO_PLAY_WIN_GOLD_F[4][5] = PLAYER
