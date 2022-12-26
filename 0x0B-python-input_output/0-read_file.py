#!/usr/bin/python3
"""
module contains a function for reading a file
"""


def read_file(filename=""):
    """reads a file"""
    with open(filename,encoding="utf-8") as f:
        f.read()
