#!/usr/bin/python3
"""class square"""


class Square:
    """initialise class square"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size
    
    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        
        @position.setter
        def position(self, value):
            if type(value) is not tuple or len(value) != 2 or type(value[0]) is not int or type(value[1]) is not int or type(value[0]) < 0 or type(value[1]) < 0:
                raise TypeError("position must be a tuple of 2 positive integers")

    """function that returns area of square"""

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
