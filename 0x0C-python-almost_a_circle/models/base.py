#!/usr/bin/python3
"""
module has class base
"""


class Base:
    """base class"""
    __nb_objects = 0
    def __init__(self, id=None):
        """initialises class base"""
        if self.id is not None:
            self.id = id
        else:
            Base.__nb_objects +=1
