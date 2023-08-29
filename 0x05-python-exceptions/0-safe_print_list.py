#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    while count < x and x > 0:
        try:
            print(my_list[count], end="")
            count += 1
            return (count)
        except IndexError:
            pass
    print()
    return (count)      
