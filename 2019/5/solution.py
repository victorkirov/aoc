lines = [l.strip() for l in open('input') if l]
values = [int(value) for value in lines[0].split(',')]


def compute(input_value):
    input = list(values)
    index = 0

    while (command_def:=input[index]) != 99:
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
            input[input[index + 1]] = input_value
            index += 2
        elif command == 4:
            print(input[input[index + 1]])
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


print('Part 1: ')
compute(1)
print('Part 2: ')
compute(5)
