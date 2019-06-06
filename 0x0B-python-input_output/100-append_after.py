#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    with open(filename, mode='r') as jfile:
        totals = ""
        while True:
            i = jfile.readline()
            if i == '':
                break
            totals += i
            if search_string in i:
                totals += new_string
    with open(filename, mode='w') as jfile:
        jfile.write(totals)
