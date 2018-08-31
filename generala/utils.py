import random

from . import *


def throw_dice(num):
    results = []
    for number in range(0, num):
        results.append(random.randint(1, 6))
    return results


def check_throw(throw_array, points_to_check, throw_number):
    if points_to_check == GENERALA['name']:
        for index in range(0, len(throw_array) - 1):
            if throw_array[index] != throw_array[index + 1]:
                return 0
        if throw_number == 1:
            return SERVEDGENERALA['score']
        else:
            return GENERALA['score']
    elif points_to_check == POKER['name']:
        for index in range(0, len(throw_array)):
            if throw_array.count(index + 1) == 4:
                return POKER['score']
        return 0
    elif points_to_check == FULL['name']:
        if throw_array.count(1) == 3:
            if throw_array.count(2) == 2:
                if throw_number == 1:
                    return SERVEDFULL['score']
                else:
                    return FULL['score']
            elif throw_array.count(3) == 2:
                if throw_number == 1:
                    return SERVEDFULL['score']
                else:
                    return FULL['score']
            elif throw_array.count(4) == 2:
                if throw_number == 1:
                    return SERVEDFULL['score']
                else:
                    return FULL['score']
            elif throw_array.count(5) == 2:
                if throw_number == 1:
                    return SERVEDFULL['score']
                else:
                    return FULL['score']
            elif throw_array.count(6) == 2:
                if throw_number == 1:
                    return SERVEDFULL['score']
                else:
                    return FULL['score']
            else:
                return 0
        elif throw_array.count(2) == 3:
            if throw_array.count(1) == 2:
                if throw_number == 1:
                    return SERVEDFULL['score']
                else:
                    return FULL['score']
            elif throw_array.count(3) == 2:
                if throw_number == 1:
                    return SERVEDFULL['score']
                else:
                    return FULL['score']
            elif throw_array.count(4) == 2:
                if throw_number == 1:
                    return SERVEDFULL['score']
                else:
                    return FULL['score']
            elif throw_array.count(5) == 2:
                if throw_number == 1:
                    return SERVEDFULL['score']
                else:
                    return FULL['score']
            elif throw_array.count(6) == 2:
                if throw_number == 1:
                    return SERVEDFULL['score']
                else:
                    return FULL['score']
            else:
                return 0
        elif throw_array.count(3) == 3:
            if throw_array.count(1) == 2:
                if throw_number == 1:
                    return SERVEDFULL['score']
                else:
                    return FULL['score']
            elif throw_array.count(2) == 2:
                if throw_number == 1:
                    return SERVEDFULL['score']
                else:
                    return FULL['score']
            elif throw_array.count(4) == 2:
                if throw_number == 1:
                    return SERVEDFULL['score']
                else:
                    return FULL['score']
            elif throw_array.count(5) == 2:
                if throw_number == 1:
                    return SERVEDFULL['score']
                else:
                    return FULL['score']
            elif throw_array.count(6) == 2:
                if throw_number == 1:
                    return SERVEDFULL['score']
                else:
                    return FULL['score']
            else:
                return 0
        elif throw_array.count(4) == 3:
            if throw_array.count(1) == 2:
                if throw_number == 1:
                    return SERVEDFULL['score']
                else:
                    return FULL['score']
            elif throw_array.count(3) == 2:
                if throw_number == 1:
                    return SERVEDFULL['score']
                else:
                    return FULL['score']
            elif throw_array.count(2) == 2:
                if throw_number == 1:
                    return SERVEDFULL['score']
                else:
                    return FULL['score']
            elif throw_array.count(5) == 2:
                if throw_number == 1:
                    return SERVEDFULL['score']
                else:
                    return FULL['score']
            elif throw_array.count(6) == 2:
                if throw_number == 1:
                    return SERVEDFULL['score']
                else:
                    return FULL['score']
            else:
                return 0
        elif throw_array.count(5) == 3:
            if throw_array.count(1) == 2:
                if throw_number == 1:
                    return SERVEDFULL['score']
                else:
                    return FULL['score']
            elif throw_array.count(3) == 2:
                if throw_number == 1:
                    return SERVEDFULL['score']
                else:
                    return FULL['score']
            elif throw_array.count(4) == 2:
                if throw_number == 1:
                    return SERVEDFULL['score']
                else:
                    return FULL['score']
            elif throw_array.count(2) == 2:
                if throw_number == 1:
                    return SERVEDFULL['score']
                else:
                    return FULL['score']
            elif throw_array.count(6) == 2:
                if throw_number == 1:
                    return SERVEDFULL['score']
                else:
                    return FULL['score']
            else:
                return 0
        elif throw_array.count(6) == 3:
            if throw_array.count(1) == 2:
                if throw_number == 1:
                    return SERVEDFULL['score']
                else:
                    return FULL['score']
            elif throw_array.count(3) == 2:
                if throw_number == 1:
                    return SERVEDFULL['score']
                else:
                    return FULL['score']
            elif throw_array.count(4) == 2:
                if throw_number == 1:
                    return SERVEDFULL['score']
                else:
                    return FULL['score']
            elif throw_array.count(5) == 2:
                if throw_number == 1:
                    return SERVEDFULL['score']
                else:
                    return FULL['score']
            elif throw_array.count(2) == 2:
                if throw_number == 1:
                    return SERVEDFULL['score']
                else:
                    return FULL['score']
            else:
                return 0
        else:
            return 0

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
        sum = 0
        for index in range(0, len(throw_array)):
            if throw_array[index] == ONE['score']:
                sum += ONE['score']
        return sum
    elif points_to_check == TWO['name']:
        sum = 0
        for index in range(0, len(throw_array)):
            if throw_array[index] == TWO['score']:
                sum += TWO['score']
        return sum
    elif points_to_check == THREE['name']:
        sum = 0
        for index in range(0, len(throw_array)):
            if throw_array[index] == THREE['score']:
                sum += THREE['score']
        return sum
    elif points_to_check == FOUR['name']:
        sum = 0
        for index in range(0, len(throw_array)):
            if throw_array[index] == FOUR['score']:
                sum += FOUR['score']
        return sum
    elif points_to_check == FIVE['name']:
        sum = 0
        for index in range(0, len(throw_array)):
            if throw_array[index] == FIVE['score']:
                sum += FIVE['score']
        return sum
    elif points_to_check == SIX['name']:
        sum = 0
        for index in range(0, len(throw_array)):
            if throw_array[index] == SIX['score']:
                sum += SIX['score']
        return sum
