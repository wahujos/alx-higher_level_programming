#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        sorted_list = sorted(my_list)
        maximum = sorted_list[-1]
        return maximum
