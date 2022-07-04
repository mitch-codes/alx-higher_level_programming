#!/usr/bin/python3
"""author: Mitch"""


def inherits_from(obj, a_class):
    """a function to determine if an object
    is an inherited from a class

    """
    result = issubclass(type(obj), a_class)
    return result
