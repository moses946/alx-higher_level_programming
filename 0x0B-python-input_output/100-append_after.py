#!/usr/bin/python3
""" append_after module """


def append_after(filename="", search_string="", new_string=""):
    """ Appends a line of text after each line contanining a specific string
    Args:
        filename(str): name of file to read and append
        search_string(str): search string
        new_string(str): string to append
    """
    if search_string == "":
        return
    with open(filename, 'r', encoding="utf-8") as fileptr:
        content = fileptr.readlines()
    for idx, line in enumerate(content):
        if search_string in line:
            if idx == len(content) - 1:
                content.append(new_string)
                break
            else:
                content.insert(idx + 1, new_string)
                break
    with open(filename, 'w', encoding="utf-8") as fileptr:
        fileptr.writelines(content)
