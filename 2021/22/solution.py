from functools import reduce, cache
from collections import defaultdict
from itertools import product, combinations, permutations
from typing import List


# strings
lines = [l.strip() for l in open('input') if l]
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


def process_diff(
    region,
    x_start,
    x_end,
    y_start,
    y_end,
    z_start,
    z_end
) -> List:
    [
        (rx_start, ry_start, rz_start),
        (rx_end, ry_end, rz_end),
    ] = region

    x_vals = [x_start, x_start - 1, x_end, x_end + 1, rx_start, rx_end]
    y_vals = [y_start, y_start - 1, y_end, y_end + 1, ry_start, ry_end]
    z_vals = [z_start, z_start - 1, z_end, z_end + 1, rz_start, rz_end]

    x_vals.sort()
    y_vals.sort()
    z_vals.sort()

    if (
        x_vals[0] == rx_start and x_vals[1] == rx_end
        or x_vals[-2] == rx_start and x_vals[-1] == rx_end
        or y_vals[0] == ry_start and y_vals[1] == ry_end
        or y_vals[-2] == ry_start and y_vals[-1] == ry_end
        or z_vals[0] == rz_start and z_vals[1] == rz_end
        or z_vals[-2] == rz_start and z_vals[-1] == rz_end
    ):
        return [region]

    regions = []

    for xi in range(3):
        xl = x_vals[xi * 2]
        xr = x_vals[xi * 2 + 1]
        for yi in range(3):
            yl = y_vals[yi * 2]
            yr = y_vals[yi * 2 + 1]
            for zi in range(3):
                zl = z_vals[zi * 2]
                zr = z_vals[zi * 2 + 1]

                if (
                    rx_start <= xl <= rx_end
                    and ry_start <= yl <= ry_end
                    and rz_start <= zl <= rz_end
                    and rx_start <= xr <= rx_end
                    and ry_start <= yr <= ry_end
                    and rz_start <= zr <= rz_end
                    and not (
                        x_start <= xl <= x_end
                        and y_start <= yl <= y_end
                        and z_start <= zl <= z_end
                        and x_start <= xr <= x_end
                        and y_start <= yr <= y_end
                        and z_start <= zr <= z_end
                    )
                ):
                    regions.append(
                        [
                            (xl, yl, zl),
                            (xr, yr, zr),
                        ]
                    )

    return regions



def part2():
    regions = []
    runs = 0
    for (
        command,
        x_start,
        x_end,
        y_start,
        y_end,
        z_start,
        z_end
    ) in commands:
        runs += 1
        print(runs)
        new_regions = []
        for region in regions:
            new_regions += process_diff(
                region,
                x_start,
                x_end,
                y_start,
                y_end,
                z_start,
                z_end
            )
        if command == 'on':
            new_regions.append(
                [
                    (x_start, y_start, z_start),
                    (x_end, y_end, z_end),
                ]
            )
        regions = new_regions

    return sum([
        (end[0] - start[0] + 1) * (end[1] - start[1] + 1) * (end[2] - start[2] + 1)
        for [start, end]
        in regions
    ])


print('Part 1: ', part1())
print('Part 2: ', part2())
