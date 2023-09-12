#!/usr/bin/python3
""" Returns True if object is instance of a class
"""


def inherits_from(obj, a_class):
    """ Returns True if the object is an instance of a class
    """
    return issubclass(obj, a_class)
