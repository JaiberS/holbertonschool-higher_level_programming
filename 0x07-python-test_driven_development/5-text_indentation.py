#!/usr/bin/python3
"""
    >>> tester = __import__('3-text_indentation').text_indentation

"""


def text_indentation(text):
    """
    >>> tester = __import__('3-text_indentation').text_indentation

    """
    str0 = ""
    if type(text) is not str:
        raise TypeError('text must be a string')
    i = 0
    while i < (len(text)):
        if text[i] != '\n':
            str0 += text[i]
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            str0 += '\n' * 2
            while text[i + 1] == ' ':
                i = i + 1
        i = i + 1
    print(str0, end="")
