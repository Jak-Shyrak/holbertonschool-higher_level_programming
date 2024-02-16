#!/usr/bin/python3
"""
Module for Rectangle class inherited from BaseGeometry.
"
"
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class Square that inherits from Rectangle.
    """
    def __init__(self, size):
        """
        Initializes the Square.

        Args:
            size: The size of the Square.
        """
        super().integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        return self._Rectangle__width * self._Rectangle__height

    def __str__(self):
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
