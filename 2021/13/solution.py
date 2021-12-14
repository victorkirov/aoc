from functools import reduce
from collections import defaultdict
from itertools import product, combinations, permutations

# groups
data = open('input').read()
values = [v.strip() for v in data.split('\n\n')]
values = [v.split('\n') for v in values]

points_list = [
    (int(v.split(',')[0]),int(v.split(',')[1]))
    for v in values[0]
]
instructions = [
    (v.split(' ')[-1].split('=')[0],int(v.split(' ')[-1].split('=')[1]))
    for v in values[1]
]

# parts
def part1():
    points = set(points_list)

    (axis, distance) = instructions[0]

    if axis == 'y':
        new_points = {(x, y if y < distance else distance * 2 - y) for (x,y) in points}
    else:
        new_points = {(x if x < distance else distance * 2 - x, y) for (x,y) in points}

    points = new_points

    return len(points)


def part2():
    points = set(points_list)

    for (axis, distance) in instructions:
        if axis == 'y':
            new_points = {(x, y if y < distance else distance * 2 - y) for (x,y) in points}
        else:
            new_points = {(x if x < distance else distance * 2 - x, y) for (x,y) in points}

        points = new_points

    min_x = min([x for (x,_) in points])
    min_y = min([y for (_,y) in points])
    max_x = max([x for (x,_) in points])
    max_y = max([y for (_,y) in points])

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x,y) in points:
                print('#', end='')
            else:
                print('.', end='')
        print()

    return len(points)


print('Part 1: ', part1())
print('Part 2: ', part2())
