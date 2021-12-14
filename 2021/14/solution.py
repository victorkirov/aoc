from functools import reduce
from collections import defaultdict, Counter
from itertools import product, combinations, permutations
from cachetools import cached, TTLCache

cache = TTLCache(maxsize=1000000000, ttl=86400)

# groups
data = open('input').read()
values = [v.strip() for v in data.split('\n\n')]
values = [v.split('\n') for v in values]

[template, insertions] = values

instructions = {
    v.split(' -> ')[0]: v.split(' -> ')[1]
    for v in insertions
}

# parts
def part1():
    runs = 0
    polymer = template[0]

    while runs < 10:
        runs += 1

        new_polymer = ''

        last_c = None
        for c in list(polymer):
            if not last_c:
                new_polymer += c
                last_c = c
                continue

            pair = f'{last_c}{c}'
            if pair in instructions:
                new_polymer += instructions[pair]
            last_c = c

            new_polymer += c

        polymer = new_polymer

    counts = Counter(list(polymer))
    return max(counts.values()) - min(counts.values())


@cached(cache)
def counts_for_pair(left, right, depth):
    if depth == 0:
        return {}

    pair = f'{left}{right}'

    middle = instructions[pair]

    left_counts = counts_for_pair(left, middle, depth - 1)
    right_counts = counts_for_pair(middle, right, depth - 1)

    counts = defaultdict(lambda: 0)
    counts[middle] += 1

    for key, value in left_counts.items():
        counts[key] += value
    for key, value in right_counts.items():
        counts[key] += value

    return counts


def part2():
    polymer = template[0]

    counts = defaultdict(lambda: 0)

    last_c = None
    for c in list(polymer):
        counts[c] += 1

        if not last_c:
            last_c = c
            continue

        inner_counts = counts_for_pair(last_c, c, 40)

        for key, value in inner_counts.items():
            counts[key] += value

        last_c = c

    return max(counts.values()) - min(counts.values())


print('Part 1: ', part1())
print('Part 2: ', part2())
