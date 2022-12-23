#!/usr/bin/python3
"""
checks if  is an instance of a specified class
"""


def is_same_class(obj, a_class):
    """returns true or false wheteher an object is instance of specified class"""
    return issubclass(obj,a_class)
