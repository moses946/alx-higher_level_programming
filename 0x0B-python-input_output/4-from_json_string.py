#!/usr/bin/python3
""" from_json_string module """


import json


def from_json_string(my_str):
    """ Return an object represented by a JSON string
    Args:
        my_str (str): JSON string
    Return:
           Object represented by JSON string
    """
    return json.loads(my_str)
