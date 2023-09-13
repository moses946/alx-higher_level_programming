#!/usr/bin/python3
""" module containing student class
"""


class Student:
    """ Student class
    Attributes:
        first_name: string
        last_name: string
        age: int
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        a = attrs
        return {n: getattr(self, n) for n in vars(self) if a is None or n in a}

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
