#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_list = sorted(list(a_dictionary.items()))
    for i, j in new_list:
        print(i + ': ' + str(j))
