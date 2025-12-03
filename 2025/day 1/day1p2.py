#!/usr/bin/env python3


ticks = tuple(range(100))
current_tick = 50
password = 0

def move_dial(num_ticks):
    global current_tick
    current_tick = (current_tick + num_ticks) % len(ticks)

if __name__ == "__main__":
    with open('input.txt') as f:
        for line in f:
            rotation = line.strip()
            direction = rotation[0]
            value = int(rotation[1:])
            if direction == 'L':
                value = -value  # negate

            passes_zero = 0
            if current_tick != 0:
                if direction == 'L' and (current_tick + value) < 0:
                    passes_zero += 1

            passes_zero += abs(current_tick + value) // len(ticks)

            move_dial(value)
            if passes_zero > 0:
                password += passes_zero
            elif current_tick == 0:
                password += 1

    print('password:', password)
