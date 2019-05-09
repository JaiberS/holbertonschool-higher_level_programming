#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dic = []
    for i, j in a_dictionary.items():
        if j == value:
            new_dic.append(i)
    for k in new_dic:
        del a_dictionary[k]
    return a_dictionary
