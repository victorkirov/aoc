lines = [l.strip() for l in open('input') if l]
values = [int(value) for value in lines[0].split(',')]


def compute(input_values):
    input = list(values)
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


def paint(initial_colour):
    x = y = 0
    direction_x = 0
    direction_y = 1

    colours = {}

    r = compute([initial_colour])
    new_colour = next(r)

    try:
        while(True):
            turn = next(r)

            colours[(x ,y)] = new_colour

            direction_x, direction_y = direction_y, direction_x
            if turn == 0 and direction_x:
                direction_x *= -1
            elif turn ==1 and direction_y:
                direction_y *= -1

            x += direction_x
            y += direction_y

            colour = colours.get((x, y), initial_colour)
            new_colour = r.send(colour)
    except StopIteration:
        pass

    return colours


def part1():
    return paint(0)

def part2():
    colours = paint(1)

    min_x = min([c[0] for c in colours])
    max_x = max([c[0] for c in colours])
    min_y = min([c[1] for c in colours])
    max_y = max([c[1] for c in colours])

    for y in range(max_y, min_y - 1, -1):
        line = ''
        for x in range(min_x, max_x + 1):
            colour = colours.get((x,y), 0)
            line += ' ' if not colour else '#'
        print(line)

print('Part 1: ')
print(len(part1()))
print('Part 2: ')
part2()
