#!/usr/bin/python3
"""
module has class base
"""


import json, os


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

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            new = cls(5, 5)
        else:
            new = cls(10)
        return new

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = f"{cls.__name__}.json"
        if os.path.exists(filename) is False:
            return []
        else:
            with open(filename, encoding='utf-8') as f:
                json_str = f.read()
        list_dic = cls.from_json_string(json_str)
        list_ins = []
        for i in range(len(list_dic)):
            list_ins.append(cls.create(**list_dic[i]))
        return list_ins
