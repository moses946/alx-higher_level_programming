#!/usr/bin/python3
""" save_to_json_file module """


import json


def save_to_json_file(my_obj, filename):
    """ writes an object to a text file """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
