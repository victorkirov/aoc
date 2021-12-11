from functools import reduce
from collections import defaultdict
from itertools import product, combinations, permutations

# strings
lines = [l.strip() for l in open('input') if l]
values = [v for v in lines]


# parts
def part1():
    counts = defaultdict(lambda: 0)

    for value in values:
        [start, end] = value.split(' -> ')
        [startX, startY] = [int(c) for c in start.split(',')]
        [endX, endY] = [int(c) for c in end.split(',')]

        if startX == endX:
            minY = min(startY, endY)
            maxY = max(startY, endY)
            for y in range(minY, maxY + 1):
                counts[(startX, y)] += 1

        if startY == endY:
            minX = min(startX, endX)
            maxX = max(startX, endX)
            for x in range(minX, maxX + 1):
                counts[(x, startY)] += 1

    return sum([
        1 if x > 1 else 0
        for x in counts.values()
    ])


def part2():
    counts = defaultdict(lambda: 0)

    for value in values:
        [start, end] = value.split(' -> ')
        [startX, startY] = [int(c) for c in start.split(',')]
        [endX, endY] = [int(c) for c in end.split(',')]

        x = startX
        y = startY
        counts[(x, y)] += 1
        while x != endX or y != endY:
            x += (
                0 if startX == endX
                else 1 if startX < endX
                else -1
            )
            y += (
                0 if startY == endY
                else 1 if startY < endY
                else -1
            )
            counts[(x, y)] += 1

    for x in range(0,10):
        for y in range(0,10):
            print(str(counts[(x,y)]) if (x,y) in counts else '.', end='')
        print()

    return sum([
        1 if x > 1 else 0
        for x in counts.values()
    ])


print('Part 1: ', part1())
print('Part 2: ', part2())
