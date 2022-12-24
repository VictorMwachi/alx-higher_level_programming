#!/usr/bin/python3
"""
module contains class square
inherritng from class rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """clas square"""
    def __init__(self, size):
        """initilises class square"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """returns area of a square"""
        return self.__size**2
