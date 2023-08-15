#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        copy_list = my_list
        return copy_list
    copy_list = []
    for i, v in enumerate(my_list):
        if i == idx:
            copy_list.append(element)
        else:
            copy_list.append(v)
    return copy_list