#!/usr/bin/env python3

import sys
from itertools import combinations

OFF = '.'
ON  = '#'


class Machine:
    def __init__(self, indicator_diagram, buttons, joltage_requirements):
        self.indicator_diagram = indicator_diagram
        self.indicator_lights = [OFF for c in indicator_diagram]
        self.buttons = buttons
        self.joltage_requirements = joltage_requirements

    def reset(self):
        self.indicator_lights = [OFF for c in indicator_diagram]

    def configured_correctly(self):
        return ''.join(self.indicator_lights) == self.indicator_diagram

    def push_button(self, button):
        assert(button in self.buttons)
        # toggle each indicator light
        for x in button:
            self.indicator_lights[x] = ON if self.indicator_lights[x] == OFF else OFF

def mash_buttons(machine):
    def try_candidates(candidates):
        for button in candidates:
            machine.push_button(button)
        if machine.configured_correctly():
            print('answer =', candidates)
            return True
        machine.reset()
        return False

    for i in range(100):
        all_combos = list(combinations(machine.buttons, i+1))
        for combo in all_combos:
            print('trying combo:', combo)
            if try_candidates(combo):
                return i+1

    return 0

if __name__ == "__main__":
    machines = []
    push_count = 0

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        m_line = line.split(' ')

        indicator_diagram = m_line.pop(0)[1:-1]
        joltage_requirements_str = m_line.pop()
        button_wiring_schematics = m_line

        buttons = tuple([tuple(int(x) for x in s.strip('(').strip(')').split(',')) \
        for s in button_wiring_schematics])

        joltage_requirements = tuple([int(x) for x in joltage_requirements_str[1:-1].split(',')])

        m = Machine(indicator_diagram, buttons, joltage_requirements)
        machines.append(m)
        push_count += mash_buttons(m)

    print('push count:', push_count)
