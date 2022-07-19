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
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """function that returns area of square"""

    def area(self):
        return self.__size ** 2
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(sel.__size):
                for j in range(self.__size):
                    print('#',end='')
