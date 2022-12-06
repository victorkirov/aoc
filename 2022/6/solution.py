from functools import reduce, cache
from collections import defaultdict
from itertools import product, combinations, permutations

input_file_name = 'input'

values = [l.strip() for l in open(input_file_name) if l][0]


def part(group_size):
    group = []
    for i in range(len(values)):
        char = values[i]

        group.append(char)

        if(len(group) > group_size):
            group.pop(0)
        if len(set(group)) == group_size:
            return i + 1


print('Part 1: ', part(4))
print('Part 2: ', part(14))
