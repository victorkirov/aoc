lines = [l.strip() for l in open('input') if l]
values = [((parts:=v.split(' '))[0], int(parts[1])) for v in lines]


def compute(input):
    acc = 0
    pos = 0

    visited = list()

    while pos < len(input):
        if pos in visited:
            return 'loop_detected', acc, visited
        visited.append(pos)

        [command, amount] = input[pos]

        if command == 'nop':
            pos += 1
        elif command == 'acc':
            acc += amount
            pos += 1
        elif command == 'jmp':
            pos += amount
        else:
            assert False == command

    return 'complete', acc, visited


def part2(visited_path):
    switch_mapping = {
        'jmp': 'nop',
        'nop': 'jmp',
    }

    for index in set(visited_path):
        val = values[index]
        if val[0] in switch_mapping:
            input = list(values)
            input[index] = (switch_mapping[val[0]], val[1])
            result = compute(input)

            if result[0] == 'complete':
                return result[1]


_, acc, visited_path = compute(values)

print('Part 1: ', acc)
print('Part 2: ', part2(visited_path))
