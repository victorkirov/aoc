from itertools import permutations, cycle

lines = [l.strip() for l in open('input') if l]
values = [int(value) for value in lines[0].split(',')]


def compute(input_values):
    input = list(values)
    index = 0

    while True:
        command_def = input[index]
        command = command_def % 100

        if command == 1:
            a = input[index + 1] if command_def // 100 % 10 == 1 else input[input[index + 1]]
            b = input[index + 2] if command_def // 1000 % 10 == 1 else input[input[index + 2]]
            input[input[index + 3]] = a + b
            index += 4
        elif command == 2:
            a = input[index + 1] if command_def // 100 % 10 == 1 else input[input[index + 1]]
            b = input[index + 2] if command_def // 1000 % 10 == 1 else input[input[index + 2]]
            input[input[index + 3]] = a * b
            index += 4
        elif command == 3:
            input[input[index + 1]] = input_values.pop(0)
            index += 2
        elif command == 4:
            next_input = yield input[input[index + 1]]
            input_values.append(next_input)
            index += 2
        elif command == 5:
            a = input[index + 1] if command_def // 100 % 10 == 1 else input[input[index + 1]]
            b = input[index + 2] if command_def // 1000 % 10 == 1 else input[input[index + 2]]

            if a != 0:
                index = b
            else:
                index += 3
        elif command == 6:
            a = input[index + 1] if command_def // 100 % 10 == 1 else input[input[index + 1]]
            b = input[index + 2] if command_def // 1000 % 10 == 1 else input[input[index + 2]]

            if a == 0:
                index = b
            else:
                index += 3
        elif command == 7:
            a = input[index + 1] if command_def // 100 % 10 == 1 else input[input[index + 1]]
            b = input[index + 2] if command_def // 1000 % 10 == 1 else input[input[index + 2]]
            input[input[index + 3]] = 1 if a < b else 0
            index += 4
        elif command == 8:
            a = input[index + 1] if command_def // 100 % 10 == 1 else input[input[index + 1]]
            b = input[index + 2] if command_def // 1000 % 10 == 1 else input[input[index + 2]]
            input[input[index + 3]] = 1 if a == b else 0
            index += 4
        elif command == 99:
            return


def compute_for_combo(combo):
    current_input = 0
    for phase in combo:
        current_input = next(compute([phase, current_input]))
    return current_input


def compute_for_combo_feedback(combo):
    current_input = 0

    engines = []

    for phase in combo:
        engine = compute([phase, current_input])
        engines.append(engine)

        output = next(engine)

        current_input = output

    for engine in cycle(engines):
        try:
            current_input = engine.send(current_input)
        except StopIteration:
            break

    return current_input



print('Part 1: ')
print(max([compute_for_combo(combo) for combo in permutations(list(range(0, 5)), 5)]))
print('Part 2: ')
print(max([compute_for_combo_feedback(combo) for combo in permutations(list(range(5, 10)), 5)]))
