#!/usr/bin/env python3

import sys


NUM_BATTERIES = 12

def largest_possible_joltage(bank, runs=0):
    _max = (0,0)

    for i, digit_char in enumerate(bank):
        if i > len(bank) - (NUM_BATTERIES - runs):
            break
        digit = int(digit_char)
        if digit > _max[1]:
            _max = (i, digit)
    
    return _max

if __name__ == "__main__":
    total = 0

    for line in sys.stdin:
        bank = line.strip()
        accumulator = ''

        for x in range(NUM_BATTERIES):
            _max = largest_possible_joltage(bank, runs=x)
            bank = bank[_max[0] + 1:]
            accumulator += str(_max[1])

        print('bank:', line.strip(), 'largest:', accumulator)
        total += int(accumulator)

    print('total:', total)
