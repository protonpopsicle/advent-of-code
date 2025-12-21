#!/usr/bin/env python3

import sys


def split_beam(beam_state, split_at):  # modifies beam state
    beam_state[split_at] = 0
    beam_state[split_at - 1] = 1
    beam_state[split_at + 1] = 1


if __name__ == "__main__":
    beam_state = []
    split_count = 0

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        if len(beam_state) == 0:  # init the beam state
            beam_state = [1 if c == "S" else 0 for c in line]

        for i, c in enumerate(line):
            if c == "^" and beam_state[i] == 1:
                split_beam(beam_state, i)
                split_count += 1

    print("split count:", split_count)
