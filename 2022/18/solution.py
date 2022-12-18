from itertools import permutations

input_file_name = 'input'

lines = [l.strip() for l in open(input_file_name) if l]
values = set(
    [
        tuple([int(p) for p in v.split(',')])
        for v in lines
    ]
)

cardinal_dirs = [
    (-1, 0, 0),
    (1, 0, 0),
    (0, -1, 0),
    (0, 1, 0),
    (0, 0, -1),
    (0, 0, 1),
]

all_dirs = set(permutations([1,1,1,0,0,-1,-1,-1], 3))

def part1():
    result = 0

    for value in values:
        for dir in cardinal_dirs:
            if tuple(map(sum, zip(value, dir))) not in values:
                result += 1

    return result


def part2():
    result = 0

    max_depth = max([v[2] for v in values])
    bottom_piece = [v for v in values if v[2] == max_depth][0]

    perimeter_piece = tuple(map(sum, zip(bottom_piece, (0, 0, 1))))

    perimeter = { perimeter_piece }

    to_test = [perimeter_piece]

    while to_test:
        piece = to_test.pop()
        for dir in cardinal_dirs:
            new_piece = tuple(map(sum, zip(piece, dir)))
            if new_piece in values or new_piece in perimeter:
                continue

            for dir2 in all_dirs:
                new_piece_neighbour = tuple(map(sum, zip(new_piece, dir2)))

                if new_piece_neighbour in values:
                    perimeter.add(new_piece)
                    to_test.append(new_piece)
                    break

    for value in values:
        for dir in cardinal_dirs:
            if tuple(map(sum, zip(value, dir))) in perimeter:
                result += 1

    return result


print('Part 1: ', part1())
print('Part 2: ', part2())
