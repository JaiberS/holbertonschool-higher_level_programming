#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return
    ln = len(my_list)
    if idx > ln:
        return
    return(my_list[idx])
