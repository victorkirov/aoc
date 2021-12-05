from functools import reduce
from collections import defaultdict
from itertools import product, combinations, permutations

# strings
lines = [l.strip() for l in open('input') if l]
values = [v for v in lines]


# parts
def part1():
    depth = 0
    pos = 0

    for value in values:
        [instruction, amount] = value.split(' ')

        if instruction == 'forward':
            pos += int(amount)
        if instruction == 'up':
            depth -= int(amount)
            depth = max(0, depth)
        if instruction == 'down':
            depth += int(amount)

    return depth * pos


def part2():
    pos = 0
    depth = 0
    aim = 0

    for value in values:
        [instruction, amount] = value.split(' ')

        if instruction == 'forward':
            pos += abs(int(amount))
            depth += int(amount) * aim
        if instruction == 'up':
            aim -= int(amount)
        if instruction == 'down':
            aim += int(amount)

    return depth * pos


print('Part 1: ', part1())
print('Part 2: ', part2())
