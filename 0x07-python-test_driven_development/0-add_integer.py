#!/usr/bin/python3
def add_integer(a, b=98):
    """adds integers"""
    if a is float:
        a = int(a)
    if b is float:
        b = int(b)
    if a is not int:
        raise TypeError("a must be an integer")
    if b is not int:
        raise TypeError("b must be an integer")
    return a + b
