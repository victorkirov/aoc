from functools import reduce
from collections import defaultdict
import operator

# groups
data = open('input').read()
values = [v.strip() for v in data.split('\n\n')]
values = [v.split('\n') for v in values]

tiles = defaultdict(list)
edges = defaultdict(list)


for value in values:
    title = None

    for line in value:
        if title is None:
            title = int(line.split(' ')[1].strip(':'))
            continue
        tiles[title].append(line)

    left = []
    right = []
    for line in value[1:]:
        left.append(line[0])
        right.append(line[-1])

    edges[title] = [value[1], ''.join(right), ''.join(value[-1]), ''.join(left)]

all_edges = [edge_item for edge in edges.values() for edge_item in edge]

# parts
def part1():
    corners = []
    sides = []

    for tile_id, tile_edges in edges.items():
        outside_edge_count = 0
        for tile_edge in tile_edges:
            if (
                all_edges.count(tile_edge) % 2 != 0
                and all_edges.count(''.join(reversed(tile_edge))) == 0
            ):
                outside_edge_count += 1

        if outside_edge_count == 2:
            corners.append(tile_id)

        if outside_edge_count == 1:
            sides.append(tile_id)

    return corners, sides


def flip_v(tile):
    return list(reversed(tile))


def flip_h(tile):
    return [list(reversed(tile_row)) for tile_row in tile]

def rotate(tile):
    rotated_tile = []
    for x in range(0, len(tile[0])):
        new_row = []
        for y in range(len(tile) - 1, -1, -1):
            new_row.append(tile[y][x])

        rotated_tile.append(''.join(new_row))
    return rotated_tile


def get_edges(tile):
    left = []
    right = []
    for line in tile:
        left.append(line[0])
        right.append(line[-1])

    return tile[0], ''.join(right), ''.join(tile[-1]), ''.join(left)


def is_match(row):
    match_count = all_edges.count(row)
    rev_match_count = all_edges.count(''.join(reversed(row)))
    return match_count + rev_match_count > 1


def find_match_left(tile, desired_left):
    _, _, _, left = get_edges(tile)

    if left == desired_left:
        return tile

    transformed_tile = tile
    # v_flip
    for _ in [0, 1]:
        # h_flip
        for _ in [0, 1]:
            # rotation
            for _ in range(0, 4):
                transformed_tile = rotate(transformed_tile)
                _, _, _, left = get_edges(transformed_tile)

                if left == desired_left:
                    return transformed_tile

            transformed_tile = flip_h(transformed_tile)
        transformed_tile = flip_v(transformed_tile)

    return None


def find_match(tile, desired_top, desired_left):
    top, _, _, left = get_edges(tile)

    if (not desired_left or left == desired_left) and (not desired_top or top == desired_top):
        return tile

    transformed_tile = tile
    # v_flip
    for _ in [0, 1]:
        # h_flip
        for _ in [0, 1]:
            # rotation
            for _ in range(0, 4):
                transformed_tile = rotate(transformed_tile)
                top, _, _, left = get_edges(transformed_tile)

                if (not desired_left or left == desired_left) and (not desired_top or top == desired_top):
                    return transformed_tile

            transformed_tile = flip_h(transformed_tile)
        transformed_tile = flip_v(transformed_tile)

    return None


def part2():
    corners, sides = part1()

    image = []

    # find top left corner in correct orientation
    corner_id = corners[0]
    corner_tile = tiles[corner_id]

    c_top, c_right, _, c_left = get_edges(corner_tile)
    while is_match(c_top) or is_match(c_left):
        corner_tile = rotate(corner_tile)
        c_top, c_right, _, c_left = get_edges(corner_tile)

    image.append([corner_tile])
    processed = {corner_id}

    # find first row
    p_right = c_right
    for column in range(1, int(len(tiles) ** 0.5)):
        for side_id in sides + corners:
            if side_id in processed:
                continue
            transformed_tile = find_match(tiles[side_id], None, p_right)
            if transformed_tile is not None:
                processed.add(side_id)
                image[0].append(transformed_tile)
                _, p_right, _, _ = get_edges(transformed_tile)
                break

    # find rest
    for row in range(1, int(len(tiles) ** 0.5)):
        # find first
        _, _, t_bottom, _ = get_edges(image[-1][0])
        for side_id in sides + corners:
            if side_id in processed:
                continue
            transformed_tile = find_match(tiles[side_id], t_bottom, None)
            if transformed_tile is not None:
                processed.add(side_id)
                image.append([transformed_tile])
                break

        for column in range(1, int(len(tiles) ** 0.5)):
            _, _, t_bottom, _ = get_edges(image[-2][column])
            _, p_right, _, _ = get_edges(image[-1][column - 1])
            for side_id in tiles.keys():
                if side_id in processed:
                    continue
                transformed_tile = find_match(tiles[side_id], t_bottom, p_right)
                if transformed_tile is not None:
                    processed.add(side_id)
                    image[-1].append(transformed_tile)
                    break

    picture = []

    for tile_row in image:
        sub_image = [''] * len(tile_row[0][1:-1])
        for tile in tile_row:
            for row, row_values in enumerate(tile[1:-1]):
                for column_value in row_values[1:-1]:
                    sub_image[row] += column_value
        picture.extend(sub_image)

    return get_dragon_count(picture)


def get_dragon_count(picture):
    trans_pic = picture
    # v_flip
    for _ in [0, 1]:
        # h_flip
        for _ in [0, 1]:
            # rotation
            for _ in range(0, 4):
                d_count = find_dragons(trans_pic)
                if d_count > 0:
                    return sum([row.count('#') for row in picture]) - d_count * len(dragon_map)

                trans_pic = rotate(trans_pic)

            trans_pic = flip_h(trans_pic)
        trans_pic = flip_v(trans_pic)

    return None


dragon_map = {
    (0,1),
    (1,2),
    (4,2),
    (5,1),
    (6,1),
    (7,2),
    (10,2),
    (11,1),
    (12,1),
    (13,2),
    (16,2),
    (17,1),
    (18,1),
    (18,0),
    (19,1),
}

def find_dragons(picture):
    count = 0
    for x in range(0, len(picture[0]) - 20):
        for y in range(0, len(picture) - 3):
            found = True
            for dif in dragon_map:
                if picture[y + dif[1]][x + dif[0]] != '#':
                    found = False
                    break
            if found:
                count += 1

    return count


print('Part 1: ', reduce(operator.mul, part1()[0]))
print('Part 2: ', part2())
