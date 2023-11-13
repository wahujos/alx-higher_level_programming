#!/usr/bin/python3
""" handling documentations"""
import json
"""handling json files"""

class Base:
    """Defining class Base"""
    __nb_objects = 0
    """Class attribute, like a variable of the class"""

    def __init__(self, id=None):
        """Initializing function"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == {}:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        filename = "{}.json".format(cls.__name__)
        with open(filename, mode = 'w', encoding="UTF8") as f:
            obj_dicts = [obj.to_dictionary() for obj in list_ojs]
            json_str = cls.to_json_string(obj_dicts)
            f.write(json_str)
