#!/usr/bin/python3
"""
module contains a function that writes an object
to fileusing json representation
"""


import json


def save_to_json_file(my_obj, filename):
    """returns a textfile containning json representaion
    of an object"""
    return json.dump(my_obj, filename)
