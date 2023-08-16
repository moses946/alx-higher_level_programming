#!/usr/bin/python3
def roman_to_int(roman_string):
    r = roman_string
    table = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    i = 0
    result = 0
    while i < len(r):
        if list(table.keys()).index(r[i]) < list(table.keys()).index(r[i + 1]):
            temp = table[r[i + 1]] - table[r[i]]
            result += temp
            i += 2
        else:
            result += table[r[i]]
            i += 1
    return result
