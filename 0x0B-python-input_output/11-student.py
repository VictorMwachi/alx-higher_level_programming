#!/usr/bin/python3
"""
module contains class student
"""


class Student:
    """defines a student"""
    def __init__(self, first_name, last_name, age):
        """initialises class student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            dict_new = {}
            for att in attrs:
                if hasattr(self, att):
                    dict_new[att] = getattr(self, att)
            return dict_new

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        save = vars(self)
        for key, value in json.items():
            save[key] = value
