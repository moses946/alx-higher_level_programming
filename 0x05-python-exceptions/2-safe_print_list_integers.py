#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        while count < x:
            print("{:d}".format(my_list[count]))
            count += 1
        return (count)
    except Exception:
        raise Exception