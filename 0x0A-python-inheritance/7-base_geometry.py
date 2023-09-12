#!/usr/bin/python3
""" Module containing BaseGeometry class
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
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/7-base_geometry.txt")
