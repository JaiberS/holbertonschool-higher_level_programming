#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lna = len(tuple_a)
    lnb = len(tuple_b)
    lista = []
    listb = []
    for i in range(lna):
        lista.append(tuple_a[i])
    while lna < 2:
        lista.append(0)
        lna += 1
    for i in range(lnb):
        listb.append(tuple_b[i])
    while lnb < 2:
        listb.append(0)
        lnb += 1
    tuple_c = (lista[0] + listb[0], lista[1] + listb[1])
    return(tuple_c)
