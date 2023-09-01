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
    def __init__(self, size):
        self.__size = size
