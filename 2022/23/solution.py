from collections import defaultdict

input_file_name = 'input'

values = [l.strip() for l in open(input_file_name) if l]

start_elf_positions = set()

for y, v in enumerate(values):
    for x, e in enumerate(v):
        if e == '#':
            start_elf_positions.add((x,y))

dir_diffs = {
    'n': (0, -1),
    's': (0, 1),
    'w': (-1, 0),
    'e': (1, 0),
}
dir_checks = {
    'n': [(0, -1), (1, -1), (-1, -1)],
    's': [(0, 1), (1, 1), (-1, 1)],
    'w': [(-1, 0), (-1, 1), (-1, -1)],
    'e': [(1, 0), (1, 1), (1, -1)],
}

# parts
def part1():
    dirs = ['n', 's', 'w', 'e']
    done = False
    elf_positions = start_elf_positions.copy()

    rounds = 0
    while not done and rounds < 10:
        rounds += 1

        proposed_positions = {}
        next_elf_positions = set()
        done = True

        for (x, y) in elf_positions:
            clear = True
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if (dx, dy) == (0, 0):
                        continue

                    if (x + dx, y + dy) in elf_positions:
                        clear = False
                        done = False


            if clear:
                next_elf_positions.add((x, y))
                continue

            for dir in dirs:
                dir_diff = dir_diffs[dir]
                avail = True
                for (dx, dy) in dir_checks[dir]:
                    if (x + dx, y + dy) in elf_positions:
                        avail = False
                        break

                if avail:
                    proposed_positions[(x, y)] = (x + dir_diff[0], y + dir_diff[1])
                    break

            if (x, y) not in proposed_positions:
                proposed_positions[(x, y)] = (x, y)

        proposed_counts = defaultdict(int)
        for (x, y) in proposed_positions.values():
            proposed_counts[(x, y)] += 1

        for current, proposed in proposed_positions.items():
            if proposed_counts[proposed] > 1:
                next_elf_positions.add(current)
            else:
                next_elf_positions.add(proposed)

        elf_positions = next_elf_positions

        dirs.append(dirs.pop(0))

    min_x = min([x for (x, y) in elf_positions])
    max_x = max([x for (x, y) in elf_positions])
    min_y = min([y for (x, y) in elf_positions])
    max_y = max([y for (x, y) in elf_positions])

    empties = 0

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) in elf_positions:
                print('#', end='')
            else:
                print('.', end='')
                empties += 1
        print()
    print()

    return empties


def part2():
    dirs = ['n', 's', 'w', 'e']
    done = False
    elf_positions = start_elf_positions.copy()

    rounds = 0
    while not done:
        rounds += 1

        proposed_positions = {}
        next_elf_positions = set()
        done = True

        for (x, y) in elf_positions:
            clear = True
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if (dx, dy) == (0, 0):
                        continue

                    if (x + dx, y + dy) in elf_positions:
                        clear = False
                        done = False


            if clear:
                next_elf_positions.add((x, y))
                continue

            for dir in dirs:
                dir_diff = dir_diffs[dir]
                avail = True
                for (dx, dy) in dir_checks[dir]:
                    if (x + dx, y + dy) in elf_positions:
                        avail = False
                        break

                if avail:
                    proposed_positions[(x, y)] = (x + dir_diff[0], y + dir_diff[1])
                    break

            if (x, y) not in proposed_positions:
                proposed_positions[(x, y)] = (x, y)

        proposed_counts = defaultdict(int)
        for (x, y) in proposed_positions.values():
            proposed_counts[(x, y)] += 1

        for current, proposed in proposed_positions.items():
            if proposed_counts[proposed] > 1:
                next_elf_positions.add(current)
            else:
                next_elf_positions.add(proposed)

        elf_positions = next_elf_positions

        dirs.append(dirs.pop(0))

    return rounds


print('Part 1: ', part1())
print('Part 2: ', part2())
