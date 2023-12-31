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
            __width: Private attribute
            __height: Private attribute
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ getter method for width attribute
        """
        return self.__width

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
        self.__width = value

    @property
    def height(self):
        """ getter method for height attribute
        """
        return (self.__height)

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
        self.__height = value

    def area(self):
        """ Method that returns rectangle area
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """ Method that returns  rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """ Prints the rectangle using the character '#'
        """
        rect_str = ''
        if self.__width == 0 or self.__height == 0:
            return rect_str

        for row in range(self.__height):
            for column in range(self.__width):
                rect_str += f'{self.print_symbol}'
            if row < self.__height - 1:
                rect_str += '\n'
        return rect_str

    def __repr__(self):
        """ Returns string representation of the rectangle
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ Detects instance deletion
        """
        self.__width = None
        self.__height = None
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
