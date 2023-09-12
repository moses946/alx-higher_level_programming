#!/usr/bin/python3
""" Module containing BaseGeometry class and Rectangle class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inheriting form Rectangle Class"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
