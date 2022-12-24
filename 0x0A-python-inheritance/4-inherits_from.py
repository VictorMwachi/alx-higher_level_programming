#!/usr/bin/python3
"""
checks if  is a subclass of a specified class
"""


def inherits_from(obj, a_class):
    """returns true or false wheteher an object
    is a subclass of specified class"""
    return isinstance(obj, a_class) and obj != a_class
