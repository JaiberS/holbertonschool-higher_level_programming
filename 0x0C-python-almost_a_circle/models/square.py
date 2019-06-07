#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        if type(size) is not int:
            raise TypeError('width must be an integer')
        if size <= 0:
            raise ValueError('width must be > 0')
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__size = value

    def __str__(self):
        str0 = "[" + self.__class__.__name__ + "] (" + str(self.id) + ") "
        str1 = str(self.x) + "/" + str(self.y) + " - " + str(self.__size)
        return str0 + str1

    def update(self, *args, **kwargs):
        if args is None or len(args) == 0:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.__size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
        else:
            if len(args) < 1:
                return
            self.id = args[0]
            if len(args) < 2:
                return
            self.__size = args[1]
            if len(args) < 3:
                return
            self.x = args[2]
            if len(args) < 4:
                return
            self.y = args[3]

    def to_dictionary(self):
        d = {}
        d.setdefault('id', self.id)
        d.setdefault('size', self.__size)
        d.setdefault('x', self.x)
        d.setdefault('y', self.y)
        return d
