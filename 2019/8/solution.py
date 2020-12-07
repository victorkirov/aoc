from collections import Counter

line = open('input').readline().strip()
layer_size = 25 * 6
index = 0
values = []

while index < len(line):
    values.append(line[index:index+layer_size])
    index += layer_size


def part1():
    best_row = None

    for value in values:
        counts = Counter(value)
        best_row = counts if best_row is None or best_row['0'] > counts['0'] else best_row

    return best_row['1'] * best_row['2']


def part2():
    def get_colour(pixel):
        for colour in pixel:
            if colour != '2':
                return colour
        return '2'

    image = "".join(map(get_colour, zip(*values)))
    index = 0
    while index < len(image):
        print(image[index: index + 25].replace('0', ' ').replace('1', '#'))
        index += 25


print('Part 1: ', part1())
print('Part 2: ')
part2()
