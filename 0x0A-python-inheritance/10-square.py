#!/usr/bin/python3
"""defining of the module"""


class BaseGeometry:
    """defining a class"""
    def area(self):
        """defining the function"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """defining the interger validator function"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """class documentation"""
    def __init__(self, width, height):
        """init function"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """defining area function"""
        return self.__width * self.__height

    def __str__(self):
        """defining str function"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """class documentation"""
    def __init__(self, size):
        """init function"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """custom area function"""
        return self.__size * self.__size

    def __str__(self):
        """Defining str function in square class"""
        return "[Rectange] {}/{}".format(self.__size, self.__size)
