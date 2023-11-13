#!/usr/bin/python3
"""handle module docs"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """defining the class square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        c_name = __class__.__name__
        s_id = self.id
        s_x = self.x
        s_y = self.y
        s_s = self.width
        return "[{}] ({}) {}/{} - {}".format(c_name, s_id, s_x, s_y, s_s)
    
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        if args:
            attributes = ['id', 'size', 'x', 'y']
            for i, value in enumerate(args):
                setattr(self, attributes[i], value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        return {'id' : self.id,
                'size': self.width,
                'x': self.x,
                'y': self.y
                }
