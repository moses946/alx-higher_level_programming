#!/usr/bin/python3

def print_last_digit(number):
    if type(number) != int:
        return TypeError
    print("{}".format(str(number)[-1]), end='')
    return str(number)[-1]
