#!/usr/bin/env python3

import itertools
import math
import sys


counter = itertools.count(start=1)
max_connections = 1000

class Circuit:
    def __init__(self, distance=0, coords=[]):
        self.id = next(counter)
        self.distance = distance
        self.coords = coords

    def __str__(self):
        return "{%s} len=%s %s" % (self.id, len(self.coords), self.coords)

def get_circuit(coord):
    for i, c in enumerate(all_circuits):
        if coord in c.coords:
            return i, c

    return None, None

def merge_circuits(c1_i, c2_i):
    c1 = all_circuits[c1_i]
    c2 = all_circuits[c2_i]
    new_c = Circuit(0, list(set(c1.coords + c2.coords)))

    for i in sorted([c1_i, c2_i], reverse=True):
        del all_circuits[i]

    all_circuits.append(new_c)
    return new_c

def compare_all(coords):
    distances = []

    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            d = math.dist(coords[i], coords[j])
            distances.append((d, coords[i], coords[j]))

    return distances

if __name__ == "__main__":
    coords = []
    
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        coord = tuple(int(x) for x in line.split(','))
        coords.append(coord)

    distances = compare_all(coords)

    all_circuits = []
    connections = 0

    for d, coord1, coord2 in sorted(distances):
        if connections == max_connections:
            break

        print('Eval pair:', coord1, coord2, 'distance: %.2f' % d)

        # check for existing circuits containing either of these coordintes
        c1_i, cand1 = get_circuit(coord1)
        c2_i, cand2 = get_circuit(coord2)

        if cand1 is None and cand2 is None:  # 0 existing circuits found
            circuit = Circuit(d, [coord1, coord2])
            all_circuits.append(circuit)
            print('%d:\n  NEW CIRCUIT: {%s} - %s\n' % (connections, circuit.id, circuit.coords))
        elif cand1 and cand2:  # 2 existing circuits found
            if cand1 == cand2:  # they are the same circuit, do nothing
                print('%d:\n  NO OP. both present in circuit: {%s}\n' % (connections, cand1.id))
            else:  # they are different, can be merged into one circuit
                new_c = merge_circuits(c1_i, c2_i)
                print('%d:\n  MERGE CIRCUITS: {%s} + {%s} = {%s} - %s\n' % (connections, cand1.id, cand2.id, new_c.id, new_c.coords))
        else:  # whichever one found should be updated to include the other coord
            if cand1 is not None:
                cand1.coords.append(coord2)
            elif cand2 is not None:
                cand2.coords.append(coord1)
            cand = cand1 if cand1 is not None else cand2
            print('%d:\n  UPDATE CIRCUIT: {%s} - %s\n' % (connections, cand.id, cand.coords))
        
        connections += 1

    print('----------')
    print('End state:\n%s' % '\n'.join([str(c) for c in all_circuits]))

    largest_circuits = sorted(all_circuits, key=lambda c: len(c.coords), reverse=True)[:3]
    print('total: ', math.prod([len(c.coords) for c in largest_circuits]))