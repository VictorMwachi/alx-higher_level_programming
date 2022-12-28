#!/usr/bin/python3
"""
module has class base
"""


import json


class Base:
    """base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialises class base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return f"[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = f"{cls.__name__}.json"
        list_dic = []
        if list_objs is None:
            pass
        else:
            for obj in list_objs:
                list_dic.append(obj.to_dictionary())
        list_str = cls.to_json_string(list_dic)
        with open(filename, 'w') as f:
            f.write(list_str)

    @staticmethod
    def from_json_string(json_string):
        """returns alist of json strings"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)
