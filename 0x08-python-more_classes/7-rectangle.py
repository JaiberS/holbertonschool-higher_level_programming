#!/usr/bin/python3
class Rectangle:

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
        if not type(width) == int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        if not type(height) == int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not type(value) == int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not type(value) == int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.height * 2

    def __str__(self):
        str0 = ''
        if self.__width == 0 or self.__height == 0:
            return str0
        for i in range(self.__height):
            str0 = str0 + str(self.print_symbol) * self.__width + '\n'
        return str0[:-1]

    def __repr__(self):
        str1 = "Rectangle("
        return str1 + str(self.__width) + ", " + str(self.__height) + ')'

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")