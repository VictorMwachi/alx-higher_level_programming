#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """Initialize Rectangle object with height and width"""

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """retrieve rectangle width"""
        return self.__width
    
    @width.setter
    def width(self, value):
        if type(value) is not int:
            """setter for the private instance attribute hwidth"""
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrive rectangle height"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """setter for the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
