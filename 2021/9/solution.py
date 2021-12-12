from functools import reduce
from collections import defaultdict
from itertools import product, combinations, permutations

# strings
lines = [l.strip() for l in open('input') if l]
values = [[int(x) for x in list(v)] for v in lines]

test_positions = list(set(permutations([-1,0],2)) | set(permutations([1,0],2)))

# parts
def part1():
    minimums = []

    for y in range(0,len(values)):
        for x in range(0,len(values[0])):
            is_min = True
            val = values[y][x]

            for test_position in test_positions:
                (dx, dy) = test_position
                test_x = x + dx
                test_y = y + dy

                if (
                    test_x < 0 or test_x > len(values[0]) - 1
                    or test_y < 0 or test_y > len(values) - 1
                ):
                    continue

                if val >= values[test_y][test_x]:
                    is_min = False

            if is_min:
                minimums.append(val)

    return sum(minimums) + len(minimums)


def part2():
    ground_map = set()

    for y in range(0,len(values)):
        for x in range(0,len(values[0])):
            if values[y][x] != 9:
                ground_map.add((x,y))

    basin_sizes = []

    while len(ground_map) > 0:
        cells_to_process = [ground_map.pop()]
        basin_size = 1

        while len(cells_to_process) > 0:
            cell = cells_to_process.pop()
            for test_position in test_positions:
                (x, y) = cell
                (dx, dy) = test_position
                test_x = x + dx
                test_y = y + dy

                test_point = (test_x, test_y)
                if test_point in ground_map:
                    basin_size += 1

                    cells_to_process.append(test_point)
                    ground_map -= {test_point}

        basin_sizes.append(basin_size)

    basin_sizes.sort()

    return basin_sizes[-3] * basin_sizes[-2] * basin_sizes[-1]

print('Part 1: ', part1())
print('Part 2: ', part2())
