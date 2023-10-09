#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    reverse = my_list[::-1]
    for i in reverse:
        if i == 1:
            print("{:d}".format(i))
            continue
        print("{:d}".format(i))
