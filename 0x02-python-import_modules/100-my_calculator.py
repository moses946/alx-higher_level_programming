#!/usr/bin/python3
from sys import argv
from calculator_1 import *
operators = ['+', '-', '*', '/']
if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    result = int(eval(str(int(argv[1]))+argv[2]+str(int(argv[3]))))
    print(f"{argv[1]} {argv[2]} {argv[3]} = {result}")
