from functools import cache
import time

input_file_name = 'input'
input_file_name = 'test'

lines = [l.strip() for l in open(input_file_name) if l]
values = [v for v in lines]

nodes = {}

for value in values:
    parts = value.split(' ')
    parent = parts[1]
    rate = int(parts[4].split('=')[1].split(';')[0])

    children = [c.strip(',') for c in parts[9:]]

    nodes[parent] = {
        'name': parent,
        'rate': rate,
        'children': children
    }


def part1():
    @cache
    def get_min_path_len(current_node_name, target_node_name, visited_nodes):
        current_node = nodes[current_node_name]
        if target_node_name in current_node['children']:
            return 1

        min_path_len = 999999999
        for child in current_node['children']:
            if child not in visited_nodes:
                min_path_len = min(
                    min_path_len,
                    get_min_path_len(child, target_node_name, visited_nodes + ',' + current_node_name) + 1
                )

        return min_path_len

    def move_next_node(current_node_name, time_left, released_pressure, available_nodes):
        if time_left <= 0 or available_nodes == []:
            return released_pressure

        max_rate = released_pressure

        for node in available_nodes:
            path_len = get_min_path_len(current_node_name, node['name'], '')

            if path_len > time_left + 1:
                continue

            max_rate = max(
                max_rate,
                move_next_node(
                    node['name'],
                    time_left - path_len - 1,
                    released_pressure + (time_left - path_len - 1) * node['rate'],
                    [n for n in available_nodes if n['name'] != node['name']],
                )
            )

        return max_rate

    available_nodes = [
        node
        for node in nodes.values()
        if node['rate'] > 0
    ]

    return move_next_node('AA', 26, 0, available_nodes)


runs = 0
def part2():
    @cache
    def get_min_path_len(current_node_name, target_node_name, visited_nodes):
        current_node = nodes[current_node_name]
        if target_node_name in current_node['children']:
            return 1

        min_path_len = 999999999
        for child in current_node['children']:
            if child not in visited_nodes:
                min_path_len = min(
                    min_path_len,
                    get_min_path_len(child, target_node_name, visited_nodes + ',' + current_node_name) + 1
                )

        return min_path_len

    def move_next_node(man_current, man_time, el_current, el_time, available_nodes_in):
        available_nodes_in.sort()
        available_nodes_str = ','.join(available_nodes_in)

        @cache
        def move_next_node_(l_current, l_time, r_current, r_time, available_nodes_str):
            global runs
            runs += 1

            if available_nodes_str == '':
                return 0

            available_nodes = available_nodes_str.split(',')

            max_rate = 0

            if l_time > r_time:
                min_current_node = r_current
                min_time = r_time
                max_current_node = l_current
                max_time = l_time
            else:
                min_current_node = l_current
                min_time = l_time
                max_current_node = r_current
                max_time = r_time

            for node_name in available_nodes:
                node = nodes[node_name]
                path_len = get_min_path_len(max_current_node, node['name'], '')

                if path_len >= max_time + 1:
                    continue

                next_available = [n for n in available_nodes if n != node['name']]
                next_available.sort()

                node_rate = (max_time - path_len - 1) * node['rate']

                if min_time > max_time - path_len - 1:
                    next_rate = move_next_node_(
                        min_current_node,
                        min_time,
                        node['name'],
                        max_time - path_len - 1,
                        ','.join(next_available),
                    )
                else:
                    next_rate = move_next_node_(
                        node['name'],
                        max_time - path_len - 1,
                        min_current_node,
                        min_time,
                        ','.join(next_available),
                    )

                max_rate = max(
                    max_rate,
                    node_rate + next_rate
                )

            return max_rate

        return move_next_node_(man_current, man_time, el_current, el_time, available_nodes_str)

    available_nodes = [
        node['name']
        for node in nodes.values()
        if node['rate'] > 0
    ]

    return move_next_node('AA', 26, 'AA', 26, available_nodes)


start = time.perf_counter()
print('Part 1: ', part1())
print('Time: ', time.perf_counter() - start, 's')

start = time.perf_counter()
print('Part 2: ', part2())
print('Time: ', time.perf_counter() - start, 's')
print(runs)
