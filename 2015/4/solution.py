from functools import reduce
from collections import defaultdict
from itertools import product, combinations, permutations
import hashlib


# parts
def part1():
    val = 'bgvyzdsv'
    n = 1

    while not hashlib.md5(f'{val}{str(n)}'.encode('ascii')).hexdigest().startswith('00000'):
        n += 1
    return n

def part2():
    val = 'bgvyzdsv'
    n = 1

    while not hashlib.md5(f'{val}{str(n)}'.encode('ascii')).hexdigest().startswith('000000'):
        n += 1
    return n


print('Part 1: ', part1())
print('Part 2: ', part2())
