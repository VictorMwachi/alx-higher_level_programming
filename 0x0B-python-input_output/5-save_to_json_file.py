#!/usr/bin/python3
"""
module contains a function that writes an object
to fileusing json representation
"""


import json


def save_to_json_file(my_obj, filename):
    """returns a textfile containning json representaion
    of an object"""
    with open(filename, 'w', encoding='utf-8') as f:
        return json.dump(my_obj, f)
