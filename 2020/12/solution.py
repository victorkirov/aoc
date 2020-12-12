# strings
lines = [l.strip() for l in open('input') if l]
values = [(v[0], int(v[1:])) for v in lines]

# parts
def part1():
    deg = 90
    x = 0
    y = 0

    for value in values:
        ins = value[0]
        amount = value[1]

        def move(dir, distance):
            dir = dir % 360
            move_map = {
                0: (0, distance),
                90: (distance, 0),
                180: (0, -distance),
                270: (-distance, 0),
            }
            return move_map[dir]

        dx = dy = 0

        if ins == 'L':
            deg -= amount
        elif ins == 'R':
            deg += amount
        elif ins == 'N':
            dx, dy = move(0, amount)
        elif ins == 'S':
            dx, dy = move(180, amount)
        elif ins == 'E':
            dx, dy = move(90, amount)
        elif ins == 'W':
            dx, dy = move(270, amount)
        elif ins == 'F':
            dx, dy = move(deg, amount)

        x += dx
        y += dy

    return abs(x) + abs(y)


def part2():
    x = 0
    y = 0
    wx = 10
    wy = 1

    for value in values:
        ins = value[0]
        amount = value[1]

        dwx = dwy = 0
        dx = dy = 0

        def rotate(ox, oy, deg):
            deg = deg % 360

            if deg == 0:
                return ox, oy
            if deg == 90:
                return oy, -ox
            if deg == 180:
                return -ox, -oy
            if deg == 270:
                return -oy, ox
            raise RuntimeError(ox, oy, deg)

        if ins == 'L':
            wx, wy = rotate(wx, wy, -amount)
        elif ins == 'R':
            wx, wy = rotate(wx, wy, amount)
        elif ins == 'N':
            dwy = amount
        elif ins == 'S':
            dwy = -amount
        elif ins == 'E':
            dwx = amount
        elif ins == 'W':
            dwx = -amount
        elif ins == 'F':
            dx, dy = (amount * wx, amount * wy)

        wx += dwx
        wy += dwy

        x += dx
        y += dy

    return abs(x) + abs(y)


print('Part 1: ', part1())
print('Part 2: ', part2())
