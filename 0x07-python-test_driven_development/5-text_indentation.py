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
    list_text = text.split(' ')
    special_chars = ['.', '?', ':']
    for word in list_text:
        if any(x in word for x in special_chars):
            print(f"{word}\n")
        else:
            print(f"{word} ", end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("./test/5-text_indentation.txt")