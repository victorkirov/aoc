from itertools import permutations
import operator
from cachetools import cached, LRUCache
from time import time

# strings
lines = [l.strip() for l in open('input') if l]
values = [v for v in lines]


active_set = set()

for y in range(0, len(values)):
    for x in range(0, len(values[y])):
       if values[y][x] == '#':
            active_set.add((x,y))


@cached(cache=LRUCache(maxsize=2))
def get_neighbour_permutations(dimensions):
    return set(permutations([0,1,-1] * dimensions, dimensions))


@cached(cache=LRUCache(maxsize=2))
def get_neighbour_permutations_ex_me(dimensions):
    neighbour_perm_list = [0] * (dimensions - 1) + [1,-1] * dimensions
    return set(permutations(neighbour_perm_list, dimensions))


def get_next_state(current_state, dimensions):
    positions_to_consider = set(
        tuple(map(operator.add, position, perm))
        for position in current_state
        for perm in get_neighbour_permutations(dimensions)
    )

    next_state = set()

    neighbour_perms = get_neighbour_permutations_ex_me(dimensions)
    for position in positions_to_consider:
        is_active = position in current_state
        active_neighbours = sum(
            1
            for perm in neighbour_perms
            if tuple(map(operator.add, position, perm)) in current_state
        )

        if (
            2 <= active_neighbours <= 3 and is_active
            or active_neighbours == 3 and not is_active
        ):
            next_state.add(position)

    return next_state


# parts
def run(runs, dimensions):
    result = set(i + (0,) * (dimensions - 2) for i in active_set)

    for _ in range(runs):
        result = get_next_state(result, dimensions)

    return len(result)


print('Part 1: ', run(6, 3))
print('Part 2: ', run(6, 4))
