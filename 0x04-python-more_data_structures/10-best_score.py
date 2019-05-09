#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None and len(a_dictionary) != 0:
        maxim = -99999999999
        keymax = ''
        for i, j in a_dictionary.items():
            if maxim < j:
                maxim = j
                keymax = i
        return keymax
    else:
        return None
