#!/usr/bin/python3
"""read_file module"""


def read_file(filename=""):
    """reads a textfile and prints it to stdout

        Args:
            filename :(str) Text file name
    """
    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read(), end="")

