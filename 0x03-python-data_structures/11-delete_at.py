#!/usr/bin/python3
import pdb


def delete_at(my_list=[], idx=0):
    pdb.set_trace()
    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list
