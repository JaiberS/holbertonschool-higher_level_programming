#!/usr/bin/python3
"""
    >>> matrix = [
    ...     [1, 2, 3],
    ...     [4, 5, 6]
    ... ]

    >>> tester.matrix_divided(matrix, 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""


def matrix_divided(matrix, div):
    """
    >>> c = matrix_divided(matrix, 3)
    """
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    rowlen = len(matrix[0])
    for i in range(len(matrix)):
        if len(matrix[i]) is not rowlen:
            raise TypeError('Each row of the matrix must have the same size')
    for i in range(len(matrix)):
        if not all(isinstance(x, int) for x in matrix[i]):
            str1 = "matrix must be a matrix (list of lists)"
            raise TypeError(str1 + ' of integers/floats')
    nx = list(map(lambda its: list(map(lambda x: rup(x, div), its)), matrix))
    return nx


def rup(x, div):
    floored = int((x / div) * 1000)
    if floored % 10 >= 5:
        return (int(floored / 10) + (x % div > 0)) / 100
    return int(floored / 10) / 100
