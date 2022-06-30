#!/usr/bin/python3
"""a class square that defines a square by:
    (based on 0-square.py)

    """


class Square:
    """square class with a private attribute -
    size.

    """

    def __init__(self, size=0):
        """initializes size attribute as a private
        instance variable

        Args:
            __size (int): the __size of the new square.

        """
        self.__size = size

    @property
    def size(self):
        """get the size of the square"""
        return self.__size

    @size.setter
    def size(self, size_value):
        """get the size of the square"""
        self.__size = size_value

        if not isinstance(size_value, int):
            raise TypeError("size must be an integer")
        elif size_value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns the current
        square area

        """
        return (self.__size ** 2)
