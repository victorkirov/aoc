from functools import reduce
from collections import defaultdict
from itertools import product, combinations, permutations

data = open('input').read()
values = data.strip().split(',')

counts = [0] * 9

for value in values:
    counts[int(value)] += 1

# parts
def simulate(days):
    result = list(counts)

    for _ in range(0, days):
        new_fish_count = result.pop(0)

        result[6] += new_fish_count
        result.append(new_fish_count)

    return sum(result)


print('Part 1: ', simulate(80))
print('Part 2: ', simulate(256))
