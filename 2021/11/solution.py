from functools import reduce
from collections import defaultdict
from itertools import product, combinations, permutations

# strings
lines = [l.strip() for l in open('input') if l]
values = [[int(x) for x in list(v)] for v in lines]

neighbour_positions = list(set(permutations([-1, -1,0, 1, 1],2)))


# parts
def part1():
    runs = 100
    octopus_map = {
        (x,y): values[y][x]
        for y in range(0,len(values))
        for x in range(0,len(values[0]))
    }
    flashes = 0

    while runs > 0:
        runs -= 1

        for pos in octopus_map.keys():
            octopus_map[pos] += 1

        flashing_octopus_positions = [
            octopus_pos
            for (octopus_pos, value) in octopus_map.items()
            if value == 10
        ]

        while len(flashing_octopus_positions) > 0:
            flashes += 1
            (x, y) = flashing_octopus_positions.pop()

            for (dx, dy) in neighbour_positions:
                neighbour_pos = (x+dx, y+dy)

                if not neighbour_pos in octopus_map:
                    continue

                octopus_map[neighbour_pos] += 1

                if octopus_map[neighbour_pos] == 10:
                    flashing_octopus_positions.append(neighbour_pos)

        for (pos, value) in octopus_map.items():
            if value > 9:
                octopus_map[pos] = 0

    for y in range(0,len(values)):
        for x in range(0,len(values[0])):
            print(octopus_map[(x,y)], end='')
        print()

    return flashes


def part2():
    runs = 0
    octopus_map = {
        (x,y): values[y][x]
        for y in range(0,len(values))
        for x in range(0,len(values[0]))
    }
    octopus_count = len(octopus_map)

    while 1:
        flashes = 0
        runs += 1

        for pos in octopus_map.keys():
            octopus_map[pos] += 1

        flashing_octopus_positions = [
            octopus_pos
            for (octopus_pos, value) in octopus_map.items()
            if value == 10
        ]

        while len(flashing_octopus_positions) > 0:
            flashes += 1
            (x, y) = flashing_octopus_positions.pop()

            for (dx, dy) in neighbour_positions:
                neighbour_pos = (x+dx, y+dy)

                if not neighbour_pos in octopus_map:
                    continue

                octopus_map[neighbour_pos] += 1

                if octopus_map[neighbour_pos] == 10:
                    flashing_octopus_positions.append(neighbour_pos)

        for (pos, value) in octopus_map.items():
            if value > 9:
                octopus_map[pos] = 0

        if flashes == octopus_count:
            break

    for y in range(0,len(values)):
        for x in range(0,len(values[0])):
            print(octopus_map[(x,y)], end='')
        print()

    return runs


print('Part 1: ', part1())
print('Part 2: ', part2())
