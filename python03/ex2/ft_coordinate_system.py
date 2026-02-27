#!/usr/bin/env python3

import sys
import math


def distance(a: tuple[float, float, float],
             b: tuple[float, float, float]) -> float:
    return (math.sqrt((b[1]-a[1])**2 + (b[2]-a[2])**2 + (b[0]-a[0])**2))


def parse_coordinates(a: str, b: str, c: str) -> tuple[float, float, float]:
    try:
        float_a = float(a)
        float_b = float(b)
        float_c = float(c)
    except (ValueError, TypeError) as e:
        raise ValueError(f"Error parsing coordinates ({a}. {b}, {c}) \n"
                         f"Error type : {e}")
    else:
        return (float_a, float_b, float_c)


def main():
    print("=== Game Coordinate System ===")
    coordinates = []
    for coord in (sys.argv[1:]):
        coordinates.append(coord)
    if (len(coordinates) != 3):
        print("Error, please provide exactly 3 coordinates.")
        return
    print(f"Parsing coordinates : {coordinates}")
    try:
        coord_tuple = parse_coordinates(*coordinates)
    except ValueError as e:
        print(e)
    else:
        print(f"parsed position : {coord_tuple}")
        print(f"distance between 0 and {coord_tuple} :"
              f" {distance((0,0,0), coord_tuple):.2f}")
        print()
        print("Unpacking demonstration")
        (x, y, z) = coord_tuple
        print(f"Player at x = {x}, y = {y}, z = {z}")


if __name__ == "__main__":
    main()
