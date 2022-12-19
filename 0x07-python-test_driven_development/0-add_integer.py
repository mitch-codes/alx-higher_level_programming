#!/usr/bin/python3
"""Integers addition"""


def add_integer(a, b=98):
    """Adds two numbers
    Args:
        a - first number input
        b - second number input

    """
    if (isinstance(a, (int, float)) is False):
        raise TypeError("a must be an integer")
    if (isinstance(b, (int, float)) is False):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
