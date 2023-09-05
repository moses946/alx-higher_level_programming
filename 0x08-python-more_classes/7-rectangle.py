#!/usr/bin/python3
"""Module containing definition of a Rectangle class
"""


class Rectangle:
    """
    A Rectangle class that initializes a rectangle instance and contains
    several methods that operate on the rectangle instance
    """

    number_of_instances = 0  # attribute containing number of instances created

    print_symbol = '#'  # attribute containing symbol for string representation

    def __init__(self, width=0, height=0):
        """ Instantiation of Rectangle class
        Args:
            width: (int) width of rectangle
            height: (int) height of rectangle
        Attributes:
            width: Private attribute
            height: Private attribute
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ getter method for width attribute
        """
        return self.width

    @width.setter
    def width(self, value):
        """ setter method for width attribute
        Args:
            value: (int) rectangle width to be set
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.width = value

    @property
    def height(self):
        """ getter method for height attribute
        """
        return (self.height)

    @height.setter
    def height(self, value):
        """ setter method for height attribute
        Args:
            value: (int) rectangle height to be set
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.height = value

    def area(self):
        """ Method that returns rectangle area
        """
        return (self.width * self.height)

    def perimeter(self):
        """ Method that returns  rectangle perimeter
        """
        if self.width == 0 or self.height == 0:
            return (0)
        return ((self.width + self.height) * 2)

    def __str__(self):
        """ Prints the rectangle using the character '#'
        """
        rect_str = ''
        if self.width == 0 or self.height == 0:
            return rect_str

        for row in range(self.height):
            for column in range(self.width):
                rect_str += f'{self.print_symbol}'
            if row < self.height - 1:
                rect_str += '\n'
        return rect_str

    def __repr__(self):
        """ Returns string representation of the rectangle
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """ Detects instance deletion
        """
        self.width = None
        self.height = None
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Returns the bigger rectangle based on area
        Args:
            rect_1: (Rectangle) rectangle instance
            rect_2: (Rectangle) rectangle instance
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area() or rect_1.area() == rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ Class method that returns a new rectangle
        Args:
            size: (int) width and height of rectangle
        """
        return (cls(size, size))
