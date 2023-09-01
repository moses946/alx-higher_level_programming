#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        """initializes size as a private attribute"""
        self.__size = size

    def area(self):
        """ Computes the current square area"""
        return (self.__size ** 2)

    @property
    def size(self):
        """getter method to retrieve size attribute"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """setter method to set the value of size attribute"""
        try:
            if int(value) < 0:
                raise ValueError("size must be >= 0")
            self.__size = int(value)
        except TypeError:
            raise TypeError("size must be an integer")
