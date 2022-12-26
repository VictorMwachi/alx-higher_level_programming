#!/usr/bin/python3
"""
module contains function for appending a file
"""


def append_write(filename="", text=""):
    """appends text to a file and retuns the updated file"""
    with open(filename, 'a', encoding='utf-8') as f:
        return(f.write(text))
