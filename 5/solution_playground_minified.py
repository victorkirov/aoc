ids = set(
    [
        int((bin_str:=l.strip().translate(str.maketrans({'F': '0', 'B': '1', 'L': '0', 'R': '1'})))[0:7], 2) * 8 + int(bin_str[7:], 2)
        for l in open('input') if l
    ]
)

print('Part 1', max(ids))
print('Part 2', next(iter(set(range(min(ids), max(ids))).difference(set(ids)))))
