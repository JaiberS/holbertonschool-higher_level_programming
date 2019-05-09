#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_list = []
    new_list.append(true_common(set_1, set_2))
    new_list.append(true_common(set_2, set_1))
    for i in range(len(new_list[1])):
        new_list[0].append(new_list[1][i])
    del new_list[1]
    new2_list = new_list[0]
    return new2_list


def true_common(set_1, set_2):
    new_list = []
    for i in range(len(set_1)):
        counter = 0
        for j in range(len(set_2)):
            if list(set_1)[i] == list(set_2)[j]:
                counter += 1
                continue
        if counter == 0:
            new_list.append(list(set_1)[i])
    return new_list
