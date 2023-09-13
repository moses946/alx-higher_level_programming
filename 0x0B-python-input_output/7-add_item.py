#!/usr/bin/python3
""" script adding all arguments and saves them to a file """


import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    current_list = load_from_json_file("add_item.json")
    for idx, val in enumerate(sys.argv):
        if idx != 0:
            current_list.append(val)
    save_to_json_file(current_list, "add_items.json")
except Exception:
    new_list = []
    for idx, val in enumerate(sys.argv):
        if idx != 0:
            new_list.append(val)
    save_to_json_file(new_list, "add_items.json")
