#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for inner_list in matrix:
        temp = []
        for val in inner_list:
            temp.append(val ** 2)
        new_matrix.append(temp)
    return new_matrix
