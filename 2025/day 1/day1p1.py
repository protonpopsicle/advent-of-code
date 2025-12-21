#!/usr/bin/env python3

import sys

ticks = tuple(range(100))
current_tick = 50
password = 0


def move_dial(num_ticks):
    global current_tick
    current_tick = (current_tick + num_ticks) % len(ticks)


if __name__ == "__main__":
    for line in sys.stdin:
        rotation = line.strip()
        direction = rotation[0]
        value = int(rotation[1:])
        if direction == "L":
            value = -value  # negate

        move_dial(value)
        if current_tick == 0:
            password += 1

    print("password:", password)
