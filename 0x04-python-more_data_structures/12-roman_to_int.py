#!/usr/bin/python3
def roman_to_int(roman_string):
    if not str(roman_string).isalpha():
        return 0
    if roman_string is None:
        return 0
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    previous = 0
    for i in roman_string:
        current = romans.get(i, 0)
        if current <= previous or previous == 0:
            total += current
        else:
            total += current - (previous * 2)
        previous = romans.get(i, 0)
    return total
