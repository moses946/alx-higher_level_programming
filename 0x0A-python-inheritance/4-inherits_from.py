#!/usr/bin/python3
""" Returns True if object is instance of a class
"""


def inherits_from(obj, a_class):
    """ Returns True if the object is an instance of a class
    """
    if isinstance(obj, a_class) and not issubclass(a_class, obj.__class__):
        return True
    return False
