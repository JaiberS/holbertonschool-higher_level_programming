#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda items: list(map(lambda x: x * x, items)), matrix))
