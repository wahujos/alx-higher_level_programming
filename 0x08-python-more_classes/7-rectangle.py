#!/usr/bin/python3
'''class Rectangle'''


class Rectangle:
    '''class attribute public'''
    number_of_instances = 0
    print_symbol = '#'

    '''defining a class'''
    def __init__(self, width=0, height=0):
        '''initialization'''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        '''returns the area of the rectangle'''
        return self.__height * self.__width

    def perimeter(self):
        '''returns the perimeter of the rectangle'''
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        '''prints hash sign to show the rectangle'''
        rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle
        else:
            return '\n'.join([str(self.print_symbol) * self.__width] * self.__height)

    def __repr__(self):
        '''repr method'''
        module_name = self.__module__
        class_name = self.__class__.__name__
        hex_id = hex(id(self))
        return f"{class_name}({self.__width}, {self.__height})"

    def __del__(self):
        '''called when an instance is deleted'''
        print("Bye rectangle...")
        if Rectangle.number_of_instances > 0:
            Rectangle.number_of_instances -= 1 
