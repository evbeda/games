import random

from . import (
    FIVE, FOUR, FULL, GENERALA,
    ONE, POKER, SERVEDFULL, SERVEDGENERALA, SERVEDSTAIR,
    SIX, STAIR, THREE, TWO,
    )


def throw_dice(num):
    results = []
    for _ in range(0, num):
        results.append(random.randint(1, 6))
    return results


def check_throw(throw_array, points_to_check, throw_number):

    score = int()

    if points_to_check == GENERALA['name']:
        for index in range(0, len(throw_array) - 1):
            if throw_array[index] != throw_array[index + 1]:
                score = 0
                break
        else:
            if throw_number == 1:
                score = SERVEDGENERALA['score']
            else:
                score = GENERALA['score']
    elif points_to_check == POKER['name']:
        for index in range(0, len(throw_array)):
            if throw_array.count(index + 1) == 4:
                score = POKER['score']
                break
        else:
            score = 0

    elif points_to_check == FULL['name']:
        score = check_throw_full_score(throw_array, throw_number)

    elif points_to_check == STAIR['name']:
        orderedList = sorted(throw_array)
        if orderedList in ([1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [1, 3, 4, 5, 6],):
            if throw_number == 1:
                return SERVEDSTAIR['score']
            else:
                return STAIR['score']
        else:
            return 0

    elif points_to_check == ONE['name']:
        score = score = score_sum_point(throw_array, ONE)

    elif points_to_check == TWO['name']:
        score = score_sum_point(throw_array, TWO)

    elif points_to_check == THREE['name']:
        score = score_sum_point(throw_array, THREE)

    elif points_to_check == FOUR['name']:
        score = score_sum_point(throw_array, FOUR)

    elif points_to_check == FIVE['name']:
        score = score_sum_point(throw_array, FIVE)

    elif points_to_check == SIX['name']:
        score = score_sum_point(throw_array, SIX)

    return score


def check_throw_full_score(throw_array, throw_number):
    score = int()
    for number in range(7):
        for quantity in range(7):
            if quantity != number and throw_array.count(quantity) == 2:
                score = full_score(throw_number)
    return score


def full_score(throw_number) -> int:
    return SERVEDFULL['score'] if throw_number == 1\
                    else FULL['score']


def score_sum_point(throw_array, kind):
    return sum([kind['score'] for el in throw_array if el == kind['score']])
