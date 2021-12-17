from functools import reduce
from collections import defaultdict
from itertools import product, combinations, permutations

# target area: x=156..202, y=-110..-69

t_minx = 156
t_maxx = 202
t_miny = -110
t_maxy = -69


def test_trajectory(i_x, i_y):
    x = 0
    y = 0
    topy = 0

    while x < t_maxx and y > t_miny:
        x += max(i_x, 0)
        i_x -= 1

        y += i_y
        i_y -= 1

        topy = max(y, topy)

        if t_minx <= x <= t_maxx and t_miny <= y <= t_maxy:
            return topy

    return -1

best_y = 0
counts = 0

for x in range(t_maxx + 1):
    for y in range(t_miny, -t_miny):
        top = test_trajectory(x, y)
        best_y = max(top, best_y)
        counts += 1 if test_trajectory(x, y) != -1 else 0

print('Part1 -> ', best_y)
print('Part2 -> ', counts)
