#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_val = 0
    for i in my_list:
        max_val = int(i) if int(i) > max_val else max_val
    return max_val
