#!/usr/bin/python3
"""
checks if  is a subclass or instance of a specified class
"""


def is_kind_of_class(obj, a_class):
    """returns true or false wheteher an object
    is a subclass or instance of specified class"""
    return isinstance(obj, a_class) or type(obj) == a_class
