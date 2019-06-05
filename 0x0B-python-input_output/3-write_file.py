#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, mode='w', encoding='utf-8') as jfile:
        count = jfile.write(text)
        return count
