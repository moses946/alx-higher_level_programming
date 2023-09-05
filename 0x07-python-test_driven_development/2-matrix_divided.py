"""
This is a module containing a matrix divider function.
Divides all the values of a matrix

    >>> matrix = [
    ...         [1, 2, 3],
    ...         [4, 5, 6]
    ...         ]

    >>> matrix_divided(matrix, 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""
def matrix_divided(matrix, div):
    """
    Returns a new matrix after dividing all values of a matrix
    Args:
        matrix: (list) 2D array containing integers
        div: (int/float) Divisor
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not all(isinstance(i, (int, float)) for x in matrix for i in x):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    length = [len(x) for x in matrix]
    if len(set(length)) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    new_matrix = []
    for idx, val in enumerate(matrix):
        new_matrix.append([])
        for digit in val:
            new_matrix[idx].append(round(digit / div, 2))
    return new_matrix

if __name__ == "__main__":
    import doctest
    doctest.testfile('./test/2-matrix_divided.txt')
