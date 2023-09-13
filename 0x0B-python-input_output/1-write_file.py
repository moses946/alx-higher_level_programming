#!/usr/bin/python3
""" write_file module """


def write_file(filename="", text=""):
    """ writes a string to text file
    Args:
        filename (str): Filename
        text (str): String
    """
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
