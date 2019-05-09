#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_list = []
    for i in range(len(set_1)):
        counter = 0
        for j in range(len(set_2)):
            if list(set_1)[i] == list(set_2)[j]:
                counter += 1
                continue
        if counter != 0:
            new_list.append(list(set_1)[i])
    return new_list
