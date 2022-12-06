#!/usr/bin/env python3

# Created by: Joanne Santhosh
# Created on: Dec 2022
# This program calculates the volume of a cylinder


import math


def calculate_volume(radius: int, height: int) -> None:
    # calculate volume

    # process
    volume = math.pi * (radius * radius) * height

    # output
    print("The volume of the cylinder is {0} cm³".format(volume))


def main():
    # this function gets the base and height

    # input
    radius_from_user = int(input("Enter the radius value of the cylinder (cm): "))
    height_from_user = int(input("Enter the height value of the cylinder (cm): "))
    print("")

    try:
        radius = float(radius_from_user)
        height = float(height_from_user)
        if radius_from_user and height_from_user < 0:
            print("\n-1cm³")
    except ValueError:
        print("\nInvalid Input")
    print("\nDone.")


if __name__ == "__main__":
    main()
