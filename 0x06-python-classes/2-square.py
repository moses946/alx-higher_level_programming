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
        """
            Initializes size as a private attribute

            Raises:
                TypeError: If size is not an integer
                ValueError: If size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
