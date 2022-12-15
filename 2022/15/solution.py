input_file_name = 'input'


def parse_line(line):
    parts = line.split(' ')
    return (
        int(parts[2].split('=')[1].split(',')[0]),
        int(parts[3].split('=')[1].split(':')[0])
    ), (
        int(parts[8].split('=')[1].split(',')[0]),
        int(parts[9].split('=')[1]),
    )


# strings
lines = [l.strip() for l in open(input_file_name) if l]
values = [parse_line(v) for v in lines]


def print_points(points):
    min_y = min([p[1] for p in points])
    max_y = max([p[1] for p in points])
    min_x = min([p[0] for p in points])
    max_x = max([p[0] for p in points])
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) in points:
                print(points[(x, y)], end='')
            else:
                print('.', end='')
        print()


# parts
def part1(y):
    points = {}

    for sensor, beacon in values:
        points[sensor] = 'S'
        points[beacon] = 'B'

        dist = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])

        for x in range(sensor[0] - dist, sensor[0] + dist):
            if (x, y) in points:
                continue
            if abs(sensor[0] - x) + abs(sensor[1] - y) > dist:
                continue
            points[(x, y)] = '#'

    return len([v for v in points.values() if v == '#'])


def get_limits_for_row(row):
    limits = []
    for sensor, beacon in values:
        dist = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])

        min_y = sensor[1] - dist
        max_y = sensor[1] + dist

        if min_y <= row <= max_y:
            diff = abs(abs(sensor[1] - row) - dist)
            limits.append((sensor[0] - diff, sensor[0] + diff))
    limits.sort(key=lambda x: x[0])
    return limits


def part2(max_c):
    for y in range(0, max_c + 1):
        limits = get_limits_for_row(y)

        x = 0
        for min_x, max_x in limits:
            if min_x > x:
                return (x+1) * 4000000 + y
            x = max(x, max_x)


print('Part 1: ', part1(2000000))
print('Part 2: ', part2(4000000))
