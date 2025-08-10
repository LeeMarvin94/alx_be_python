# polymorphism_demo.py

import math


class Shape:
    """Base Shape with an interface for area calculation."""

    def area(self):
        """Compute the area of the shape.

        Subclasses must override this method.
        """
        raise NotImplementedError("Subclasses must implement area().")


class Rectangle(Shape):
    """Rectangle defined by length and width."""

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Area = length × width."""
        return self.length * self.width


class Circle(Shape):
    """Circle defined by its radius."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Area = π × r²."""
        return math.pi * (self.radius ** 2)

