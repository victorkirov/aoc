import collections

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


print('Part 1: ')
print(next(compute([1])))
print('Part 2: ')
print(next(compute([2])))
