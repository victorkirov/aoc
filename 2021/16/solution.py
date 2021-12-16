from functools import reduce
from collections import defaultdict
from itertools import product, combinations, permutations
from typing import List, Tuple


# ints
data = [l.strip() for l in open('input') if l]
values = list(data[0])


def hex_to_bin(hex):
    return bin(int(hex, base=16))[2:].zfill(4)


binary = ''.join(hex_to_bin(v) for v in values)


def get_version_sum(
    bin_lst: List[str],
) -> int:
    result = 0

    while len(bin_lst) > 0:
        version = int(''.join(bin_lst[:3]), 2)
        bin_lst = bin_lst[3:]
        type = int(''.join(bin_lst[:3]), 2)
        bin_lst = bin_lst[3:]

        if type == 4:
            while 1:
                chunk = bin_lst[:5]
                bin_lst = bin_lst[5:]

                if chunk[0] == '0':
                    break
        else:
            length_type_id = int(bin_lst[0])
            bin_lst = bin_lst[1:]

            if length_type_id == 0:
                sub_packet_size = int(''.join(bin_lst[:15]), 2)
                bin_lst = bin_lst[15:]
                result += get_version_sum(bin_lst[:sub_packet_size])
                bin_lst = bin_lst[sub_packet_size:]
            else:
                sub_packet_count = int(''.join(bin_lst[:11]), 2)
                bin_lst = bin_lst[11:]

        result += version

        if '1' not in bin_lst:
            break

    return result

# parts
def part1():
    bin_lst = list(binary)

    return get_version_sum(bin_lst)


def process(
    bin_lst: List[str],
) -> Tuple[int, List[str]]:
    version = int(''.join(bin_lst[:3]), 2)
    bin_lst = bin_lst[3:]
    op_type = int(''.join(bin_lst[:3]), 2)
    bin_lst = bin_lst[3:]

    if op_type == 4:
        chunks = []
        while 1:
            chunk = bin_lst[:5]
            bin_lst = bin_lst[5:]
            chunks += chunk[1:]

            if chunk[0] == '0':
                return int(''.join(chunks), 2), bin_lst

    # else Operator
    length_type_id = int(bin_lst[0])
    bin_lst = bin_lst[1:]

    numbers = []

    if length_type_id == 0:
        sub_packet_size = int(''.join(bin_lst[:15]), 2)
        bin_lst = bin_lst[15:]

        sub_packet = bin_lst[:sub_packet_size]
        bin_lst = bin_lst[sub_packet_size:]

        while len(sub_packet) > 0:
            number, sub_packet = process(sub_packet)
            numbers.append(number)
    else:
        sub_packet_count = int(''.join(bin_lst[:11]), 2)
        bin_lst = bin_lst[11:]

        for _ in range(sub_packet_count):
            number, bin_lst = process(bin_lst)
            numbers.append(number)

    if op_type == 0:
        return sum(numbers), bin_lst
    if op_type == 1:
        return reduce(lambda a,b: a*b, numbers), bin_lst
    if op_type == 2:
        return min(numbers), bin_lst
    if op_type == 3:
        return max(numbers), bin_lst
    if op_type == 5:
        return 1 if numbers[0] > numbers[1] else 0, bin_lst
    if op_type == 6:
        return 1 if numbers[0] < numbers[1] else 0, bin_lst
    if op_type == 7:
        return 1 if numbers[0] == numbers[1] else 0, bin_lst


def part2():
    bin_lst = list(binary)

    return process(bin_lst)[0]


print('Part 1: ', part1())
print('Part 2: ', part2())
