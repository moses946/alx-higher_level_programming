#!/usr/bin/python3
def print_matrix_integer(matrix=[]):
    for row in matrix:
        for idx, val in enumerate(row):
            if idx != len(row) - 1:
                print("{:d} ".format(int(val)), end='')
            else:
                print("{:d}".format(int(val)), end='')
        print()
