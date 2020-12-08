from fractions import gcd
from collections import defaultdict
import math


# lines
lines = [l.strip() for l in open('input') if l]
values = [list(v) for v in lines]


def get_visible_count(x, y):
    ratios = defaultdict(list)
    for j in range(0, len(values)):
        for i in range(0, len(values[0])):
            if x == i and y == j:
                continue
            if values[j][i] == '#':
                x_dist = x-i
                y_dist = y-j
                distance = (x_dist**2 + y_dist**2)**0.5
                den = abs(x_dist + y_dist if x_dist == 0 or y_dist == 0 else gcd(x_dist, y_dist))
                ratios[(x_dist / den, y_dist / den)].append((distance, i, j))
    return ratios


def part1():
    max_count = 0
    best = None

    for y in range(0, len(values)):
        for x in range(0, len(values[0])):
            if values[y][x] == '#':
                asteroid_count = len(get_visible_count(x, y))

                if asteroid_count > max_count:
                    max_count = asteroid_count
                    best = (x, y)

    print(best)
    return max_count


def part2():
    ratios = get_visible_count(25, 31)
    angles = {}

    for ratio, data in ratios.items():
        x, y = ratio
        angle = -math.atan2(x, y) % (2 * math.pi)
        angles[angle] = data

    asteroid = 0
    while True:
        for angle in sorted(angles.keys()):
            asteroid += 1

            asteroids_in_angle = angles[angle]
            asteroid_to_destroy = min(asteroids_in_angle)

            if asteroid == 200:
                return asteroid_to_destroy[1]*100 + asteroid_to_destroy[2]

            asteroids_in_angle.remove(asteroid_to_destroy)

            if len(asteroids_in_angle) == 0:
                angles.pop(angle)


print('Part 1: ', part1())
print('Part 2: ', part2())
