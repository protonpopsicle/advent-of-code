#!/usr/bin/env python3

import sys

START_NODE = 'you'
END_NODE   = 'out'


# depth-first search aglo
def find_all_paths(graph, start, end, path=None):
    if path is None:
        path = ()

    path = path + (start,)

    if start == end:
        return [path]
    elif start not in graph:
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

    for line in input_txt.split('\n'):
        if not line:
            continue
        device, output_str = line.split(':')
        outputs = output_str.strip().split(' ')
        graph[device] = outputs

    graph[END_NODE] = []

    paths = find_all_paths(graph, START_NODE, END_NODE)

    print(f"All paths from {START_NODE} to {END_NODE}:")
    for p in paths:
        print(p)

    print('total:', len(paths))
