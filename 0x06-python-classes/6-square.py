#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        """initializes size as a private attribute"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """getter method to retrieve position attribute"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """setter method to set the value of position attribute"""
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """ Computes the current square area"""
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square using '#' and spaces using '_'"""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.size):
            print(" " + self.__position[0] + "#" * self.__size)
