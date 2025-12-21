#!/usr/bin/env python3

"""
This puzzle was the one that stumped me in 2025. I could not figure out.

The code here was informed by the following resources:
- https://aoc.winslowjosiah.com/solutions/2025/day/10/
- https://www.reddit.com/r/adventofcode/comments/1pk87hl/2025_day_10_part_2_bifurcate_your_way_to_victory/

TODO: Rewrite this solution in a style thats more my own.
"""

import sys
from itertools import combinations

OFF = "."
ON = "#"


class Machine:
    def __init__(self, indicator_diagram, buttons, joltage_requirements):
        self.indicator_diagram = indicator_diagram
        self.indicator_lights = [OFF for _ in indicator_diagram]
        self.buttons = buttons
        self.joltage_requirements = joltage_requirements


def mash_buttons(m):
    # Precompute patterns mapping indicator patterns -> presses.
    patterns = {}
    for num_presses in range(len(m.buttons) + 1):
        for presses in combinations(m.buttons, num_presses):
            pattern = set()
            for button in presses:
                pattern ^= set(button)
            key = tuple(sorted(pattern))
            if key not in patterns:
                patterns[key] = []
            patterns[key].append(presses)
    return patterns


def solve_machine(m):
    valid_combos = mash_buttons(m)
    joltage_result = configure_joltages(m.joltage_requirements, valid_combos)
    assert joltage_result is not None
    return joltage_result


def configure_joltages(joltages, patterns):
    # Copied from: https://aoc.winslowjosiah.com/solutions/2025/day/10/
    def get_min_presses(target):
        # No button presses are needed to reach zero joltage
        if not any(target):
            return 0

        # We must turn on the indicators with odd joltage levels
        indicators = tuple(
            sorted(i for i, joltage in enumerate(target) if joltage % 2 == 1)
        )
        result = None
        for presses in patterns.get(indicators, []):
            # Simulate button presses to reach indicator state
            target_after = list(target)
            for button in presses:
                for joltage_index in button:
                    target_after[joltage_index] -= 1
            # Skip if any levels become negative
            if any(joltage < 0 for joltage in target_after):
                continue

            # All new target levels are even; calculate min presses to
            # reach half the target levels
            half_target = tuple(joltage // 2 for joltage in target_after)
            num_half_target_presses = get_min_presses(half_target)
            if num_half_target_presses is None:
                continue
            # We can reach the target by reaching the half-target twice;
            # add twice the half-target presses to the initial ones
            num_presses = len(presses) + 2 * num_half_target_presses

            # Update minimum presses count
            if result is None:
                result = num_presses
            else:
                result = min(result, num_presses)

        return result

    return get_min_presses(tuple(joltages))


if __name__ == "__main__":
    push_count = 0

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        m_line = line.split(" ")

        m_line.pop(0)
        joltage_requirements_str = m_line.pop()
        button_wiring_schematics = m_line

        buttons = tuple(
            [
                tuple(int(x) for x in s.strip("(").strip(")").split(","))
                for s in button_wiring_schematics
            ]
        )

        joltage_requirements = tuple(
            [int(x) for x in joltage_requirements_str[1:-1].split(",")]
        )
        indicator_diagram = "".join(
            [OFF if x % 2 == 0 else ON for x in joltage_requirements]
        )

        m = Machine(indicator_diagram, buttons, joltage_requirements)
        num_joltage_presses = solve_machine(m)
        print("line:", line, "\n  num_joltage_presses", num_joltage_presses)
        push_count += num_joltage_presses

    print("total push count:", push_count)
