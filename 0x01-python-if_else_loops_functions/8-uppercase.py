#!/usr/bin/python3

def uppercase(str):
    for i in str:
        val = ord(i) if 97 > ord(i) <= 122 else ord(i) - 32
        print("{}".format(chr(val)), end='')
    print('')
