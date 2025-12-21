#!/usr/bin/env python3

import sys


def is_fresh(id, id_ranges):
    for _min, _max in id_ranges:
        if id >= _min and id <= _max:
            return True

    return False


if __name__ == "__main__":
    input_txt = sys.stdin.read()

    id_ranges = []
    ids = []
    total_fresh = 0

    ranges_txt, ids_txt = input_txt.split("\n\n")

    for line in ranges_txt.split():
        _min, _max = line.strip().split("-")
        id_ranges.append((int(_min), int(_max)))

    for line in ids_txt.split():
        ids.append(int(line.strip()))

    for id in ids:
        fresh = is_fresh(id, id_ranges)
        if fresh:
            total_fresh += 1

    print("fresh count:", total_fresh)
