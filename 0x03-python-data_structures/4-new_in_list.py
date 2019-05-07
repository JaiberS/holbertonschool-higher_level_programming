#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    ln = len(my_list)
    if idx >= ln:
        return my_list
    my_new_list = []
    for i in range(ln):
        my_new_list.append(my_list[i])
    my_new_list[idx] = element
    return my_new_list
