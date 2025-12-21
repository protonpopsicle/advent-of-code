#!/usr/bin/env python3

import sys

total = 0


def largest_possible_joltage(bank):
    largest = 0
    for i, bat1 in enumerate(bank):
        for bat2 in bank[i + 1 :]:
            candidate = int(bat1 + bat2)
            if candidate > largest:
                largest = candidate
    return largest


if __name__ == "__main__":
    for line in sys.stdin:
        largest = largest_possible_joltage(line.strip())
        print("bank:", line.strip(), "largest:", largest)
        total += largest

    print("total:", total)
