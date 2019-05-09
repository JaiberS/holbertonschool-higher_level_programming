#!/usr/bin/python3
def mutiply_list_map(my_list=[], number=0):
    if my_list is not None:
        if my_list == []:
            return my_list
        new_my_list = []
        numberlist = []
        for i in range(len(my_list)):
            numberlist.append(number)
        new_my_list.append(list(map(lambda x, y: x * y, my_list, numberlist)))
        new_my_list = new_my_list[0]
        return new_my_list
