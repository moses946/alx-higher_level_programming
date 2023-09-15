#!/usr/bin/python3
"""
The ``text indentation`` method
Prints a text with 2 new lines after special characters
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after '.' , '?' and ':'
    Args:
        text: (str) String of text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in ".:?":
        text = text.replace(char, char + "\n\n")
    lines = text.split("\n")
    for i, line in enumerate(lines):
        lines[i] = line.strip()
    text = "\n".join(lines)
    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/5-text_indentation.txt")
