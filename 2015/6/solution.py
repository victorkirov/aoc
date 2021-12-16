from functools import reduce
from collections import defaultdict
from itertools import product, combinations, permutations

# strings
lines = [l.strip() for l in open('input') if l]
values = [v.removeprefix('turn ').split() for v in lines]


# parts
def part1():
    row_template = [-1] * 1000
    grid = [list(row_template) for _ in range(1000)]

    for value in values:
        [instruction, start, _, end] = value
        [sx, sy] = start.split(',')
        sx = int(sx)
        sy = int(sy)

        [ex, ey] = end.split(',')
        ex = int(ex)
        ey = int(ey)

        for x in range(sx, ex + 1):
            for y in range(sy, ey + 1):
                if instruction == 'toggle':
                    grid[x][y] *= -1
                if instruction == 'on':
                    grid[x][y] = 1
                if instruction == 'off':
                    grid[x][y] = -1

    return sum([sum([1 if cell == 1 else 0 for cell in row]) for row in grid])


def part2():
    row_template = [0] * 1000
    grid = [list(row_template) for _ in range(1000)]

    for value in values:
        [instruction, start, _, end] = value
        [sx, sy] = start.split(',')
        sx = int(sx)
        sy = int(sy)

        [ex, ey] = end.split(',')
        ex = int(ex)
        ey = int(ey)

        for x in range(sx, ex + 1):
            for y in range(sy, ey + 1):
                if instruction == 'toggle':
                    grid[x][y] += 2
                if instruction == 'on':
                    grid[x][y] += 1
                if instruction == 'off':
                    grid[x][y] -= (1 if grid[x][y] > 0 else 0)

    return sum([sum(row) for row in grid])


print('Part 1: ', part1())
print('Part 2: ', part2())
