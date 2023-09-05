"""
The ``Say my name`` module
Prints "My name is <first name> <last name>"
"""
def say_my_name(first_name, last_name=""):
    """
    Prints the args as part of a string
    Args:
        first_name: (str) String representing first name
        last_name: (str) String representing last name (defaults to "")
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")

if __name__ == "__main__":
    import doctest
    doctest.testfile('./test/3-say_my_name.txt')