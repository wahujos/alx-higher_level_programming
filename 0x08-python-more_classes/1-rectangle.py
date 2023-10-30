#!/usr/bin/python3
'''A class Rectangle'''


class Rectangle:
    '''Defining class rectangle'''
    def __init__(self, width=0, height=0):
        '''initializing the init method'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''retrieve width property'''
        return self._width

    @width.setter
    def width(self, value):
        '''Sets the width'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''retriving height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setting the height'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
