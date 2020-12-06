lines = [l.strip() for l in open('input') if l]
values = [v for v in lines]


def part1():
    group = set()
    group_items = []

    for value in values:
        group.update(set(list(value)))

        if not value:
            group_items.append(len(group))
            group = set()

    group_items.append(len(group))

    return sum(group_items)


def part2():
    group = None
    group_items = []

    for value in values:
        if group is None:
            group = set(list(value))
        elif value:
            group.intersection_update(set(list(value)))

        if not value:
            group_items.append(len(group))
            group = None

    group_items.append(len(group))

    return sum(group_items)


print('Part 1: ', part1())
print('Part 2: ', part2())
