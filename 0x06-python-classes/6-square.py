#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        if not type(size) == int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        if not type(position) == tuple or not len(position) == 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        for i in range(len(position)):
            if not type(position[i]) == int or position[i] < 0:
                str1 = 'position must be a tuple of 2'
                raise TypeError(str1 + ' positive integers')
        self.__size = size
        self.__position = position

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not type(value) == int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(' ' * self.__position[0] + '#' * self.__size)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not type(value) == tuple or not len(value) == 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        for i in range(len(value)):
            if not type(value[i]) == int or value[i] < 0:
                str1 = 'position must be a tuple of 2'
                raise TypeError(str1 + ' positive integers')
        self.__position = value
