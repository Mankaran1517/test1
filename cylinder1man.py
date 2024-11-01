"""Volume and area of cylinder, with exceptions.
This is the starter version, without exceptions.
The functions return a negative value if the height is negative.

TPRG 2131 Fall 202x Test 1
"""
# Mankaran Singh Chattha
# 100944566
# TPRG2131 Fall test 1
from math import pi

# three-dimensional shape consisting of two parallel circular bases, joined by a curved surface.
# Volume formula: V = π * r^2 * h
def volume_cylinder(diameter, height):
    """Volume of a cylinder given diameter and height."""
    if height < 0:
        raise ValueError("Height must be a positive value.")
    return pi * (diameter / 2.0)**2 * height

# Surface area formula: A = 2πr(h + r)
def area_cylinder(diameter, height):
    """Surface area of a cylinder given diameter and height."""
    if height < 0:
        raise ValueError("Height must be a positive value.")
    radius = diameter / 2.0
    return 2.0 * pi * radius * (height + radius)  # simplified

if __name__ == "__main__":
    while True:
        dia = float(input("\nDiameter? "))
        high = float(input("Height? "))
 
 # so nmow in thyis new program when You will fill negative height it will not give you anything
        if high < 0:
            print("Error: Height must be a positive value.")
            continue  # Ask for input again if height is negative
        
        print("The volume is", volume_cylinder(dia, high))
        print("The area is", area_cylinder(dia, high))