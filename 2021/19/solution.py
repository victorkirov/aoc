from functools import reduce
from collections import defaultdict
from itertools import product, combinations, permutations
from typing import Generator, List, Set, Tuple

# groups
data = open('input').read()
values = [v.strip() for v in data.split('\n\n')]
values = [
    {
        (int(row.split(',')[0]), int(row.split(',')[1]), int(row.split(',')[2]))
        for row in v.split('\n')[1:]
    }
    for v in values
]


def get_orientations(
    scan: Set[Tuple[int, int, int]]
) -> Generator[Set[Tuple[int, int, int]], None, Set[Tuple[int, int, int]]]:
    for dummy in [
        set(scan),  # assuming we are facing z
        {(z, x, y) for (x, y, z) in set(scan)},  # assuming we are facing y
        {(y, z, x) for (x, y, z) in set(scan)}  # assuming we are facing x
    ]:
        for _ in range(2):
            for _ in range(4):
                yield dummy
                dummy = {(y, -x, z) for (x, y, z) in dummy}
            dummy = {(y, x, -z) for (x, y, z) in dummy}

    return dummy


def shift_scan(
    scan: Set[Tuple[int, int, int]],
    dx: int,
    dy: int,
    dz: int
) -> Set[Tuple[int, int, int]]:
    return {
        (x + dx, y + dy, z + dz)
        for (x, y, z)
        in scan
    }


# parts
def get_scan_details() -> Tuple[Set[Tuple[int, int, int]], List[Tuple[int, int, int]]]:
    points = values[0]
    new_points = points

    scanners = [(0, 0, 0)]

    unmatched_scanners = values[1:]

    while len(unmatched_scanners) > 0:
        match_found = False
        for scanner in unmatched_scanners:
            for orientated_scanner in get_orientations(scanner):
                for (px, py, pz) in new_points:
                    for (sx, sy, sz) in orientated_scanner:
                        dx = px - sx
                        dy = py - sy
                        dz = pz - sz
                        shifted_scan = shift_scan(orientated_scanner, dx, dy, dz)

                        if len(shifted_scan.intersection(new_points)) >= 12:
                            points = points | shifted_scan
                            new_points = (points & shifted_scan) | shifted_scan

                            scanners.append((dx, dy, dz))
                            break
                    else:
                        continue
                    break
                else:
                    continue
                break
            else:
                continue
            match_found = True
            break

        if match_found:
            unmatched_scanners.remove(scanner)
            print(f'{len(unmatched_scanners)} left')
        else:
            print("Couldn't find match in new points, checking all")
            new_points = points

    return points, scanners


def get_largest_distance(scanners: List[Tuple[int, int, int]]) -> int:
    max_distance = 0

    for scanner in scanners:
        for other_scanner in scanners:
            if scanner == other_scanner:
                continue
            (x1, y1, z1) = scanner
            (x2, y2, z2) = other_scanner
            distance = abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)
            max_distance = max([distance, max_distance])

    return max_distance


points, scanners = get_scan_details()

print('Part 1: ', len(points))
print('Part 2: ', get_largest_distance(scanners))
