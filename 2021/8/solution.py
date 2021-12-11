from functools import reduce
from collections import defaultdict
from itertools import product, combinations, permutations
from typing import List, Set

# strings
lines = [l.strip() for l in open('input') if l]
values = [v for v in lines]


# parts
def part1():
    result = 0

    for value in values:
        [_, output] = value.split(' | ')
        output_digits = output.split(' ')

        for digit in output_digits:
             if len(digit) in [2, 3, 4, 7]:
                 result += 1

    return result


def part2():
    result = 0

    for value in values:
        [input, output] = value.split(' | ')
        input_signals = input.split(' ')
        output_digits = output.split(' ')

        mappings: List[Set] = [None] * 10

        unsolved = []

        for digit in input_signals:
            if len(digit) not in [2, 3, 4, 7]:
                unsolved.append(set(digit))
                continue

            if len(digit) == 2:
                 mappings[1] = set(digit)
            if len(digit) == 4:
                 mappings[4] = set(digit)
            if len(digit) == 3:
                 mappings[7] = set(digit)
            if len(digit) == 7:
                 mappings[8] = set(digit)

        input_signal_sets = unsolved

        # we have 1,4,7,8 so far

        unsolved = []
        for digit_set in input_signal_sets:
            if digit_set - mappings[7] == mappings[8] - mappings[7]:
                mappings[6] = digit_set
            elif digit_set | mappings[7] | mappings[4] == digit_set:
                mappings[9] = digit_set
            else:
                unsolved.append(digit_set)


        input_signal_sets = unsolved

        # now we have 1,4,6,7,8,9

        unsolved = []
        for digit_set in input_signal_sets:
            if (mappings[4] - mappings[1]).issubset(digit_set):
                mappings[5] = digit_set
            else:
                unsolved.append(digit_set)

        input_signal_sets = unsolved

        # now we have 1,4,5,6,7,8,9

        unsolved = []
        for digit_set in input_signal_sets:
            if not (mappings[6] - mappings[5]).issubset(digit_set):
                mappings[3] = digit_set
            else:
                unsolved.append(digit_set)

        input_signal_sets = unsolved

        # now we have 1,3,4,5,6,7,8,9

        unsolved = []
        for digit_set in input_signal_sets:
            if (mappings[3] - mappings[7]).issubset(digit_set):
                mappings[2] = digit_set
            else:
                mappings[0] = digit_set

        # now we have all

        displayed_digit = ''
        for digit in output_digits:
            displayed_digit += str(mappings.index(set(digit)))

        result += int(displayed_digit)


    return result


print('Part 1: ', part1())
print('Part 2: ', part2())
