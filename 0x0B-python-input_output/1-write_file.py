#!/usr/bin/python3
"""
module contains function for writing file
"""


def write_file(filename="", text=""):
    """writes text in file in utf-8 formart"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
