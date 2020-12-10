from collections import defaultdict

# lines
data = [l.strip() for l in open('input') if l]
values = [int(v) for v in data]

j_map = defaultdict(list)

for adapter in values:
    for inner in values:
        if adapter == inner:
            continue
        if inner > adapter and inner <= adapter + 3:
            j_map[adapter].append(inner)


def part1():
    previous_item = 0
    counts = {1:0, 2:0, 3:1} # '3' maps to 1 for the final jump

    for item in sorted(values):
        counts[item - previous_item] += 1
        previous_item = item

    return counts[1] * counts[3]


def count_paths(start, counts):
    if start not in j_map:
        counts[start] = 1
        return 1

    if start in counts:
        return counts[start]

    counts[start] = sum([count_paths(item, counts) for item in j_map[start]])
    return counts[start]


def part2():
    to_check = list(set(range(1,4))&set(j_map))
    counts = {}

    return sum([count_paths(item, counts) for item in to_check])


print('Part 1: ', part1())
print('Part 2: ', part2())
