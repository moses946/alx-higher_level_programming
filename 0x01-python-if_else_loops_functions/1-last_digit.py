#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

str_number = int(str(number)[-1])

if str_number > 5:
    print(f"Last digit of {number} is {str_number} and is greater than 5")
elif str_number == 0:
    print(f"Last digit of {number} is {str_number} and is 0")
else:
    print(f"Last digit of {number} is {str_number} and is less than 6")
