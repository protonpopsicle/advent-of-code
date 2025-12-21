#!/usr/bin/env python3

import sys

HORIZONTAL = "H"
VERTICAL = "V"

"""
Do any of the lines of the boundary path go inside the square?
returns True or False
"""


def path_crosses_rect(path, corners):
    min_x = min(corners, key=lambda p: p[0])[0]
    min_y = min(corners, key=lambda p: p[1])[1]
    max_x = max(corners, key=lambda p: p[0])[0]
    max_y = max(corners, key=lambda p: p[1])[1]

    for i, point in enumerate(path):
        point2 = path[(i + 1) % len(path)]  # last point connects to the first point
        x1, y1 = point
        x2, y2 = point2

        orientation = VERTICAL if x1 == x2 else HORIZONTAL
        # print(orientation, ':', point, "---", point2)

        # eliminate lines that are fully outside the rect
        if orientation == VERTICAL:
            # cond 1: stable value (x) is less than min_x OR greater than max_x
            if x1 <= min_x or x1 >= max_x:
                continue
            # cond 2: y1 and y2 are both less than min_y OR y1 and y2 are both greater than max_y
            if (y1 <= min_y and y2 <= min_y) or (y1 >= max_y and y2 >= max_y):
                continue
        elif orientation == HORIZONTAL:
            # cond 1: stable value (y) is less than min_y OR greater than max_y
            if y1 <= min_y or y1 >= max_y:
                continue
            # cond 2: x1 and x2 are both less than min_x OR x1 and x2 are both greater than max_x
            if (x1 <= min_x and x2 <= min_x) or (x1 >= max_y and x2 >= max_x):
                continue

        print("%s: %s--%s intersects rect: %s" % (orientation, point, point2, corners))
        return True

    return False


def rect_in_bounds(corner1, corner2, edge_path):
    x1, y1 = corner1
    x2, y2 = corner2
    corner3 = (x1, y2)
    corner4 = (x2, y1)
    corners = (corner1, corner2, corner3, corner4)
    return not path_crosses_rect(edge_path, corners)


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
    red_tiles = []

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        tile = tuple(int(x) for x in line.split(","))
        red_tiles.append(tile)

    areas = compare_all(red_tiles)
    print(red_tiles)

    largest_area = None

    # filter areas
    for entry in sorted(areas, reverse=True):
        print("checking rect candidate...", entry)
        area, c1, c2 = entry
        if rect_in_bounds(c1, c2, red_tiles):
            largest_area = area
            break

    print("largest area:", largest_area)
