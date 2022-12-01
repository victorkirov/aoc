from functools import reduce, cache
from collections import defaultdict
from itertools import product, combinations, permutations

# groups
data = open('input').read()
values = [v.strip() for v in data.split('\n\n')]
values = [v.split('\n') for v in values]


# parts
def part1():
    result = 0

    for value in values:
        current = sum([int(x) for x in value])
        result = max(result, current)

    return result


def part2():
    calorie_list = [
        sum([int(x) for x in value])
        for value in values
    ]
    calorie_list.sort(reverse=True)
    return sum(calorie_list[:3])


print('Part 1: ', part1())
print('Part 2: ', part2())
