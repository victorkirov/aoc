from functools import reduce
from collections import defaultdict
from itertools import product, combinations, permutations

# strings
lines = [l.strip() for l in open('input') if l]
values = [v for v in lines]

values = list(map(int, list(values[0])))


def play_round(cups, min_val, max_val):
    picked_up = cups[1:4]
    remaining = [cups[0]] + cups[4:]

    current = remaining[0]
    next_cup = current - 1

    while next_cup not in remaining:
        next_cup -= 1
        if next_cup < min_val:
            next_cup = max_val

    destination_index = remaining.index(next_cup)
    result =  remaining[0:destination_index + 1] + picked_up + remaining[destination_index + 1:]
    return result[1:] + [result[0]]


# parts
def part1():
    min_val = min(values)
    max_val = max(values)
    result = values

    for _ in range(100):
        result = play_round(result, min_val, max_val)

    return (wrapped:=(result + result))[(f_i:=wrapped.index(1)) + 1: wrapped.index(1,f_i + 1)]


def part2():
    max_val = 1000000
    all_values = values + list(range(max(values) + 1, max_val + 1))

    result = {}
    for i, val in enumerate(all_values):
        result[all_values[i - 1]] = val

    current = values[0]

    for _ in range(10000000):

        picked_val_1 = result[current]
        picked_val_2 = result[picked_val_1]
        picked_val_3 = result[picked_val_2]

        result[current] = result[picked_val_3]

        placement_val = current - 1
        while placement_val < 1 or placement_val in [picked_val_1, picked_val_2, picked_val_3]:
            placement_val -= 1

            if placement_val < 1:
                placement_val = max_val

        result[picked_val_3] = result[placement_val]
        result[placement_val] = picked_val_1

        current = result[current]

    return result[1] * result[result[1]]


print('Part 1: ', ''.join(map(str, part1())))
print('Part 2: ', part2())
