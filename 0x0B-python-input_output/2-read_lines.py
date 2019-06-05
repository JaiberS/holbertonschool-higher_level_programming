#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, 'r', encoding='utf-8') as jfile:
        text = jfile.read()
        count = text.count('\n')
        if nb_lines <= 0 or nb_lines >= count:
            print(text, end='')
        else:
            splitted = text.split('\n')
            while(len(splitted ) != nb_lines):
                splitted.pop(-1)
            print('\n'.join(splitted))
