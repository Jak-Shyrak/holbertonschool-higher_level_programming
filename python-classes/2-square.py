#!/usr/bin/python3
"""Contains a class definition of 'Square'"""


class Square:
    """Definition of private size in square"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            