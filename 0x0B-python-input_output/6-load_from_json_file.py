#!/usr/bin/python3
"""
module contains a function that creates an Object from a JSON file
"""


import json


def load_from_json_file(filename):
    """returns an object created from a json file"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.dump(f)
