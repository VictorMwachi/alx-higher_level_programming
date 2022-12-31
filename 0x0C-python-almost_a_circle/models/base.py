#!/usr/bin/python3
"""
module has class base
"""


import json
import os
import csv
import turtle


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
        new.update(**dictionary)
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serialises to csv"""
        filename = f"{cls.__name__}.csv"
        if cls.__name__ == 'Rectangle':
            list_keys = ['id', 'width', 'height', 'x', 'y']
        if cls.__name__ == 'Square':
            list_keys = ['id', 'size', 'x', 'y']
        list_s = []
        list_s.append(list_keys)
        if list_objs is None:
            pass
        else:
            for obj in list_objs:
                temp_dic = obj.to_dictionary()
                list_values = []
                for key in list_keys:
                    list_values.append(temp_dic[key])
                list_s.append(list_values)
        with open(filename, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(list_s)

    @classmethod
    def load_from_file_csv(cls):
        """desirealises from csv"""
        filename = f"{cls.__name__}.csv"
        if os.path.exists(filename) is False:
            return []
        if cls.__name__ == 'Rectangle':
            list_keys = ['id', 'width', 'height', 'x', 'y']
        if cls.__name__ == 'Square':
            list_keys = ['id', 'size', 'x', 'y']
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            csv_list = list(reader)
        list_obj = []
        for i, line_list in enumerate(csv_list):
            if i != 0:
                dic_obj = {}
                for j in range(len(list_keys)):
                    dic_obj[list_keys[j]] = int(line_list[j])
                list_obj.append(dic_obj)
        list_ins = []
        for i in range(len(list_obj)):
            list_ins.append(cls.create(**list_obj[i]))
        return list_ins

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ that opens a window and draws all the Rectangles and Squares"""
        turtle.title("Draws all the Rectangles and Squares")
        turtle.pensize(2)
        turtle.speed(1)
        def draw_rect(width, height, x, y):
                """draws rectangle only"""
                turtle.color('blue')
                turtle.forward(x)
                turtle.pendown()
                turtle.begin_fill()
                for l in range(2):
                    turtle.forward(width)
                    turtle.left(90)
                    turtle.forward(height)
                    turtle.left(90)
                turtle.end_fill()
                turtle.penup()
                turtle.forward(width)#move to right end

        def draw_square(size, x, y):
                """draws square only"""
                turtle.pensize(2)
                turtle.speed(1)
                turtle.color('green')
                turtle.forward(x)
                turtle.pendown()
                turtle.begin_fill()
                for l in range(4):
                    turtle.forward(size)
                    turtle.left(90)
                turtle.end_fill()
                turtle.penup()
                turtle.forward(size)#move to right end
        for lis in list_rectangles:
            height = lis.height
            width = lis.width
            draw_rect(width,height,lis.x, lis.y)
        turtle.reset()
        for lis in list_squares:
            size = lis.size
            draw_square(size, lis.x, lis.y)
        turtle.hideturtle()
        turtle.done()
