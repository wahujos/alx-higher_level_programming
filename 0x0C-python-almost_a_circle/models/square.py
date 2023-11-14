#!/usr/bin/python3
from models.rectangle import Rectangle
""" documentation of the rectangle class that we inherit from"""
from models.base import Base
""" documentation of the base class that we inherit from"""


class Square(Rectangle):
    """defining the class square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """place holder documentation place holder documentation """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """place holder documentation place holder documentation """
        c_name = __class__.__name__
        s_id = self.id
        s_x = self.x
        s_y = self.y
        s_s = self.width
        return "[{}] ({}) {}/{} - {}".format(c_name, s_id, s_x, s_y, s_s)

    @property
    def size(self):
        """place holder documentation place holder documentation """
        return self.width

    @size.setter
    def size(self, size):
        """place holder documentation place holder documentation """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """place holder documentation place holder documentation """
        if args:
            attributes = ['id', 'size', 'x', 'y']
            for i, value in enumerate(args):
                setattr(self, attributes[i], value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """place holder documentation place holder documentation """
        return {'id': self.id,
                'size': self.width,
                'x': self.x,
                'y': self.y
                }
