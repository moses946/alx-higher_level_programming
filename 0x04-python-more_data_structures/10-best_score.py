#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_val = float('-inf')
    max_key = ""
    for key, val in a_dictionary.items():
        if val is not None and val > max_val:
            max_val = val
            max_key = key
        if max_val == float('-inf'):
            return None
    return max_key
