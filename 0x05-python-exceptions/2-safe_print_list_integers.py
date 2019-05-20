#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    j = 0
    for i in range(0, x):
        printed = printint(my_list[i])
        if printed:
            j += 1
    print()
    return j


def printint(value):
    try:
        print("{:d}".format(value), end="")
        return True
    except ValueError:
        return False
    except TypeError:
        return False
