#!/usr/bin/python3
"""
    This is the `0-add_integer` module.
    Returns the addition of two integers e.g:

        >>> add_integer(5, 10)
        15
"""


def add_integer(a, b=98):
    """
        Computes the addition of two integers or floats
        Args:
            a: (int) Integer
            b: (int) Integer (defaults to 98)
        Return: (int) a + b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))


if __name__ == "__main__":
    import doctest
    doctest.testfile('./test/0-add_integer.txt')
