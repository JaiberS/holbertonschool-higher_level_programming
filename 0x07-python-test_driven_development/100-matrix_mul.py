#!/usr/bin/python3
"""
    >>> tester.matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
    [[7, 10], [15, 22]]

"""


def matrix_mul(m_a, m_b):
    """
    >>> c = tester.matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
    """
    if m_a is not list:
        raise TypeError('m_a must be a list')
    if m_b is not list:
        raise TypeError('m_b must be a list')
    for i in m_a:
        if type(i) is not list:
            raise TypeError('m_a must be a list of lists')
        if m_a is [[]] or i is []:
            raise ValueError('m_a can\'t be empty')
    for i in m_b:
        if type(i) is not list:
            raise TypeError('m_b must be a list of lists')
        if m_b is [[]] or i is []:
            raise ValueError('m_b can\'t be empty')
    for i in range(len(m_a)):
        if not all(isinstance(x, int) for x in m_a[i]):
            raise TypeError('m_a should contain only integers or floats') 
    for i in range(len(m_b)):
        if not all(isinstance(x, int) for x in m_b[i]):
            raise TypeError('m_b should contain only integers or floats')  
    rowlen = len(m_a[0])
    for i in range(len(m_a)):
        if len(m_a) is not rowlen:
            raise TypeError('each row of m_a must should be of the same size')
    rowlen = len(m_b[0])
    for i in range(len(m_b)):
        if len(m_b) is not rowlen:
            raise TypeError('each row of m_b must should be of the same size') 
    if len(m_a[0]) != len(m_b): 
        raise ValueError('m_a and m_b can\'t be multiplied')
   nx = list(map(lambda its: list(map(lambda x: rup(x, div), its)), matrix))
    return nx
