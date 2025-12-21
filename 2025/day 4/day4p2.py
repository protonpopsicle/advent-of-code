#!/usr/bin/env python3

import sys

BLANK = "."
PAPER_ROLL = "@"
GRAVE = "X"


def adjacent_indices(x, y):
    return (
        (x - 1, y),
        (x + 1, y),
        (x, y - 1),
        (x, y + 1),  # edges
        (x - 1, y - 1),
        (x - 1, y + 1),
        (x + 1, y - 1),
        (x + 1, y + 1),  # diagonals
    )


def calc_total(matrix):
    impacted_coords = []

    for x, row in enumerate(matrix):
        if x == 0 or x == len(matrix) - 1:
            continue

        for y, symbol in enumerate(row):
            if y == 0 or y == len(row) - 1 or symbol != PAPER_ROLL:
                continue

            adjacent_symbols = [matrix[x2][y2] for x2, y2 in adjacent_indices(x, y)]
            if adjacent_symbols.count(PAPER_ROLL) < 4:
                impacted_coords.append((x, y))

            print(matrix[x][y], adjacent_symbols)

    return impacted_coords


if __name__ == "__main__":
    file_content = sys.stdin.read()
    total = 0

    # build matrix
    matrix = []
    empty_row = []

    for raw_line in file_content.split():
        line = raw_line.strip()

        if len(matrix) == 0:
            empty_row = [BLANK for _ in range(len(line) + 2)]
            matrix.append(empty_row)
        matrix.append([BLANK, *line.strip(), BLANK])

    matrix.append(empty_row)

    while True:
        impacted_coords = calc_total(matrix)
        count = len(impacted_coords)
        print("count:", count)
        if count > 0:
            total += count
            for x, y in impacted_coords:
                matrix[x][y] = GRAVE
        else:
            break

    print("total:", total)
