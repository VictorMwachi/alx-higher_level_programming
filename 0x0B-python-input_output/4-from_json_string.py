#!/usr/bin/python3
"""
module contains a function that
returns an object (Python data structure)
represented by a JSON string
"""


import json


def from_json_string(my_str):
    """retirns python data structure
    represented by a json string"""
    return json.load(my_str)
