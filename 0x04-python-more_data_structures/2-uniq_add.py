#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    for i in range(len(my_list)):
        counter = 0
        for j in range(len(new_list)):
            if my_list[i] == new_list[j]:
                counter += 1
                continue
        if counter == 0:
            new_list.append(my_list[i])
    total = 0
    for k in range(len(new_list)):
        total += new_list[k]
    return total
