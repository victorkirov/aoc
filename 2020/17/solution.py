from itertools import permutations
import operator

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
            neighbour = tuple(map(operator.add, position, perm))
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
def run(runs, dimensions):
    result = get_input_set(dimensions)

    for i in range(runs):
        result = get_next_state(result, dimensions)

    return len(result)


print('Part 1: ', run(6, 3))
print('Part 2: ', run(6,4 ))
