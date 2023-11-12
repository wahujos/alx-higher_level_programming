#!/usr/bin/python3
""" handling documentations"""


class Base:
    """Defining class Base"""
    __nb_objects = 0
    """Class attribute, like a variable of the class"""

    def __init__(self, id=None):
        """Initializing function"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
