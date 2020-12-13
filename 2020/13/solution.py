from math import lcm

# strings
with open('input') as f:
    min_wait = int(f.readline())
    values = [v.strip() for v in f.readline().split(',') if v]

# parts
def part1():
    diff = None
    best = None

    for value in values:
        try:
            value = int(value)
            mod = value - (min_wait % value)

            if diff is None or mod < diff:
                diff = mod
                best = value
        except:
            pass

    return (best - (min_wait % best)) * best


def part2():
    required_departures = []

    for index, value in enumerate(values):
        try:
            value = int(value)
            required_departures.append((value, index))
        except:
            pass

    mins = 0
    repeat = 1
    while required_departures:
        bus, diff = required_departures.pop(0)

        runs = 0
        while ((mins + repeat * runs) + diff) % bus != 0:
            runs += 1

        mins = mins + runs * repeat

        repeat = lcm(repeat, bus)

    return mins


print('Part 1: ', part1())
print('Part 2: ', part2())
