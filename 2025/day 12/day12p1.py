#!/usr/bin/env python3
import re
import sys


w_x_h_pattern = re.compile(r'^(\d+)x(\d+)')
shapes = []
regions = []

def print_shapes():
    for i, shape in enumerate(shapes):
        print(f'{i}:')
        for row in shape['matrix']:
            print(''.join(['#' if x == 1 else '.' for x in row]))
        print()

def place_presents(region):
    print(f'placing presents in region: {region}')
    presents_area = 0
    for i, q in enumerate(region['quantities']):
        presents_area += shapes[i]['area'] * q
    if presents_area <= region['width'] * region['height']:
        print('  the presents fit')
        return True
    print('  the presents do not fit')    
    return False

if __name__ == "__main__":
    area_accumulator = 0
    row_buf = []

    for line in sys.stdin:
        if line[0] in ('.', '#'):
            row = tuple(1 if c == '#' else 0 for c in line.strip())
            row_buf.append(row)
            area_accumulator += sum(row)
        elif line == '\n':
            shapes.append({
                'area': area_accumulator,
                'matrix': tuple(row_buf)
            })
            row_buf.clear()
            area_accumulator = 0
        else: 
            match = re.match(w_x_h_pattern, line)
            if match:
                regions.append({
                    'width': int(match.group(1)),
                    'height': int(match.group(2)),
                    'quantities': tuple(int(c) for c in line.split(' ')[1:])
                })
            
    print_shapes()
    total_fit = 0
    for region in regions:
        if place_presents(region):
            total_fit += 1

    print(f'total fit: {total_fit}')