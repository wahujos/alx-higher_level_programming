#!/usr/bin/python3
'''Module documentation'''


def read_file(filename=""):
    '''defining the function'''
    with open(filename, 'r', encoding="UTF8") as f:
        for line in f:
            print(line, end='')
