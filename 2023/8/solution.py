from itertools import cycle
from math import lcm
from typing import List, Dict, Tuple

input_file_name = 'input'

# groups
data = open(input_file_name).read()
values = [v.strip() for v in data.split('\n\n')]
values = [v.split('\n') for v in values]

instructions = list(values[0][0])

dirs: Dict[str, Tuple[str, str]] = {}


for v in values[1]:
    [k, lr] = v.replace(' ', '').split('=')
    [l, r] = lr[1:-1].split(',')
    dirs[k] = (l, r)

# parts
def part1():
    result = 0

    curr ='AAA'
    for value in cycle(instructions):
        result += 1

        if value == 'R':
            curr = dirs[curr][1]
        else:
            curr = dirs[curr][0]

        if curr == 'ZZZ':
            break

    return result


def part2():
    starts: List[str] = [k for k in dirs.keys() if k[2] == 'A']
    cycles = []

    for start in starts:
        visited = [start]

        for value in cycle(instructions):
            if value == 'R':
                next_val = dirs[visited[-1]][1]
            else:
                next_val = dirs[visited[-1]][0]

            if next_val[2] == 'Z':
                if next_val in visited:
                    cycles.append(len(visited) - visited.index(next_val))
                    break

            visited.append(next_val)

    return lcm(*cycles)


print('Part 1: ', part1())
print('Part 2: ', part2())
