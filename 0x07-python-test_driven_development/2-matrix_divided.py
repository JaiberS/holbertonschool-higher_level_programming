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
    if matrix is None:
        str1 = "matrix must be a matrix (list of lists)"
        raise TypeError(str1 + ' of integers/floats')
    for i in range(len(matrix)):
        if matrix[i] is None:
            str1 = "matrix must be a matrix (list of lists)"
            raise TypeError(str1 + ' of integers/floats')
        for j in range(len(matrix[i])):
            tipo = type(matrix[i][j])
            if tipo is not int and tipo is not float:
                str1 = "matrix must be a matrix (list of lists)"
                raise TypeError(str1 + ' of integers/floats')
    rowlen = len(matrix[0])
    for i in range(len(matrix)):
        if len(matrix[i]) is not rowlen:
            raise TypeError('Each row of the matrix must have the same size')
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    nx = list(map(lambda its: list(map(lambda x: ef(x, div), its)), matrix))
    return nx


def ef(x, div):
    if div == float('inf') and x < 0:
        x = x * -1
    return round(x / div, 2)
