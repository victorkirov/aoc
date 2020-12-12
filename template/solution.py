from functools import reduce
from collections import defaultdict
from itertools import product, combinations, permutations

# strings
lines = [l.strip() for l in open('input') if l]
values = [v for v in lines]

# ints
data = [l.strip() for l in open('input') if l]
values = [int(v) for v in data]

# groups
data = open('input').read()
values = [v.strip() for v in data.split('\n\n')]
values = [v.split('\n') for v in values]

# map
value_map = defaultdict(list)

def is_map(parent, potential_child):
    pass

for value in values:
    for inner in values:
        if value == inner:
            continue
        if is_map(value, inner):
            value_map[value].append(inner)


# parts
def part1():
    result = None

    for value in values:
        print(value)

    return result


def part2():
    pass


print('Part 1: ', part1())
print('Part 2: ', part2())
