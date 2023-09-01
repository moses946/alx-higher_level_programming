#!/usr/bin/python3
"""
    This module demonstrates implementation of a class square
"""


class Square:
    """
        Defines a square with private attribute size
        Args:
            size (int): Integer representing the length/width of the square
            position (tuple): Tuple representing coordinates of the square
        Attributes:
            __size (int): Private attribute containing the square dimensions
            __position (tuple): Private attribute containing square coordinates
    """
    def __init__(self, size=0, position=(0, 0)):
        """initializes size and position using setter methods"""
        self.size(size)
        self.position(position)

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

    @property
    def position(self):
        """getter method to retrieve position attribute"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """
            Computes the current square area

            Returns:
                int: Area of the squares
        """
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square using '#' and spaces using '_'"""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.size):
            print(" " * self.__position[0] + "#" * self.__size)
