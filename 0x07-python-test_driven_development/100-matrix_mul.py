#!/usr/bin/python3
"""
    >>> tester.matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
    [[7, 10], [15, 22]]

"""


def matrix_mul(m_a, m_b):
    """
    >>> c = tester.matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
    """
    if type(m_a) is not list:
        raise TypeError('m_a must be a list')
    if type(m_b) is not list:
        raise TypeError('m_b must be a list')
    if m_a == []:
        raise TypeError('m_a must be a list of lists')
    if m_b == []:
        raise TypeError('m_b must be a list of lists')
    for i in range(len(m_a)):
        if type(m_a[i]) is not list:
            raise TypeError('m_a must be a list of lists')
    for i in range(len(m_b)):
        if type(m_b[i]) is not list:
            raise TypeError('m_b must be a list of lists')
    if m_a == [[]]:
        raise ValueError('m_a can\'t be empty')
    if m_b == [[]]:
        raise ValueError('m_b can\'t be empty')
    for i in range(len(m_a)):
        if m_a == [[]] or m_a[i] == []:
            raise ValueError('m_a can\'t be empty')
    for i in range(len(m_b)):
        if m_b == [[]] or m_b[i] == []:
            raise ValueError('m_b can\'t be empty')
    for i in range(len(m_a)):
        for j in range(len(m_a[i])):
            if type(m_a[i][j]) is not int and type(m_a[i][j]) is not float:
                raise TypeError('m_a should contain only integers or floats')
    for i in range(len(m_b)):
        for j in range(len(m_b[i])):
            if type(m_b[i][j]) is not int and type(m_b[i][j]) is not float:
                raise TypeError('m_b should contain only integers or floats')
    rowlen = len(m_a[0])
    for i in range(len(m_a)):
        if len(m_a[i]) is not rowlen:
            raise TypeError('each row of m_a must should be of the same size')
    rowlen = len(m_b[0])
    for i in range(len(m_b)):
        if len(m_b[i]) is not rowlen:
            raise TypeError('each row of m_b must should be of the same size')
    if len(m_a[0]) != len(m_b):
        raise ValueError('m_a and m_b can\'t be multiplied')
    nm = [[]]
    for i in range(len(m_a)):
        nv = []
        for j in range(len(m_b[0])):
            nv.append(0)
        nm.append(nv)
    nm[0] = nm.pop(-1)
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                nm[i][j] += m_a[i][k] * m_b[k][j]
    return nm
