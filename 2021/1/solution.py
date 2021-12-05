from functools import reduce
from collections import defaultdict
from itertools import product, combinations, permutations

# ints
data = [l.strip() for l in open('input') if l]
values = [int(v) for v in data]


# parts
def part1():
    result = 0
    current = values[0]

    for value in values[1:]:
        if current < value:
            result += 1
        current = value

    return result


def part2():
    A = values[0:3]
    B = values[1:4]
    result = 1 if sum(A) < sum(B) else 0

    for value in values[4:]:
        A = list(B)
        B = B[1:]
        B.append(value)
        if sum(A) < sum(B):
            result += 1

    return result


print('Part 1: ', part1())
print('Part 2: ', part2())
