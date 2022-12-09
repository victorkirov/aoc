from functools import reduce, cache
from collections import defaultdict
from itertools import product, combinations, permutations

input_file_name = 'input'

lines = [l.strip() for l in open(input_file_name) if l]
values = [
    (v.split()[0], int(v.split()[1]))
    for v in lines
]

dirs = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1),
}


def part(number_of_knots):
    r = [(0, 0)] * number_of_knots

    visited = { r[-1] }

    for i in values:
        d = i[0]
        v = i[1]

        delta = dirs[d]

        for _ in range(v):
            h = r[0]
            r[0] = (h[0] + delta[0], h[1] + delta[1])

            for i in range(len(r) - 1):
                h = r[i]
                t = r[i + 1]

                dx = h[0] - t[0]
                dy = h[1] - t[1]

                if abs(dx) > 0 and abs(dy) > 1 or abs(dx) > 1 and abs(dy) > 0:
                    t = (t[0] + dx // abs(dx), t[1]+ dy // abs(dy))
                elif abs(dx) > 1:
                    t = (t[0] + dx // abs(dx), t[1])
                elif abs(dy) > 1:
                    t = (t[0], t[1] + dy // abs(dy))

                r[i + 1] = t

                if i + 1 == len(r) - 1:
                    visited.add(t)

    return len(visited)


print('Part 1: ', part(2))
print('Part 2: ', part(10))
