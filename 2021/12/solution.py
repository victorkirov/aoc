import re
from functools import reduce
from collections import defaultdict
from itertools import product, combinations, permutations

from typing import Set

# strings
lines = [l.strip() for l in open('input') if l]
values = [v for v in lines]

travel_map = defaultdict(list)

for value in values:
    [pointA, pointB] = value.split('-')
    travel_map[pointA].append(pointB)
    travel_map[pointB].append(pointA)


def paths_from_node(node, visited: Set, small_cave_twice=False) -> int:
    destinations = travel_map[node]
    local_visited = visited | { node }
    paths = 0

    for destination in destinations:
        if destination == 'start':
            continue
        if destination == 'end':
            paths += 1
            continue
        if re.search('[a-z]', destination) and destination in local_visited:
            if small_cave_twice:
                paths += paths_from_node(destination, local_visited)
            continue
        paths += paths_from_node(destination, local_visited, small_cave_twice)

    return paths


# parts
def part1():
    return paths_from_node('start', set())


def part2():
    return paths_from_node('start', set(), True)


print('Part 1: ', part1())
print('Part 2: ', part2())
