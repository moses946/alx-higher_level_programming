#!/usr/bin/python3
""" class_to_json module """


import json


def class_to_json(obj):
    """ Returns dictionary description of an object in json """
    return {name: getattr(obj, name) for name in vars(obj)}
