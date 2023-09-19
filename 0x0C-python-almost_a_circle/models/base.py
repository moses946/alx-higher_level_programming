""" module containing base class
"""


import json
import os


class Base:
    """ The super class
    Attr:
        __nb_objects: (int) number of class instances
    """
    __nb_objects = 0

    def __init__(self, id=None):
        self.__nb_objects += 1
        if id:
            self.id = id
        else:
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns json string representation of list dicts"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps([obj.__dict__ for obj in list_dictionaries])

    @classmethod
    def save_to_file(cls, list_objs):
        """ saves json string representation to file """
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            file.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates dummy class instance"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            TypeError("Invalid class")

        cls.update(dummy, **dictionary)

    @classmethod
    def load_from_file(cls):
        """ Return list of instances"""
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        with open(filename, 'r') as file:
            list_dicts = cls.from_json_string(file.read())
            return [cls.create(**dict_) for dict_ in list_dicts]
