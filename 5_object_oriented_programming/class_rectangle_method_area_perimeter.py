# Create a class to represent a rectangle and implement methods to calculate
# area and perimeter
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

rect = Rectangle(5, 3)
print(f"Area: {rect.area()}, Perimeter: {rect.perimeter()}")
