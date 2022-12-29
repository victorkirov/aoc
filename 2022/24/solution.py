from functools import cache
from math import lcm

input_file_name = 'input'

lines = [l.strip() for l in open(input_file_name) if l]

blizzards_start = []
for li, l in enumerate(lines):
    for ci, c in enumerate(l):
        if c in ('<', '>', '^', 'v'):
            blizzards_start.append([[ci, li], c])

start_pos = (lines[0].index('.'), 0)
end_pos = (lines[-1].index('.'), len(lines) - 1)

x_min = 1
x_max = len(lines[1]) - 2
y_min = 1
y_max = len(lines) - 2

dirs = [
    (1, 0),
    (0, 1),
    (0, -1),
    (-1, 0),
    (0, 0),
]


@cache
def get_blizzards_at_turn(turn):
    if turn == 0:
        return blizzards_start, { (b[0][0], b[0][1]) for b in blizzards_start}

    blizzards, _positions = get_blizzards_at_turn(turn - 1)

    new_blizzards = []
    new_positions = set()
    for [pos, c] in blizzards:
        if c == '^':
            new_y = pos[1] - 1 if pos[1] > y_min else y_max
            new_pos = [pos[0], new_y]
        elif c == 'v':
            new_y = pos[1] + 1 if pos[1] < y_max else y_min
            new_pos = [pos[0], new_y]
        elif c == '<':
            new_x = pos[0] - 1 if pos[0] > x_min else x_max
            new_pos = [new_x, pos[1]]
        elif c == '>':
            new_x = pos[0] + 1 if pos[0] < x_max else x_min
            new_pos = [new_x, pos[1]]
        else:
            raise Exception(c)
        new_blizzards.append([new_pos, c])
        new_positions.add((new_pos[0], new_pos[1]))

    return new_blizzards, new_positions


def calc_time(start, end, start_turn):
    visited = {
        (start_turn % lcm(y_max, x_max), start): start_turn
    }
    to_check = [(start_turn, start)]


    while len(to_check) > 0:
        to_check.sort(key=lambda x: x[0], reverse=True)

        turn, my_pos = to_check.pop()
        _new_blizzards, new_positions = get_blizzards_at_turn((turn + 1) % lcm(y_max, x_max))

        for move_dir in dirs:
            new_x = my_pos[0] + move_dir[0]
            new_y = my_pos[1] + move_dir[1]

            new_pos = (new_x, new_y)

            if new_pos == end:
                return turn + 1

            if new_pos != start and (new_x < x_min or new_x > x_max or new_y < y_min or new_y > y_max):
                continue

            if new_pos in new_positions:
                continue

            new_lookup = (turn + 1, new_pos)
            new_visited_lookup = ((turn + 1) % lcm(y_max, x_max), new_pos)

            if new_visited_lookup in visited and visited[new_visited_lookup] <= turn + 1:
                continue

            visited[new_visited_lookup] = turn + 1
            to_check.append(new_lookup)


@cache
def part1():
    return calc_time(start_pos, end_pos, 0)


def part2():
    result = part1()
    result = calc_time(end_pos, start_pos, result)
    return calc_time(start_pos, end_pos, result)


print('Part 1: ', part1())
print('Part 2: ', part2())
