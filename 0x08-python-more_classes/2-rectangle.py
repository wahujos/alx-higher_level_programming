#!/usr/bin/python3
''' class Rectangle '''


class Rectangle:
    '''Defining the class Rectangle'''
    def __init__(self, width=0, height=0):
        '''Initializing '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''retriving the width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''setting the width'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''retriving the height'''
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

    def area(self):
        '''calculating the area of the rectangle'''
        return self.__width * self.__height

    def perimeter(self):
        '''calculating the perimeter of the rectangle'''
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2
