#!/usr/bin/python3
'''creating a class named Square'''


class Square:
    '''defining initialization method'''
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    '''returns the current square area'''
    def area(self):
        return self.__size * self.__size
