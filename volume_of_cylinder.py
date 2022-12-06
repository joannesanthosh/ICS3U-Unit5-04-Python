#!/usr/bin/env python3

# Created by: Joanne Santhosh
# Created on: Dec 2022
# This program calculates the volume of a cylinder


import math


def calculate_cylinder_volume(height: int, radius: int) -> float:
    # This function calculates volume

    if height <= 0 or radius <= 0:
        volume = float(-1)
        return volume
    else:
        volume = float(math.pi * (radius * radius) * height)
        return volume


def main():
    # This function gets the volume

    # Input
    height_from_user = input("Enter the height of the cylinder(mm): ")
    radius_from_user = input("Enter the radius of the cylinder(mm): ")

    try:
        height_from_user = float(height_from_user)
        radius_from_user = float(radius_from_user)
        # call functions
        final_volume = calculate_cylinder_volume(height_from_user, radius_from_user)
        if final_volume < 0:
            print("-1")
        else:
            print("The volume of this cylinder is {0} mm³.".format(final_volume))
    except ValueError:
        print("Invalid Input")

    print("\nDone.")


if __name__ == "__main__":
    main()
