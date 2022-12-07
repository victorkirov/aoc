from functools import reduce, cache
from collections import defaultdict
from itertools import product, combinations, permutations

input_file_name = 'input'

values = [l.strip() for l in open(input_file_name) if l]

dirs = {
    'parent': None,
    'files': []
}

current_dir = dirs
for value in values:
    parts = value.split(' ')
    if parts[0] == '$':
        cmd = parts[1]

        if cmd == 'cd':
            if parts[2] == '/':
                current_dir = dirs
            elif parts[2] == '..':
                current_dir = current_dir['parent']
            else:
                if parts[2] not in current_dir:
                    current_dir[parts[2]] = {
                        'parent': current_dir,
                        'files': []
                    }
                current_dir = current_dir[parts[2]]
        elif cmd == 'ls':
            pass
    else:
        if parts[0] == 'dir':
            continue
        current_dir['files'].append(int(parts[0]))


def add_sizes(path):
    size = sum(path['files'])

    for key, value in path.items():
        if key in ['parent', 'files']:
            continue

        size += add_sizes(value)

    path['size'] = size

    return size


add_sizes(dirs)


def part1():
    def get_small_sizes(path, size):
        large = []

        if path['size'] <= size:
            large.append(path['size'])

        for key, value in path.items():
            if key in ['parent', 'files', 'size']:
                continue

            large += get_small_sizes(value, size)

        return large

    return sum(get_small_sizes(dirs, 100000))


def part2():
    hd_size = 70000000
    need_size = 30000000
    free_size = hd_size - dirs['size']

    min_size_to_delete = need_size - free_size

    def find_smallest_dir_to_delete(path, size):
        if path['size'] <= size:
            return None

        current_smallest = path['size']

        for key, value in path.items():
            if key in ['parent', 'files', 'size']:
                continue

            smallest = find_smallest_dir_to_delete(value, size)
            if smallest and smallest < current_smallest:
                current_smallest = smallest
        return current_smallest

    return find_smallest_dir_to_delete(dirs, min_size_to_delete)


print('Part 1: ', part1())
print('Part 2: ', part2())
