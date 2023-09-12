#!/usr/bin/python3
""" Module containing BaseGeometry class and Rectangle class
"""


class BaseGeometry(object):
    """Class with method area"""
    def area(self, width, *height):
        """ Returns the area
        """
        return (width * height[0])

    def integer_validator(self, name, value):
        """
        Validates an attribute value
        Args:
            name :(string) Name
            value :(int) Integer
        """
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise TypeError("<name> must be greater than 0")

class Rectangle(BaseGeometry):
    """Rectangle class inheriting from BaseGeometry class"""
    def __init__(self, width, height):
        BaseGeometry.integer_validator("", width)
        BaseGeometry.integer_validator("", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"

class Square(Rectangle):
    """Square class inheriting form Rectangle Class"""
    def __init__(self, size):
        BaseGeometry.integer_validator("", size)
        self.__size = size
