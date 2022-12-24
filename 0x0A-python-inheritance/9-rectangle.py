#!/usr/bin/python3
"""contins basegeometry empty class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class rectangle"""
    def __init__(self, width, height):
        """initialises class rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """retuns the area"""
        return self.__width * self.__height

    def __str__(self):
        """string defination of class rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"
