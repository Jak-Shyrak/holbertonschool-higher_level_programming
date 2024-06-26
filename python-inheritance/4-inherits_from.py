#!/usr/bin/python3
"""
    returns True if the object is an instance of\
          a class that inherited (directly or indirectly) from\
              the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance of\
          a class that inherited (directly or indirectly) from\
              the specified class ; otherwise False."""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
