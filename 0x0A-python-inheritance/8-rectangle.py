#!/usr/bin/python3
""" Module containing BaseGeometry class and Rectangle class
"""


class BaseGeometry(object):
    """Class with method area"""
    def area(self):
        """ Not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates an attribute value
        Args:
            name :(string) Name
            value :(int) Integer
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise TypeError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """Rectangle class inheriting from BaseGeometry class"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
