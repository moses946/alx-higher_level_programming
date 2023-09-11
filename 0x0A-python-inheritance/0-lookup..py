""" This module returns attributes and methods of an object
"""


def lookup(obj):
    """ Returns list of available attributes and methods

        Args:
            obj :(class) python object
        
        Return:
            List : Available attributes and methods of an objects

    """
    return [obj.__dict__]
