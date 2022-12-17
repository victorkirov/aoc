from itertools import cycle

input_file_name = 'input'

lines = [l.strip() for l in open(input_file_name) if l]
cmds = list(lines[0])

# rocks
data = open('rocks').read()
rocks = [v.strip() for v in data.split('\n\n')]
rocks = [v.split('\n') for v in rocks]


def part1():
    mound = []
    hole_width = 7

    rock_wave = cycle(rocks)
    cmd_wave = cycle(cmds)
    rounds = 0

    for rock in rock_wave:
        rounds += 1

        size = len(rock[0])
        pos = 2

        for _ in range(4):
            cmd = next(cmd_wave)
            if cmd == '>':
                pos += 1
            elif cmd == '<':
                pos -= 1

            if pos < 0:
                pos = 0
            elif pos > hole_width - size:
                pos = hole_width - size

        hit = mound == []
        merged_depth = 0
        while not hit and merged_depth < len(mound):
            test_merge = merged_depth + 1

            for i in range(1, min(test_merge, len(rock)) + 1):
                mound_line = mound[-(test_merge - i + 1)]
                rock_line = rock[-i]

                for j in range(pos, pos + size):
                    if mound_line[j] == '#' and rock_line[j - pos] == '#':
                        hit = True
                        break

                if hit:
                    break
            if hit:
                break

            merged_depth += 1

            cmd = next(cmd_wave)
            last_pos = pos
            if cmd == '>':
                pos += 1
            elif cmd == '<':
                pos -= 1

            if pos < 0:
                pos = last_pos
            elif pos > hole_width - size:
                pos = last_pos
            else:
                for i in range(1, min(test_merge, len(rock)) + 1):
                    mound_line = mound[-(test_merge - i + 1)]
                    rock_line = rock[-i]

                    for j in range(pos, pos + size):
                        if mound_line[j] == '#' and rock_line[j - pos] == '#':
                            pos = last_pos
                            break

        for line in reversed(rock):
            if merged_depth > 0:
                for j in range(len(line)):
                    mound_line = mound[-merged_depth]
                    if line[j] == '#':
                        mound[-merged_depth] = mound_line[:j + pos] + '#' + mound_line[j + pos + 1:]
                merged_depth -= 1
            else:
                mound.append('.' * pos + line + '.' * (hole_width - pos - size))

        if rounds == 2022:
            break

    # mound.reverse()
    # for l in mound:
    #     print(l)

    return len(mound)


def part2():
    mound = []
    hole_width = 7

    rock_wave = cycle(rocks)
    cmd_i = 0
    rounds = 0

    processed = {}
    heights = []

    for rock in rock_wave:
        # print(cmd_i, rounds, len(mound))
        start_cmd = cmd_i
        rock_i = rocks.index(rock)

        rounds += 1

        size = len(rock[0])
        pos = 2

        for _ in range(4):
            cmd = cmds[cmd_i]
            cmd_i += 1
            cmd_i %= len(cmds)

            if cmd == '>':
                pos += 1
            elif cmd == '<':
                pos -= 1

            if pos < 0:
                pos = 0
            elif pos > hole_width - size:
                pos = hole_width - size

        hit = mound == []
        merged_depth = 0
        while not hit and merged_depth < len(mound):
            test_merge = merged_depth + 1

            for i in range(1, min(test_merge, len(rock)) + 1):
                mound_line = mound[-(test_merge - i + 1)]
                rock_line = rock[-i]

                for j in range(pos, pos + size):
                    if mound_line[j] == '#' and rock_line[j - pos] == '#':
                        hit = True
                        break

                if hit:
                    break
            if hit:
                break

            merged_depth += 1

            cmd = cmds[cmd_i]
            cmd_i += 1
            cmd_i %= len(cmds)

            last_pos = pos
            if cmd == '>':
                pos += 1
            elif cmd == '<':
                pos -= 1

            if pos < 0:
                pos = last_pos
            elif pos > hole_width - size:
                pos = last_pos
            else:
                for i in range(1, min(test_merge, len(rock)) + 1):
                    mound_line = mound[-(test_merge - i + 1)]
                    rock_line = rock[-i]

                    for j in range(pos, pos + size):
                        if mound_line[j] == '#' and rock_line[j - pos] == '#':
                            pos = last_pos
                            break

        for line in reversed(rock):
            if merged_depth > 0:
                for j in range(len(line)):
                    mound_line = mound[-merged_depth]
                    if line[j] == '#':
                        mound[-merged_depth] = mound_line[:j + pos] + '#' + mound_line[j + pos + 1:]
                merged_depth -= 1
            else:
                new_line = '.' * pos + line + '.' * (hole_width - pos - size)
                mound.append(new_line)

        heights.append(len(mound))
        lookup = (start_cmd, rock_i, pos, merged_depth)

        if lookup in processed:
            repeating_rounds = rounds - processed[lookup]
            repeating_height = heights[-1] - heights[processed[lookup] - 1]

            total_repeating_height = (1000000000000 // repeating_rounds) * repeating_height
            pre_cycle_height = heights[processed[lookup] - 2]

            outstanding_rounds = 1000000000000 - (1000000000000 // repeating_rounds) * repeating_rounds
            make_up_rounds = outstanding_rounds - (processed[lookup] - 1)

            make_up_height = heights[processed[lookup] + make_up_rounds] - heights[processed[lookup]]

            return total_repeating_height + pre_cycle_height + make_up_height

        processed[(start_cmd, rock_i, pos, merged_depth)] = rounds


print('Part 1: ', part1())
print('Part 2: ', part2())
