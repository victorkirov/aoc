from itertools import permutations

# strings
lines = [l.strip() for l in open('input') if l]
values = [v for v in lines]


active_set = set()

for y in range(0, len(values)):
    for x in range(0, len(values[y])):
       if values[y][x] == '#':
            active_set.add((x,y))


def get_next_state(current_state, dimensions):
    neighbour_perm_list = [0] * (dimensions - 1) + [1,-1] * dimensions
    neighbour_perms = set(permutations(neighbour_perm_list, dimensions))

    positions = None
    for dim in range(0,dimensions):
        mind = min([c[dim] for c in current_state]) - 1
        maxd = max([c[dim] for c in current_state]) + 1

        if positions is None:
            positions = [(i,) for i in range(mind, maxd + 1)]
        else:
            next_postions = []
            for position in positions:
                for i in range(mind, maxd + 1):
                    next_postions.append(position + (i,))
            positions = next_postions

    next_state = set()
    for position in positions:
        is_active = position in current_state
        active_neighbours = 0

        for perm in neighbour_perms:
            neighbour = tuple([sum(i) for i in zip(position,perm)])
            if neighbour in current_state:
                active_neighbours += 1
            if active_neighbours >= 4:
                break
        if (
            2 <= active_neighbours <= 3 and is_active
            or active_neighbours == 3 and not is_active
        ):
            next_state.add(position)

    return next_state


def get_input_set(dimensions):
    add_dims = dimensions - 2
    return set([i + (0,) * add_dims for i in active_set])

# parts
def part1():
    result = get_input_set(3)

    for i in range(6):
        result = get_next_state(result, 3)

    return len(result)


def part2():
    result = get_input_set(4)

    for i in range(6):
        result = get_next_state(result, 4)

    return len(result)


print('Part 1: ', part1())
print('Part 2: ', part2())
