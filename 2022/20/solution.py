from functools import reduce, cache
from collections import defaultdict
from itertools import product, combinations, permutations

input_file_name = 'input'
# input_file_name = 'test'

# strings
lines = [l.strip() for l in open(input_file_name) if l]
values = [(int(v), i) for i, v in enumerate(lines)]


def part1():
    mixed = [*values]

    for value in values:
        original_i = mixed.index(value)

        mixed.pop(original_i)

        new_i = (original_i + value[0]) % len(mixed)

        mixed.insert(new_i, value)

    while mixed[0][0] != 0:
        v = mixed.pop(0)
        mixed.append(v)

    return mixed[1000 % len(mixed)][0] + mixed[2000 % len(mixed)][0] + mixed[3000 % len(mixed)][0]


def part2():
    decrypted_values = [(v[0] * 811589153, v[1])  for v in values]
    mixed = [*decrypted_values]

    for _ in range(10):
        for value in decrypted_values:
            original_i = mixed.index(value)

            mixed.pop(original_i)

            new_i = (original_i + value[0]) % len(mixed)

            mixed.insert(new_i, value)

    while mixed[0][0] != 0:
        v = mixed.pop(0)
        mixed.append(v)

    return mixed[1000 % len(mixed)][0] + mixed[2000 % len(mixed)][0] + mixed[3000 % len(mixed)][0]


print('Part 1: ', part1())
print('Part 2: ', part2())
