#!/usr/bin/python3
'''module began'''


class Square:
    ''' class created'''
    def __init__(self, size=0):
        '''initialization method'''
        self.__size = size

    @property
    def size(self):
        '''getter'''
        return self.__size

    @size.setter
    def size(self, value):
        '''setter'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        '''returns area'''
        return self.__size ** 2

    def my_print(self):
        '''prints hashes'''
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()
