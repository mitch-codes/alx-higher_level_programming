#!/usr/bin/python3
"""a module that adds numbers"""


def add(x, y):
    """adds two numbers"""

    return x + y

def devide(x, y):
    """devides two numbers"""

    if y == 0:
        raise ValueError("cannot devide with 0")
    return x / y
