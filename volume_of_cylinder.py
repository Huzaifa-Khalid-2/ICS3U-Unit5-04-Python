#!/usr/bin/env python3

# Created by: Huzaifa Khalid
# Created on: March 2022
# This program calculates the volume of aq cylinder

import math


def volume_of_cylinder(radius, height):
    # calculate volume

    volume = math.pi * (radius**2) * height

    return volume


def main():
    # This function gets input

    # input
    radius_as_str = input("Enter the base (m): ")
    height_as_str = input("\nEnter the height (m): ")

    # process

    try:
        radius_as_float = float(radius_as_str)
        height_as_float = float(height_as_str)
        # call functions
        volume = volume_of_cylinder(radius_as_float, height_as_float)
        volume = round(volume, 2)
        print("\nThe volume is {0} m³ ".format(volume))
    except Exception:
        print("\nInavald, input")
    finally:
        print("\nDone")


if __name__ == "__main__":
    main()
