#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    while count < x and x > 0:
        try:
            print("{:d}".format(my_list[count]), end='')
        except ValueError:
            pass
        count += 1
    return (count)
