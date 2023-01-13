#!/usr/bin/python3
"""author: Mitch"""


def is_same_class(obj, a_class):
    """a function to determine if an object
    is a method of a class

    """
    result = type(obj) is a_class
    return result
