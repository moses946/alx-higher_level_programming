#!/usr/bin/python3
""" load_from_json_file module """


import json


def load_from_json_file(filename):
    """ Creates an object from json file """
    with open(filename, 'r', encoding="utf-8") as file:
        json_str = file.read()
        return json.loads(json_str)
