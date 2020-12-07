# lines
lines = [l.strip() for l in open('input') if l]
values = [v.split(',') for v in lines]


def part1():
    wire_map = {}
    smallest = None

    for index, wire_paths in enumerate(values):
        x = 0
        y = 0
        for path in wire_paths:
            direction = path[0]
            distance = int(path[1:])

            while distance > 0:
                if direction == 'U':
                    y += 1
                if direction == 'D':
                    y -= 1
                if direction == 'R':
                    x += 1
                if direction == 'L':
                    x -= 1

                if (x, y) not in wire_map:
                    wire_map[(x, y)] = 0

                wire_map[(x, y)] |= 2**index

                if wire_map[(x, y)] == 3:
                    current = abs(x) + abs(y)
                    smallest = current if smallest is None or smallest > current else smallest

                distance -= 1

    return smallest


def part2():
    wire_map = {}
    smallest = None

    for index, wire_paths in enumerate(values):
        x = 0
        y = 0
        steps = 0

        for path in wire_paths:
            direction = path[0]
            distance = int(path[1:])

            while distance > 0:
                steps += 1
                if direction == 'U':
                    y += 1
                if direction == 'D':
                    y -= 1
                if direction == 'R':
                    x += 1
                if direction == 'L':
                    x -= 1

                if (x, y) not in wire_map:
                    wire_map[(x, y)] = [-1, -1]

                wire_map[(x, y)][index] = steps

                if -1 not in wire_map[(x, y)]:
                    current = sum(wire_map[(x, y)])
                    smallest = current if smallest is None or smallest > current else smallest

                distance -= 1

    return smallest


print('Part 1: ', part1())
print('Part 2: ', part2())
