#!/usr/bin/env python3

import sys


def collapse_ranges(id_ranges):
    id_ranges = sorted(id_ranges)
    indexes_to_purge = []
    new_ranges = []

    for i, r2 in enumerate(id_ranges):
        if i > 0:
            r1 = id_ranges[i-1]
            if not r2[0] > r1[1]:  # overlapping
                new_r = min(r1[0], r2[0]), max(r1[1], r2[1])
                new_ranges.append(new_r)
                indexes_to_purge += [i, i-1]

    new_ranges += [
        r for index, r in enumerate(id_ranges)
        if index not in indexes_to_purge
    ]

    return new_ranges, len(indexes_to_purge) > 0

if __name__ == "__main__":
    input_txt = sys.stdin.read()

    id_ranges = []
    total_fresh = 0

    ranges_txt = input_txt.split('\n\n')[0]

    for line in ranges_txt.split():
        _min, _max = line.strip().split('-')
        id_ranges.append((int(_min), int(_max)))

    changed = True
    while changed:
        id_ranges, changed = collapse_ranges(id_ranges)

    counter = 0
    for start,end in id_ranges:
        counter += 1 + (end - start)

    print('fresh count:', counter)
