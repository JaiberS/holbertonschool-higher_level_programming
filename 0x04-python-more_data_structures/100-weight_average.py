#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    div = []
    total = 0
    total2 = 0
    for i, j in my_list:
        total += i * j
        div.append(j)
    for k in div:
        total2 += k
    total /= total2
    return total
