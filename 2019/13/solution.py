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


mapping = {
    0: ' ',
    1: '#',
    2: '+',
    3: '_',
    4: 'O'
}


def part1():
    g = compute([])
    screen = {}

    try:
        while(True):
            x = next(g)
            y = next(g)
            type = next(g)

            screen[(x,y)] = type

    except StopIteration:
        pass

    return list(screen.values()).count(2)

def part2():
    values[0] = 2
    player_input = [0]
    g = compute(player_input)
    screen = {}

    x = next(g)
    y = next(g)
    type = next(g)

    previous_ball_position = None
    ball_position = None
    player_position = None

    try:
        while(True):
            screen[(x,y)] = type

            x = next(g)
            y = next(g)
            type = next(g)

            if type == 4:
                previous_ball_position = ball_position
                ball_position = (x, y)

                if player_position and previous_ball_position:
                    dx = player_position[0] - ball_position[0]
                    if dx < 0:
                        player_input.append(1)
                    elif dx > 0:
                        player_input.append(-1)
                    else:
                        player_input.append(0)

            if type == 3:
                player_position = (x, y)

            # if len(screen) >= 736 and 4 in screen.values() and 3 in screen.values():
            #     print_screen(screen)

    except StopIteration:
        pass

    print_screen(screen)

def print_screen(screen):
    for y in range(0, max([y for _, y in screen]) + 1):
        row = ''
        for x in range(0, max([x for x, _ in screen]) + 1):
            row += mapping[screen.get((x, y), 0)]
        print(row)
    print('Score', screen[(-1, 0)])


print('Part 1: ',part1())
print('Part 2: ', part2())
