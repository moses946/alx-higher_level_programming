#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    r = roman_string.upper()
    table = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    k = list(table.keys())
    i = 0
    result = 0
    while i < len(r):
        if r[i] not in k:
            return 0
        if i < len(r) - 1 and k.index(r[i]) < k.index(r[i + 1]):
            temp = table[r[i + 1]] - table[r[i]]
            result += temp
            i += 2
        else:
            result += table[r[i]]
            i += 1
    return result
