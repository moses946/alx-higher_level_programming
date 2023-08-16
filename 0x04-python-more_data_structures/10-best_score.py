#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_val = float('-inf')
    max_key = ""
    for key, val in a_dictionary.items():
        if val > max_val:
            max_val = val
            max_key = key
    return max_key
