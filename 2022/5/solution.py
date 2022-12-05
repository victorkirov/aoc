import re
from collections import defaultdict

input_file_name = 'input'

def get_input():
    values = [l for l in open(input_file_name) if l]

    columns = defaultdict(list)

    while line:=values.pop(0):
        if line.strip() == '':
            break
        for i in range((len(line)+1) // 4):
            letter = line[i * 4 + 1]
            if letter != ' ':
                columns[i + 1].append(letter)

    for column in columns.values():
        column.pop()
    return columns, values

def part(rev=False):
    columns, instructions = get_input()

    for instruction in instructions:
        numbers = [int(x) for x in re.findall(r'\d+', instruction)]
        moved = columns[numbers[1]][:numbers[0]]
        columns[numbers[1]] = columns[numbers[1]][numbers[0]:]

        if(rev):
            moved.reverse()

        columns[numbers[2]] = [*moved, *columns[numbers[2]]]

    print(''.join([columns[column + 1][0] for column in range(len(columns))]))


print('Part 1: ', part(True))
print('Part 2: ', part())
