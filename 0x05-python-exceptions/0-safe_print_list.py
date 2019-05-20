#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        j = 0
        for i in range(0, x):
            print("{}".format(my_list[i]), end="")
            j = i
        print()
        j += 1
        return j
    except IndexError:
        print()
        j += 1
        return j
