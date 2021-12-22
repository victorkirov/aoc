from functools import reduce, cache
from collections import defaultdict
from itertools import product, combinations, permutations

# strings
lines = [l.strip() for l in open('input2') if l]
values = [v for v in lines]

commands = []
for value in values:
    [command, cell_def] = value.split(' ')
    [x_cmd, y_cmd, z_cmd] = cell_def.split(',')

    [x_start, x_end] = x_cmd.split('=')[1].split('..')
    [y_start, y_end] = y_cmd.split('=')[1].split('..')
    [z_start, z_end] = z_cmd.split('=')[1].split('..')

    commands.append((
        command,
        int(x_start),
        int(x_end),
        int(y_start),
        int(y_end),
        int(z_start),
        int(z_end)
    ))

# parts
def part1():
    on_set = set()

    for (
        command,
        x_start,
        x_end,
        y_start,
        y_end,
        z_start,
        z_end
    ) in commands:
        for x in range(max(x_start, -50), min(x_end + 1, 51)):
            for y in range(max(y_start, -50), min(y_end + 1, 51)):
                for z in range(max(z_start, -50), min(z_end + 1, 51)):
                    if command == 'on':
                        on_set.add((x, y, z))
                    elif (x, y, z) in on_set:
                        on_set.remove((x, y, z))

    return len(on_set)


def part2():
    # 2758514936282235
    pass


print('Part 1: ', part1())
print('Part 2: ', part2())
