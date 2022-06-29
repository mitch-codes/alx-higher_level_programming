#!/usr/bin/python3
"""a class square that defines a square by:
    (based on 0-square.py)

    """


class Square:
    """square class with a private attribute -
    size.

    """
    __size
    def __init__(self, size):
        """initializes size attribute as a private instance variable"""
        self.__size = size
