#!/usr/bin/python3
""" This module contains definition of MyList class
"""


class MyList(list):
    """ Class MyList that inherits from list
    """
    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))


if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/1-my_list.txt")