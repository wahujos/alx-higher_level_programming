#!/usr/bin/python3
'''Handle modules and any other stuff'''
from models.base import Base
'''Getting information about the base'''


class Rectangle(Base):
    """defining the class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """defining the initialization method defining
        the initialization method"""
        super().__init__(id)
        """super class with super capabilities super
        class with super capabilities"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """place holder documentation place holder documentation """
        return self.__width

    @width.setter
    """place holder documentation place holder documentation """
    def width(self, value):
        """place holder documentation place holder documentation """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    """place holder documentation place holder documentation """
    def height(self):
        """place holder documentation place holder documentation """
        return self.__height

    @height.setter
    def height(self, value):
        """place holder documentation place holder documentation """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        """place holder documentation place holder documentation """
        return self.__x

    @x.setter
    def x(self, value):
        """place holder documentation place holder documentation """
        if not isinstance(value, int):
            raise TypeError("x must be an interger")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """place holder documentation place holder documentation """
        return self.__y

    @y.setter
    def y(self, value):
        """place holder documentation place holder documentation """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """place holder documentation place holder documentation
        123456789"""
        return self.__width * self.__height

    """place holder documentation place holder documentation """
    def display(self):
        """for i in range(self.__height):
            for j in range(self.__width):
                print("#", end='')
            print()"""
        for _ in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """place holder documentation place holder documentation """
        c_name = __class__.__name__
        s_id = self.id
        x1 = self.x
        y1 = self.y
        w1 = self.width
        h1 = self.height
        return "[{}] ({}) {}/{} - {}/{}".format(c_name, s_id, x1, y1, w1, h1)

    def update(self, *args, **kwags):
        """place holder documentation place holder documentation """
        if args:
            attributes_given = ['id', 'width', 'height', 'x', 'y']
            for i, value in enumerate(args):
                setattr(self, attributes_given[i], value)
        elif kwags:
            for key, value in kwags.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """place holder documentation place holder documentation """
        return {'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y}
