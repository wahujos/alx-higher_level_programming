#!/usr/bin/python3
"""defining module"""


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
