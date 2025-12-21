#!/usr/bin/env python3

import sys

"""
# Run multiple times for 3 different sub-graphs and then multiply totals together*.
I experimented to find the max-depth values. Keep in mind each user's input files differ.

  srv -> fft  (depth: 10)
  fft -> dac  (depth: 18)
  dac -> out  (depth: 11)

*This works because path dac -> out does not contain fft.

TODO: refactor this code to complete the challenge in a single run.
"""

START_NODE = "dac"
END_NODE = "out"
MAX_DEPTH = 11


longest_path_seen = 0
run_counter = 0


# depth-first search aglo
def find_all_paths(graph, start, end, path=None):
    global longest_path_seen
    global run_counter

    if path is None:
        path = ()

    path = path + (start,)

    if start == end:
        if len(path) > longest_path_seen:
            longest_path_seen = len(path)
            print(f"Found new longest path: {longest_path_seen}")
        run_counter += 1
        if run_counter % (10 * 1000) == 0:
            print(f"r:{run_counter}")
        return [path]
    elif start not in graph:
        return []
    elif len(path) == MAX_DEPTH:
        return []

    all_paths = []

    for node in graph[start]:
        if node not in path:  # cycle detection
            new_paths = find_all_paths(graph, node, end, path)
            all_paths.extend(new_paths)

    return all_paths


if __name__ == "__main__":
    input_txt = sys.stdin.read()

    # builds the graph from the input
    """
    graph = {
        'A': ['B', 'C'],
        'B': ['C', 'D'],
        'C': ['D'],
        'D': ['C', 'E'],
        'E': ['F'],
        'F': ['C'],
        'G': [] # Node with no neighbors
    }
    """

    graph = {}

    for line in input_txt.split("\n"):
        if not line:
            continue
        device, output_str = line.split(":")
        outputs = output_str.strip().split(" ")
        graph[device] = outputs

    graph[END_NODE] = []

    paths = find_all_paths(graph, START_NODE, END_NODE)

    print(f"All paths from {START_NODE} to {END_NODE}:")
    for p in paths:
        print(p)

    print("total:", len(paths))
