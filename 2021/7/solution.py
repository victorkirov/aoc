from functools import reduce
from collections import defaultdict
from itertools import product, combinations, permutations


data = open('input').read()
values = [int(x) for x in data.strip().split(',')]

min_pos = min(values)
max_pos = max(values)

pos_counts = [0] * (max_pos+1)

for value in values:
    pos_counts[value] += 1


# parts
def part1():
    fuel_min_pos = 0
    for pos in range(min_pos + 1, max_pos + 1):
        distance = pos - min_pos
        crabs_at_pos = pos_counts[pos]
        fuel_min_pos += distance * crabs_at_pos

    current_fuel = fuel_min_pos
    min_fuel = fuel_min_pos

    for pos in range(min_pos + 1, max_pos + 1):
        current_fuel += sum(pos_counts[:pos])
        current_fuel -= sum(pos_counts[pos:])

        if current_fuel < min_fuel:
            min_fuel = current_fuel

    return min_fuel


def get_fuel_for_pos(target_pos):
    fuel = 0

    crabs = 0
    for pos in range(min_pos, target_pos):
        crabs += pos_counts[pos]
        fuel += crabs * (target_pos - pos)

    crabs = 0
    for pos in range(max_pos, target_pos, -1):
        crabs += pos_counts[pos]
        fuel += crabs * (pos - target_pos)
    return fuel


def part2():
    min_fuel = None
    for pos in range(min_pos, max_pos + 1):
        fuel = get_fuel_for_pos(pos)

        if not min_fuel or min_fuel > fuel:
            min_fuel = fuel
    return min_fuel


print('Part 1: ', part1())
print('Part 2: ', part2())
