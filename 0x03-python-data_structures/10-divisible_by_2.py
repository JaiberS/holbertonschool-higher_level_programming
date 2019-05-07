#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    checker = []
    for i in range(len(my_list)):
        checker.append(my_list[i] % 2 == 0)
    return checker
