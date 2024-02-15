#!/usr/bin/python3
"""
    class MyList that inherits from list
"""


class MyList(list):
    """
    Class MyList that inherits from list
    """
    def print_sorted(self):
        """
        Prints the list, but sorted (ascending sort)
        """
        for element in self:
            if type(element) is not int:
                raise TypeError("type should be integer")
        print(sorted(self))
