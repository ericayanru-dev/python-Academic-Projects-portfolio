"""
Author: Eric Ayanru
Course: CSE110
Project: Area Calculator for Multiple Shapes

Description:
This program allows users to calculate the area of different shapes—square, rectangle, circle,
and also computes square, circle, cube volume, and sphere volume using a single input value.
"""

import math

# Conversion constant from cm² to m²
CM_TO_M2 = 1 / 10_000

def square_area():
    length = float(input("Enter the length of the square (cm): "))
    area_cm2 = length ** 2
    area_m2 = area_cm2 * CM_TO_M2
    print(f"Area of the square: {area_cm2:.2f} cm²")
    print(f"Area of the square: {area_m2:.4f} m²\n")

def rectangle_area():
    length = float(input("Enter the length of the rectangle (cm): "))
    width = float(input("Enter the width of the rectangle (cm): "))
    area_cm2 = length * width
    area_m2 = area_cm2 * CM_TO_M2
    print(f"Area of the rectangle: {area_cm2:.2f} cm²")
    print(f"Area of the rectangle: {area_m2:.4f} m²\n")

def circle_area():
    radius = float(input("Enter the radius of the circle (cm): "))
    area_cm2 = math.pi * radius ** 2
    area_m2 = area_cm2 * CM_TO_M2
    print(f"Area of the circle: {area_cm2:.2f} cm²")
    print(f"Area of the circle: {area_m2:.4f} m²\n")

def multiple_shapes():
    print("\nCalculate the area or volume of multiple shapes using one value.\n")
    value = float(input("Enter a single length value (cm): "))

    area_square = value ** 2
    area_circle = math.pi * value ** 2
    volume_cube = value ** 3
    volume_sphere = (4/3) * math.pi * value ** 3

    print("\nResults based on the value entered:")
    print(f"Square Area: {area_square:.2f} cm²")
    print(f"Circle Area: {area_circle:.2f} cm²")
    print(f"Cube Volume: {volume_cube:.2f} cm³")
    print(f"Sphere Volume: {volume_sphere:.2f} cm³\n")

def main():
    while True:
        print("Choose a shape to calculate:")
        print("1. Square")
        print("2. Rectangle")
        print("3. Circle")
        print("4. Multiple Shapes")
        print("5. Exit")

        try:
            choice = int(input("Pick a number (1–5): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 5.\n")
            continue

        if choice == 1:
            square_area()
        elif choice == 2:
            rectangle_area()
        elif choice == 3:
            circle_area()
        elif choice == 4:
            multiple_shapes()
        elif choice == 5:
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.\n")

if __name__ == "__main__":
    main()