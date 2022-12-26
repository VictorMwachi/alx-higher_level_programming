#!/usr/bin/python3
"""
module contains a function that
returns JSON representation of
an object(string)
"""


import json
def to_json_string(my_obj):
    """reurns string rep of an object"""
    return json.dumps(my_obj)
