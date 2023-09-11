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
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise TypeError("<name> must be greater than 0")