import math


def area_of_circle(radius):
    return math.pi * radius * radius

radius = float(input("Enter the radius: "))
print("Area of circle:", area_of_circle(radius))
