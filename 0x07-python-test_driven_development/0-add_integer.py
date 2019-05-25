#!/usr/bin/python3
"""
>>> add_integer(2, 3)
5

"""


def add_integer(a, b=98):
    """
    >>> c = add_integer(2, 3)
    """
    if type(a) is not int:
        if type(a) is not float:
            raise TypeError('a must be an integer')
    if type(b) is not int:
        if type(b) is not float:
            raise TypeError('b must be an integer')
    return int(a + b)
