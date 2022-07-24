#!/usr/bin/python3
def add_integer(a, b=98):
    """adds integers"""
    
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a)!= int:
        raise TypeError("a must be an integer")
    if type(b) != int:
        raise TypeError("b must be an integer")
    return a + b
