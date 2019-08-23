
BOARD = [
   [0, 1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34],
   [0, 2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35],
   [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36],
]


def get_dozen_from_number(number):
    dozen = 0
    ranges = [list(range(1, 13)), list(range(13, 25)), list(range(25, 37))]
    for rng in ranges:
        if number in rng:
            dozen = ranges.index(rng) + 1
    return dozen


def get_color_from_number(number):
    if number == 0:
        return 'green'
    if 0 < number < 37:
        range_1 = (0 < number <= 10 and number % 2 == 1)
        range_2 = (11 <= number <= 18 and number % 2 == 0)
        range_3 = (19 <= number <= 28 and number % 2 == 1)
        range_4 = (29 <= number <= 36 and number % 2 == 0)
        return 'red' if range_1 or range_2 or range_3 or range_4 \
            else 'black'


def show_board():
    line_separator = "+" + "--+"*13 + "\n"
    board = line_separator
    for row in BOARD[::-1]:
        # converts to string and adds leading zeros
        row = [str(number).zfill(2) for number in row]
        board += "|" + "|".join(row) + "|\n"
        board += line_separator
    return board
