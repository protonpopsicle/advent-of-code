#!/usr/bin/env python3

import sys


def calculate_rectangle_area(corner1, corner2):
    x1, y1 = corner1
    x2, y2 = corner2

    width = abs(x2 - x1) + 1
    height = abs(y2 - y1) + 1
    return width * height


def compare_all(coords):
    areas = []

    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            rect_area = calculate_rectangle_area(coords[i], coords[j])
            areas.append((rect_area, coords[i], coords[j]))

    return areas


if __name__ == "__main__":
    coords = []

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        coord = tuple(int(x) for x in line.split(","))
        coords.append(coord)

    areas = compare_all(coords)
    print("largest area:", sorted(areas, reverse=True)[0][0])
