#!/usr/bin/env python3

import math
import sys


OPERATORS = ('*', '+')

def parse_symbol(symbol):
    symbol = symbol.strip()
    if symbol not in OPERATORS:
        symbol = int(symbol)
    return symbol

def parse_columns(rows):
    col_widths = []

    count = 0
    for i, char in enumerate(rows[-1]):  # determine the column widths
        if i > 0 and char in OPERATORS:  # reset count
            col_widths.append(count)
            count = 0

        count += 1
    
    col_widths.append(count)

    cols = [[] for _ in col_widths]

    cursor = 0
    for i, width in enumerate(col_widths):  # for column
        for j, row in enumerate(rows):
            cols[i].append(parse_symbol(rows[j][cursor:cursor + width]))
        cursor += width

    return cols

if __name__ == "__main__":
    input_txt = sys.stdin.read()

    total = 0

    rows = [s for s in input_txt.split('\n') if s.strip()]
    cols = parse_columns(rows)

    # perform operations
    for col in cols:
        op = col.pop()
        if op == '*':
            answer = math.prod(col)
        elif op == '+':
            answer = sum(col)

        total += answer

    print('total:', total)
