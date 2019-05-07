#!/usr/bin/python3
def no_c(my_string):
    ln = len(my_string)
    i = 0
    while i < ln:
        if my_string[i] == 'c' or my_string[i] == 'C':
            my_string = remove_char_at(my_string, i)
            ln -= 1
        i += 1
    return(my_string)


def remove_char_at(str, n):
    if n < 0:
        return(str)
    return(str[0:n] + str[n + 1:])
