from functools import reduce
from collections import defaultdict
from itertools import product, combinations, permutations

# groups
data = open('input').read().replace('.', '0').replace('#', '1')
values = [v.strip() for v in data.split('\n\n')]
values = [v.split('\n') for v in values]

alg = list(values[0][0])
input_map = [list(row) for row in values[1]]

neighbour_offsets = [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]


def print_map(cell_map):
    for row in cell_map:
        print(''.join(row))
    print()


# parts
def solve(runs):
    current_map = list(input_map)
    # print_map(current_map)

    fill_char = '0'

    for run in range(runs):
        next_map = list()

        for row in range(-2, len(current_map) + 2):
            next_row = []
            for column in range(-2, len(current_map[0]) + 2):
                ref = ''
                for (dx, dy) in neighbour_offsets:
                    y = row + dy
                    x = column + dx

                    if y < 0 or x < 0 or y >= len(current_map) or x >= len(current_map[0]):
                        ref += fill_char
                    else:
                        ref += current_map[y][x]

                ref_index = int(ref, 2)
                next_row.append(alg[ref_index])

            next_map.append(next_row)

        current_map = next_map
        fill_char = alg[0 if fill_char == '0' else -1]

        # print_map(current_map)

    return sum([sum([int(cell) for cell in row]) for row in current_map])


print('Part 1: ', solve(2))
print('Part 2: ', solve(50))
