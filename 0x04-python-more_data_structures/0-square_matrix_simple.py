#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        if matrix == []:
            return matrix
        new_matrix = []
        for i in range(len(matrix)):
            new_matrix.append(list(map(square_true, matrix[i])))
        return new_matrix


def square_true(n):
    return n*n
