#!/usr/bin/python3
"""
    This module demonstrates implementation of a class square
"""


class Square:
    """
        Defines a square with private attribute size
        Args:
            size (int): Integer representing the length/width of the square
        Attributes:
            __size (int): Private attribute containing the square dimensions
    """
    def __init__(self, size=0):
        """initializes size as a private attribute"""
        self.__size = size
        self.size(size)

    @property
    def size(self):
        """getter method to retrieve size attribute"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
            Computes the current square area

            Returns:
                int: Area of the squares
        """
        return (self.__size ** 2)
