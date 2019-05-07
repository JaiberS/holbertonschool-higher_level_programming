#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    k = 0
    if matrix == [[]]:
        print()
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix[i]) - 1):
                print("{:d}".format(matrix[i][j]), end=" ")
                k = j
            k += 1
            print("{:d}".format(matrix[i][k]))
