#!/usr/bin/python3
"""a class square that initializes instance variables"""


class Square:
    """square class with a private attribute -
    size.
    """
    __size
    def __init__(self, size):
        """initializes size attribute as a private instance variable"""
        self.__size = size
