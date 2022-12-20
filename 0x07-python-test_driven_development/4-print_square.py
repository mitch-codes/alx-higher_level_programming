#!/usr/bin/python3
"""Printing square"""


def print_square(size):
    """Prints a square with the character '#'"""
    if isinstance(size, (int, float)) is False:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    size = int(size)
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("\n", end="")
