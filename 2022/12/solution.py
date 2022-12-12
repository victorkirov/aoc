input_file_name = 'input'

values = [l.strip() for l in open(input_file_name) if l]

start_pos = (None, None)
end_pos = (None, None)
cells = {}
for y, row in enumerate(values):
    for x, cell in enumerate(row):
        if cell == 'S':
            start_pos = (x, y)
            cells[(x, y)] = ord('a')
        elif cell == 'E':
            end_pos = (x, y)
            cells[(x, y)] = ord('z')
        else:
            cells[(x, y)] = ord(cell)

dirs = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
]

def part1():
    visited = {
        start_pos: {
            'moves': 0,
        }
    }
    to_visit = [start_pos]

    while len(to_visit) > 0:
        min_moves = min([visited[pos]['moves'] for pos in to_visit])
        to_visit_next = [pos for pos in to_visit if visited[pos]['moves'] == min_moves]

        my_pos = to_visit_next[0]
        to_visit.remove(my_pos)

        current_moves = visited[my_pos]['moves']

        for dx, dy in dirs:
            next_pos = (my_pos[0] + dx, my_pos[1] + dy)
            if next_pos in visited and visited[next_pos]['moves'] <= current_moves + 1:
                continue
            if (
                next_pos in cells
                and cells[next_pos] <= cells[my_pos] + 1
            ):
                visited[next_pos] = {
                    'moves': current_moves + 1,
                }
                if next_pos != end_pos:
                    to_visit.append(next_pos)

    return visited[end_pos]['moves']


def part2():
    visited = {
        end_pos: {
            'moves': 0,
        }
    }
    to_visit = [end_pos]

    while len(to_visit) > 0:
        min_moves = min([visited[pos]['moves'] for pos in to_visit])
        to_visit_next = [pos for pos in to_visit if visited[pos]['moves'] == min_moves]

        my_pos = to_visit_next[0]
        to_visit.remove(my_pos)

        current_moves = visited[my_pos]['moves']

        for dx, dy in dirs:
            next_pos = (my_pos[0] + dx, my_pos[1] + dy)
            if next_pos in visited and visited[next_pos]['moves'] <= current_moves + 1:
                continue
            if (
                next_pos in cells
                and cells[next_pos] >= cells[my_pos] - 1
            ):
                visited[next_pos] = {
                    'moves': current_moves + 1,
                }
                if cells[next_pos] == ord('a'):
                    return visited[next_pos]['moves']

                to_visit.append(next_pos)


print('Part 1: ', part1())
print('Part 2: ', part2())
