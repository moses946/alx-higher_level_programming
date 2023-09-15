#!/usr/bin/python3
"""
The ``Print square`` module.
Prints a square with the character '#'
    >>> print_square(3)
    ###
    ###
    ###
"""


def print_square(size):
    """
    Prints a square using the character '#'.
    Args:
        size: (int) length of the square
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(size):
        for i in range(size):
            print('#', end='')
        print()


if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/4-print_square.txt")
