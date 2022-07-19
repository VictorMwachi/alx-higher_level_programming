#!/usr/bin/python3
"""class square"""


class Square:
    """initialise class square"""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """function that returns area of square"""

    def area(self):
        return self.__size ** 2
