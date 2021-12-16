from functools import reduce
from collections import defaultdict
from itertools import product, combinations, permutations

# strings
lines = [l.strip() for l in open('input') if l]
values = [v for v in lines]

vowels = set(list('aeiou'))
naughty = {'ab', 'cd', 'pq', 'xy'}


def is_nice(val: str) -> bool:
    for naughty_str in naughty:
        if naughty_str in val:
            return False

    vowel_count = 0
    for l in list(val):
        if l in vowels:
            vowel_count += 1
        if vowel_count == 3:
            break

    if vowel_count < 3:
        return False

    for i in range(len(val) - 1):
        if val[i] == val[i+1]:
            return True
    return False

# parts
def part1():
    return sum([1 if is_nice(v) else 0 for v in values])


def is_nice2(val: str) -> bool:
    is_nice = False
    for i in range(len(val) - 2):
        if val[i] == val[i+2]:
            is_nice =  True
            break

    if not is_nice:
        return False

    doubles = []
    for i in range(len(val) - 1):
        double = f'{val[i]}{val[i+1]}'

        if double in doubles and (
            double != doubles[-1]
            or sum([1 if d == double else 0 for d in doubles]) > 1
        ):
            return True
        doubles.append(double)

    return False

def part2():
    return sum([1 if is_nice2(v) else 0 for v in values])

print('Part 1: ', part1())
print('Part 2: ', part2())
