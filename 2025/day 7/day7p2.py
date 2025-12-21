#!/usr/bin/env python3

import sys

SPACE = 0


class TreeNode:
    def __init__(self, value=0):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self, level=0):
        ret = "  " * level + str(self.value) + "\n"
        if self.left is not None:
            ret += self.left.__str__(level + 1)
        if self.right is not None:
            ret += self.right.__str__(level + 1)
        return ret


def split_beam(beam_state, split_at):  # modifies beam state
    parent_node = beam_state[split_at]
    beam_state[split_at] = SPACE

    left = split_at - 1
    right = split_at + 1

    if beam_state[left] == SPACE:
        beam_state[left] = TreeNode()

    parent_node.left = beam_state[left]
    beam_state[left].value += parent_node.value

    if beam_state[right] == SPACE:
        beam_state[right] = TreeNode()

    parent_node.right = beam_state[right]
    beam_state[right].value += parent_node.value


if __name__ == "__main__":
    beam_state = []
    root = TreeNode(1)
    split_count = 0

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        if len(beam_state) == 0:  # init the beam state
            beam_state = [root if c == "S" else SPACE for c in line]

        for i, c in enumerate(line):
            if c == "^" and beam_state[i] != SPACE:
                split_beam(beam_state, i)
                split_count += 1

    print(sum([item.value for item in beam_state if type(item) is TreeNode]))
