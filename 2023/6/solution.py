input_file_name = 'input'

# strings
lines = [l.strip() for l in open(input_file_name) if l]
values = [v for v in lines]

times = [int(t) for t in values[0].split(' ')[1:] if t]
distances = [int(t) for t in values[1].split(' ')[1:] if t]

# parts
def part1():
    result = 1

    for i in range(len(times)):
        time = times[i]
        distance = distances[i]
        current = 0

        for m in range((time + 1) // 2):
            m_dist = m * (time - m)

            if m_dist > distance:
                current += 2

        if time%2 == 0:
            m_dist = (time / 2) ** 2
            if m_dist > distance:
                current += 1

        result *= current

    return result


def part2():
    result = 0

    time_str = ''
    dist_str = ''

    for t in times:
        time_str += str(t)
    for d in distances:
        dist_str += str(d)

    time = int(time_str)
    distance = int(dist_str)

    for m in range((time + 1) // 2):
        m_dist = m * (time - m)

        if m_dist > distance:
            result += 2

    if time%2 == 0:
        m_dist = (time / 2) ** 2
        if m_dist > distance:
            result += 1

    return result


print('Part 1: ', part1())
print('Part 2: ', part2())
