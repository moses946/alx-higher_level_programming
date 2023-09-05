#!/usr/bin/python3
"""Module containing definition of a Rectangle class
"""


class Rectangle:
    """
    A Rectangle class that initializes a rectangle instance and contains
    several methods that operate on the rectangle instance
    """
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
