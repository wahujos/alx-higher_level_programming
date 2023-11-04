#!/usr/bin/python3
'''
doc string - defines an add integer function

'''


def add_integer(a, b=98):
    '''documenting function'''
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
