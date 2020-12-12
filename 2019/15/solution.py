from copy import deepcopy
from itertools import permutations

lines = [l.strip() for l in open('input') if l]
values = [int(value) for value in lines[0].split(',')]


def compute(input_values, code):
    input = list(code)
    index = 0
    relative_mode_index = 0

    while True:
        command_def = input[index]
        command = command_def % 100

        def get_address(offset):
            mode = (command_def // (10 * 10**offset)) % 10

            if mode == 0:
                return input[index + offset]
            elif mode == 1:
                return index + offset
            elif mode == 2:
                return input[index + offset] + relative_mode_index

            assert False == mode

        def get(offset):
            address = get_address(offset)

            if address < 0:
                raise IndexError()
            return input[address % len(input)]

        def set(offset, value):
            address = get_address(offset)
            if address < 0:
                raise IndexError()
            if address >= len(input):
                input.extend([0] * (address - len(input) + 1))

            input[address] = value


        if command == 1:
            a = get(1)
            b = get(2)
            set(3, a + b)
            index += 4
        elif command == 2:
            a = get(1)
            b = get(2)

            set(3, a * b)
            index += 4
        elif command == 3:
            set(1, input_values.pop(0))
            index += 2
        elif command == 4:
            next_input = yield get(1)
            if next_input is not None:
                input_values.append(next_input)
            index += 2
        elif command == 5:
            a = get(1)
            b = get(2)

            if a != 0:
                index = b
            else:
                index += 3
        elif command == 6:
            a = get(1)
            b = get(2)

            if a == 0:
                index = b
            else:
                index += 3
        elif command == 7:
            a = get(1)
            b = get(2)
            set(3, 1 if a < b else 0)
            index += 4
        elif command == 8:
            a = get(1)
            b = get(2)
            set(3, 1 if a == b else 0)
            index += 4
        elif command == 9:
            a = get(1)
            relative_mode_index += a
            index += 2
        elif command == 99:
            return


# north = 1
# south = 2
# west = 3
# east = 4

mapp = { (0, 0): '.' }

move_map = {
    1: (0, -1, 2),
    2: (0, 1, 1),
    3: (-1 , 0, 4),
    4: (1, 0, 3)
}

def print_map(map_to_print):
    for y in range(min([y for _, y in map_to_print]), max([y for _, y in map_to_print]) + 1):
        row = ''
        for x in range(min([x for x, _ in map_to_print]), max([x for x, _ in map_to_print]) + 1):
            row += map_to_print.get((x, y), ' ')
        print(row)


def explore(x, y, g, distance):
    for dir, (dx, dy, undo) in move_map.items():
        if (x + dx, y + dy) in mapp:
            continue
        if g is None:
            g = compute([dir], values)
            result = next(g)
        else:
            result = g.send(dir)

        if result == 0:
            mapp[(x + dx, y + dy)] = '#'
        elif result == 1:
            nx = x + dx
            ny = y + dy
            mapp[(nx, ny)] = '.'
            explore(nx, ny, g, distance + 1)
            g.send(undo)
        elif result == 2:
            nx = x + dx
            ny = y + dy
            mapp[(nx, ny)] = 'o'
            print('Found oxygen at ', distance + 1)
            explore(nx, ny, g, distance + 1)
            g.send(undo)

def part1():
    explore(0, 0, None, 0)
    print_map(mapp)

def part2():
    miny = min([y for _, y in mapp])
    maxy = max([y for _, y in mapp])

    minx = min([x for x, _ in mapp])
    maxx = max([x for x, _ in mapp])

    map2 = deepcopy(mapp)
    mins = 0

    while '.' in map2.values():
        mins += 1
        map2_ = deepcopy(mapp)

        for y in range(miny, maxy + 1):
            for x in range(minx, maxx + 1):
                if (x, y) not in map2 or map2[(x, y)] != 'o':
                    continue
                for (dx, dy) in {(0, 1), (0, -1), (1, 0), (-1, 0)}:
                    if map2_.get((x + dx, y + dy)) == '.':
                        map2_[(x + dx, y + dy)] = 'o'

        map2 = map2_

    return mins

print('Part 1: ',part1())
print('Part 2: ', part2())
