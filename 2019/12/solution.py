from math import lcm

# lines
lines = [l.strip() for l in open('input') if l]
values = []

for line in lines:
    [x, y, z] = line.split(',')
    x = int(x[x.index('=') + 1:])
    y = int(y[y.index('=') + 1:])
    z = int(z[z.index('=') + 1:-1])

    values.append(((x,y,z), (0,0,0)))


def part1():
    moons = list(values)

    for _ in range(1000):
        new_moons = []
        for moon in moons:
            x, y, z = moon[0]
            xv, yv, zv = moon[1]

            inner_moons = list(moons)
            inner_moons.remove(moon)
            for inner_moon in inner_moons:
                if x < inner_moon[0][0]:
                    xv += 1
                elif x > inner_moon[0][0]:
                    xv -= 1
                if y < inner_moon[0][1]:
                    yv += 1
                elif y > inner_moon[0][1]:
                    yv -= 1
                if z < inner_moon[0][2]:
                    zv += 1
                elif z > inner_moon[0][2]:
                    zv -= 1

            x += xv
            y += yv
            z += zv

            new_moons.append(((x,y,z), (xv,yv,zv)))

        moons = new_moons

    return sum([sum(map(abs, moon[0])) * sum(map(abs, moon[1])) for moon in moons])


def part2():
    moons = list(values)
    prev_x_states = set()
    prev_y_states = set()
    prev_z_states = set()

    x_period = None
    y_period = None
    z_period = None

    while None in [x_period, y_period, z_period]:
        def check_axis(period, index, prev_states):
            if period is not None:
                return period

            current_state = ''.join([f'{moon[0][index]}{moon[1][index]}' for moon in moons])

            if current_state in prev_states:
                return len(prev_states)
            else:
                prev_states.add(current_state)

        x_period = check_axis(x_period, 0, prev_x_states)
        y_period = check_axis(y_period, 1, prev_y_states)
        z_period = check_axis(z_period, 2, prev_z_states)

        new_moons = []
        for moon in moons:
            x, y, z = moon[0]
            xv, yv, zv = moon[1]

            inner_moons = list(moons)
            inner_moons.remove(moon)
            for inner_moon in inner_moons:
                if x < inner_moon[0][0]:
                    xv += 1
                elif x > inner_moon[0][0]:
                    xv -= 1
                if y < inner_moon[0][1]:
                    yv += 1
                elif y > inner_moon[0][1]:
                    yv -= 1
                if z < inner_moon[0][2]:
                    zv += 1
                elif z > inner_moon[0][2]:
                    zv -= 1

            x += xv
            y += yv
            z += zv

            new_moons.append(((x,y,z), (xv,yv,zv)))

        moons = new_moons

    return lcm(x_period, y_period, z_period)


print('Part 1: ', part1())
print('Part 2: ', part2())
