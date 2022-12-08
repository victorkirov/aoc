from functools import reduce, cache
from collections import defaultdict
from itertools import product, combinations, permutations

input_file_name = 'input'

# strings
lines = [l.strip() for l in open(input_file_name) if l]
values = [
    [
        {
            'height': int(x),
            'visible': False
        }
         for x in list(v)
    ]
    for v in lines
]


def part1():
    def set_visibility(r1, r2, rev=False):
        for r in r1:
            height = -1
            for c in r2:
                tree = values[r][c] if rev else values[c][r]
                if tree['height'] > height:
                    tree['visible'] = True
                    height = tree['height']

    set_visibility(range(len(values)), range(len(values[0])))
    set_visibility(range(len(values)), range(len(values[0]) - 1, -1, -1))
    set_visibility(range(len(values[0])), range(len(values)), True)
    set_visibility(range(len(values[0])), range(len(values) - 1, -1, -1), True)

    visible = 0
    for row in values:
        for tree in row:
            if tree['visible']:
                visible += 1

    return visible


def part2():
    max_score = 0
    directions = [(0,1), (0,-1), (1,0), (-1,0)]

    for r in range(len(values)):
        for c in range(len(values[0])):
            current_score = 1
            for direction in directions:
                score = 0
                row = r
                col = c
                height = values[row][col]['height']
                while True:
                    row += direction[0]
                    col += direction[1]
                    if row < 0 or row >= len(values) or col < 0 or col >= len(values[0]):
                        break
                    score += 1
                    if values[row][col]['height'] >= height:
                        break
                current_score = current_score * score
            if current_score > max_score:
                max_score = current_score

    return max_score


print('Part 1: ', part1())
print('Part 2: ', part2())
