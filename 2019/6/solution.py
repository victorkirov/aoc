from collections import defaultdict

lines = [l.strip() for l in open('input') if l]
values = [v.split(')') for v in lines]

parent_to_child_mapping = defaultdict(list)
child_to_parent_mapping = defaultdict(list)

for value in values:
    parent_to_child_mapping[value[0]].append(value[1])
    child_to_parent_mapping[value[1]].append(value[0])

def part1():
    to_visit = [('COM', 0)]

    direct = 0
    indirect = 0

    while to_visit:
        current, distance_from_com = to_visit.pop()

        if current in parent_to_child_mapping:
            children = parent_to_child_mapping[current]
            direct += len(children)
            indirect += len(children) * distance_from_com

            to_visit += list(zip(children, [distance_from_com + 1] * len(children)))

    return direct + indirect


def part2():
    visited = set()

    def get_min_distance_to_san(node, distance):
        visited.update({node})

        destinations = child_to_parent_mapping[node] + parent_to_child_mapping.get(node, [])

        min_distance = None
        for destination in destinations:
            if destination in visited:
                continue
            distance_to_san = distance + 1 if destination == 'SAN' else get_min_distance_to_san(destination, distance + 1)
            if distance_to_san:
                min_distance = distance_to_san if min_distance is None or min_distance > distance_to_san else min_distance

        return min_distance


    return get_min_distance_to_san('YOU', 0) - 2


print('Part 1: ', part1())
print('Part 2: ', part2())
