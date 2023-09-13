#!/usr/bin/python3
""" to_json_string module """


import json


def to_json_string(my_obj):
    """ returns a json representation of an object
    Args:
        my_obj (str): string object
    Return:
           Json representation of my_obj
    """
    return json.dumps(my_obj)
