input_file_name = 'input'

values = [l.strip() for l in open(input_file_name) if l]

rock_map = set()

for v in values:
    points = [
        (int(c.split(',')[0]), int(c.split(',')[1]))
        for c in v.split(' -> ')
    ]

    prev_point = None
    for point in points:
        if prev_point == None:
            prev_point = point
            continue

        x_start = min(prev_point[0], point[0])
        x_end = max(prev_point[0], point[0])
        y_start = min(prev_point[1], point[1])
        y_end = max(prev_point[1], point[1])

        for x in range(x_start, x_end + 1):
            for y in range(y_start, y_end + 1):
                rock_map.add((x, y))
        prev_point = point

min_y = min([p[1] for p in rock_map])
max_y = max([p[1] for p in rock_map])
min_x = min([p[0] for p in rock_map])
max_x = max([p[0] for p in rock_map])

def print_map(sand_pos):
    min_y = min([p[1] for p in rock_map.union(sand_pos)])
    max_y = max([p[1] for p in rock_map.union(sand_pos)])
    min_x = min([p[0] for p in rock_map.union(sand_pos)])
    max_x = max([p[0] for p in rock_map.union(sand_pos)])
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) in rock_map:
                print('#', end='')
            elif (x, y) in sand_pos:
                print('O', end='')
            else:
                print('.', end='')
        print()

def part1():
    sand = set()

    dirs = [
        (0, 1),
        (-1, 1),
        (1, 1),
    ]

    sand_added = True

    while sand_added:
        sand_added = False
        sand_pos = (500, 0)

        while sand_pos[1] <= max_y:
            moved = False

            for dir in dirs:
                new_pos = (sand_pos[0] + dir[0], sand_pos[1] + dir[1])
                if new_pos not in rock_map and new_pos not in sand:
                    moved = True
                    sand_pos = new_pos
                    break

            if not moved:
                sand.add(sand_pos)
                sand_added = True
                break

    return len(sand)


def part2():
    sand = set()

    dirs = [
        (0, 1),
        (-1, 1),
        (1, 1),
    ]

    last_pos = None

    while last_pos != (500, 0):
        sand_pos = (500, 0)
        last_pos = None

        while True:
            moved = False

            for dir in dirs:
                if sand_pos[1] + dir[1] > max_y + 1:
                    break
                new_pos = (sand_pos[0] + dir[0], sand_pos[1] + dir[1])
                if new_pos not in rock_map and new_pos not in sand:
                    moved = True
                    sand_pos = new_pos
                    break

            if not moved:
                sand.add(sand_pos)
                last_pos = sand_pos
                break
    print_map(sand)

    return len(sand)


print('Part 1: ', part1())
print('Part 2: ', part2())
