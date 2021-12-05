from functools import reduce
from collections import defaultdict
from itertools import product, combinations, permutations

# strings
lines = [l.strip() for l in open('input') if l]
values = [v for v in lines]


# parts
def part1():
    l = list(range(len(values[0])))
    counts = [0 for _ in l]

    for value in values:
        for i in l:
            counts[i] += int(value[i])

    gamma = ['1' if x > len(values) / 2 else '0' for x in counts]
    eps = ['0' if x > len(values) / 2 else '1' for x in counts]

    return int(''.join(gamma), 2) * int(''.join(eps), 2)


def get_numbers_for_pos(numbers, pos, most_common=True):
    counts = 0

    for value in numbers:
        counts += int(value[pos])

    lookup_val = (
        '1'
        if (
            (most_common and counts >= len(numbers) / 2 )
            or
            (not most_common and counts < len(numbers) / 2)
        )
        else '0'
    )

    return [value for value in numbers if value[pos] == lookup_val]


def part2():
    o2 = values
    pos = 0

    while len(o2) > 1:
        o2 = get_numbers_for_pos(o2, pos)
        pos = (pos + 1) % len(values[0])

    co2 = values
    pos = 0

    while len(co2) > 1:
        co2 = get_numbers_for_pos(co2, pos, False)
        pos = (pos + 1) % len(values[0])

    return int(''.join(o2[0]), 2) * int(''.join(co2[0]), 2)

print('Part 1: ', part1())
print('Part 2: ', part2())
