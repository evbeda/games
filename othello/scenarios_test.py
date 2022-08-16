
black_12 = [
    '        ',
    ' B B  B ',
    ' B      ',
    'BB WB   ',
    '   BW   ',
    '        ',
    '  BB B B',
    '        ',
]

white_12 = [
    'W     W ',
    '     W  ',
    ' W    W ',
    '   WB   ',
    'W  BW W ',
    '        ',
    '     B  ',
    'WW  W   ',
]
mix_6 = [
    '   B   W',
    ' W      ',
    '       B',
    '   WB   ',
    '   BW   ',
    'W       ',
    '     B  ',
    ' B     W',
]

mix_10 = [
    '   B  BW',
    ' W      ',
    '  B    B',
    '   WB   ',
    '   BW   ',
    'W W W   ',
    '     B  ',
    ' B     W',
]

flip_black = [
    'B  B  BW',
    ' W      ',
    '  B    B',
    '   WB   ',
    '   BW   ',
    'W W W   ',
    '     B  ',
    ' B     W',
]

final_flip_black = [
    'W  B  BW',
    ' W      ',
    '  B    B',
    '   WB   ',
    '   BW   ',
    'W W W   ',
    '     B  ',
    ' B     W',
]

flip_row_white = [
    'W  B  BW',
    ' W      ',
    '  B    B',
    '   WB   ',
    '   BW   ',
    'B B B   ',
    '     B  ',
    ' B     W',
]

final_flip_row_white = [
    'W  B  BW',
    ' W      ',
    '  B    B',
    '   WB   ',
    '   BW   ',
    'B B B   ',
    '     B  ',
    ' B     W',
]

diagonal_flip = [
    'B       ',
    ' B B  B ',
    ' BB     ',
    'BB WB   ',
    '   BW   ',
    '        ',
    '  BB B B',
    '        ',
]

final_diagonal_flip = [
    'W       ',
    ' W B  B ',
    ' BW     ',
    'BB WB   ',
    '   BW   ',
    '        ',
    '  BB B B',
    '        ',
]

validate_direction_1 = [
    [None, None, None, None, None, None, "B", "W"],
    [None, "W", None, None, None, None, None, None],
    [None, None, "B", None, None, None, None, 'B'],
    [None, None, None, "W", "B", None, None, None],
    [None, None, None, "B", "W", None, None, "W"],
    ["W", None, 'W', None, 'W', None, "B", None],
    [None, None, None, None, None, 'B', None, None],
    [None, 'B', None, None, None, None, None, "W"]]

validate_direction_2 = [
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, "W", None],
    ["W", None, None, None, None, None, "W", None],
    [None, "B", None, None, None, None, "W", None],
    ["W", "B", "B", None, None, None, "W", None],
    [None, None, None, "B", None, None, "W", None],
    [None, None, None, None, None, None, "W", None],
    [None, None, None, None, None, None, "B", None]]

board_winner_w = [
    'W       ',
    ' W    B ',
    '  W     ',
    'B  WB   ',
    '    W   ',
    '        ',
    '       B',
    '        ',
]

board_tie = [
    'W       ',
    ' W    B ',
    '  W     ',
    'B  WB   ',
    '    W   ',
    '        ',
    '  B    B',
    '        ',
]

board_tie_empty = [
    '        ',
    '        ',
    '        ',
    '        ',
    '        ',
    '        ',
    '        ',
    '        ',
]

all_poss_moves_board_1 = [
    '        ',
    '        ',
    '  WB WB ',
    '  BBBWWW',
    '   BBW  ',
    'BBBBBWB ',
    '     WW ',
    '        ',
]

all_poss_moves_board_2 = [
    'BBBBBBBW',
    'BWWBBBBB',
    'BWWWBBWB',
    'BWWWBBWB',
    'WWBBWBWB',
    'WWBWWBWB',
    'WWWBBBBB',
    'WWWWWWWB',
]


all_poss_moves_exp_1 = {
    (1, 1, ): [(2, 2)],
    (1, 2, ): [(2, 2)],
    (1, 6, ): [(2, 5)],
    (2, 1, ): [(2, 2)],
    (2, 4, ): [(2, 5)],
    (2, 7, ): [(3, 6), (4, 5)],
    (4, 6, ): [(4, 5), (3, 6)],
    (7, 4, ): [(6, 5)],
    (7, 6, ): [(6, 5), (6, 6)],
    (7, 7, ): [(6, 6), (5, 5)]
}
none_pos_exp_1 = [
    (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
    (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7),
    (2, 0), (2, 1), (2, 4), (2, 7),
    (3, 0), (3, 1),
    (4, 0), (4, 1), (4, 2), (4, 6), (4, 7),
    (5, 7),
    (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 7),
    (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7),
]

black_12_that_will_print = [
    ' 0 1 2 3 4 5 6 7   ',
    '| | | | | | | | | 0',
    '| |B| |B| | |B| | 1',
    '| |B| | | | | | | 2',
    '|B|B| |W|B| | | | 3',
    '| | | |B|W| | | | 4',
    '| | | | | | | | | 5',
    '| | |B|B| |B| |B| 6',
    '| | | | | | | | | 7',

]

white_12_that_will_print = [
    ' 0 1 2 3 4 5 6 7   ',
    '|W| | | | | |W| | 0',
    '| | | | | |W| | | 1',
    '| |W| | | | |W| | 2',
    '| | | |W|B| | | | 3',
    '|W| | |B|W| |W| | 4',
    '| | | | | | | | | 5',
    '| | | | | |B| | | 6',
    '|W|W| | |W| | | | 7',

]
play_board_1 = [
    '        ',
    '        ',
    '        ',
    '   WB   ',
    '   BW   ',
    '        ',
    '        ',
    '        ',
]

play_board_tie = [
    'BBBBBBBB',
    'BWWBWBBB',
    'BWWWBBWB',
    'BWWWBBWB',
    'WWBBWBWB',
    'BWBWWBWB',
    'BWWBBWWB',
    ' WWWWWWB',
]


play_board_b_wins = [
    'BBBBBBB ',
    'BWWBBBBW',
    'BWWWBBWW',
    'BWWWBBWW',
    'WWBBWBWW',
    'WWBWWBWW',
    'WWWBBWWW',
    'WWWWWWWB',
]

play_board_w_wins = [
    'BBBBBBBW',
    'BWWBBBBB',
    'BWWWBBWB',
    'BWWWBBWB',
    'WWBBWBWB',
    'WWBWWBWB',
    'WWWBBBBB',
    'WWWWWWW ',
]

put_piece_board = [
    'B       ',
    '        ',
    '        ',
    '   WB   ',
    '   BW   ',
    '        ',
    '        ',
    '        ',
]
