"""pascal triangle module"""


def pascal_triangle(n):
    """ Returns a list of lists of integers
    Args:
        n (int): Integer
    """
    if n <= 0:
        return []
    result = [[1]]
    for i in range(1, n):
        row = [1]
        last_row = result[-1]
        row += [sum(pairs) for pairs in zip(last_row, last_row[1:])]
        row .append(1)
        result.append(row)
    return result
