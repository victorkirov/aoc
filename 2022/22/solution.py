from functools import reduce, cache
from collections import defaultdict
from itertools import product, combinations, permutations
import re

# input_file_name = 'input'
input_file_name = 'test'

# groups
data = open(input_file_name).read()
values = [v for v in data.split('\n\n')]
values = [v.split('\n') for v in values]

grid = values[0]
max_width = max(len(v) for v in grid)
grid = [g.ljust(max_width, ' ') for g in grid]

instructions = re.findall('[0-9]+|[RL]', values[1][0])


def turn_right(dir):
    dx = 0 if dir[0] != 0 else -1 * dir[1]
    dy = 0 if dir[1] != 0 else dir[0]
    return (dx, dy)


def turn_left(dir):
    dx = 0 if dir[0] != 0 else dir[1]
    dy = 0 if dir[1] != 0 else -1 * dir[0]
    return (dx, dy)


# parts
def part1():
    pos = (grid[0].index('.'), 0)
    dir = (1, 0)

    for i in instructions:
        if i == 'R':
            dir = turn_right(dir)
        elif i == 'L':
            dir = turn_left(dir)
        else:
            dist = int(i)

            for _ in range(dist):
                next_y = (pos[1] + dir[1]) % len(grid)
                next_x = (pos[0] + dir[0]) % len(grid[next_y])

                while grid[next_y][next_x] == ' ':
                    next_y = (next_y + dir[1]) % len(grid)
                    next_x = (next_x + dir[0]) % len(grid[next_y])

                if grid[next_y][next_x] == '#':
                    break
                elif grid[next_y][next_x] == '.':
                    pos = (next_x, next_y)

    dir_score = (
        0 if dir[0] == 1 else
        1 if dir[1] == 1 else
        2 if dir[0] == -1 else
        3
    )

    return (pos[1] + 1) * 1000 + (pos[0] + 1) * 4 + dir_score


def check_pos_populated(x, y):
    if not 0 <= x < max_width:
        return False

    if not 0 <= y < len(grid):
        return False

    try:
        return grid[y][x] in ('.', '#')
    except Exception:
        return False


def part2():
    pos = (grid[0].index('.'), 0)
    dir = (1, 0)

    cube_size = min(len(l.strip()) for l in grid)

    for i in instructions:
        if i == 'R':
            dir = turn_right(dir)
        elif i == 'L':
            dir = turn_left(dir)
        else:
            dist = int(i)

            for _ in range(dist):
                next_y = pos[1] + dir[1]
                next_x = pos[0] + dir[0]

                if (
                    next_y < 0
                    or next_y >= len(grid)
                    or next_x < 0
                    or next_x > max_width
                    or grid[next_y][next_x] == ' '
                ):
                    # calculate actual next pos and new dir

                if grid[next_y][next_x] == '#':
                    break
                elif grid[next_y][next_x] == '.':
                    pos = (next_x, next_y)

    dir_score = (
        0 if dir[0] == 1 else
        1 if dir[1] == 1 else
        2 if dir[0] == -1 else
        3
    )

    return (pos[1] + 1) * 1000 + (pos[0] + 1) * 4 + dir_score

print('Part 1: ', part1())
print('Part 2: ', part2())
