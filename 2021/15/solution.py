from functools import reduce
from collections import defaultdict
from itertools import product, combinations, permutations

# ints
data = [l.strip() for l in open('input') if l]
values = [[int(x) for x in list(v)] for v in data]

neighbour_offsets = list(set(permutations([-1, 0], 2)) | set(permutations([1, 0], 2)))


# parts
def find_path_cost(maze):
    start = (0, 0)

    max_x = max([x for (x, _) in maze])
    max_y = max([y for (_, y) in maze])
    end = (max_x, max_y)

    node_cost = {
        start: (0, [start])
    }

    to_visit = [start]

    while end not in node_cost:
        to_visit.sort(key=lambda p: node_cost[p][0] + maze[p], reverse=True)
        current = to_visit.pop()
        (c_cost, c_path) = node_cost[current]
        (cx, cy) = current

        for (dx, dy) in neighbour_offsets:
            nx = cx + dx
            ny = cy + dy

            if nx < 0 or nx > max_x or ny < 0 or ny > max_y:
                continue

            neighbour = (nx, ny)
            n_cost = maze[neighbour]

            if neighbour not in node_cost or node_cost[neighbour][0] > c_cost + n_cost:
                node_cost[neighbour] = (c_cost + n_cost, c_path + [neighbour])
                to_visit.append(neighbour)

    return node_cost[end][0]


def part1():
    maze = {}
    for y in range(len(values)):
        for x in range(len(values[0])):
            maze[(x,y)] = values[x][y]

    return find_path_cost(maze)

def part2():
    maze = {}
    width = len(values[0])
    height = len(values)
    for y in range(height):
        for x in range(width):
            base_value = values[x][y]

            for dx in range(5):
                for dy in range(5):
                    value = base_value + dx + dy
                    if value > 9:
                        value -= 9

                    maze[(width * dx + x, height * dy + y)] = value

    return find_path_cost(maze)


print('Part 1: ', part1())
print('Part 2: ', part2())
