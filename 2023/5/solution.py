from functools import reduce, cache
from collections import defaultdict
from itertools import product, combinations, permutations
from typing import List

input_file_name = 'input'

# groups
data = open(input_file_name).read()
values = [v.strip() for v in data.split('\n\n')]
value_maps = [v.split('\n') for v in values]
seeds = [int(s) for s in value_maps[0][0].split(' ')[1:]]
other_maps = [
    [
        [int(j) for j in i.split(' ')]
        for i in v[1:]
    ]
    for v in value_maps[1:]
]


def item_through_map(item: int, m: List[List[int]]):
    for rng in m:
        if item >= rng[1] and item < rng[1] + rng[2]:
            return [item - rng[1] + rng[0], rng[2] - (item - rng[1])]

    return [item, None]


# parts
def part1():
    result = None
    for seed in seeds:
        seed_val = seed
        for m in other_maps:
            [seed_val, _] = item_through_map(seed_val, m)
        if result is None or seed_val < result:
            result = seed_val

    return result


def part2():
    result = None

    for i in range(0, len(seeds), 2):
        seed_val_curr = seeds[i]

        while seed_val_curr < seeds[i] + seeds[i + 1]:
            seed_val = seed_val_curr
            min_itt = seeds[i + 1]
            for m in other_maps:
                [seed_val, current_itt] = item_through_map(seed_val, m)

                if current_itt is not None:
                    min_itt = min(min_itt, current_itt)

            if result is None or seed_val < result:
                result = seed_val

            seed_val_curr += min_itt

    return result


print('Part 1: ', part1())
print('Part 2: ', part2())
