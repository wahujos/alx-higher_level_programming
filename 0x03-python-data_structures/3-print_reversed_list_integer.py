#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return
    reverse = my_list[::-1]
    for i in reverse:
        print("{:d}".format(i))
