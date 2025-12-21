#!/usr/bin/env python3

import sys

BLANK = "."
PAPER_ROLL = "@"


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


if __name__ == "__main__":
    file_content = sys.stdin.read()
    total = 0

    # build matrix
    matrix = []
    empty_row = ()

    for raw_line in file_content.split():
        line = raw_line.strip()

        if len(matrix) == 0:
            empty_row = tuple([BLANK for _ in range(len(line) + 2)])
            matrix.append(empty_row)
        matrix.append((BLANK, *line.strip(), BLANK))

    matrix.append(empty_row)

    # calc total
    for x, row in enumerate(matrix):
        if x == 0 or x == len(matrix) - 1:
            continue

        for y, symbol in enumerate(row):
            if y == 0 or y == len(row) - 1 or symbol == BLANK:
                continue

            adjacent_symbols = [matrix[x2][y2] for x2, y2 in adjacent_indices(x, y)]
            if adjacent_symbols.count(PAPER_ROLL) < 4:
                total += 1
                symbol = "X"

            print(symbol, adjacent_symbols)

    print("total:", total)
