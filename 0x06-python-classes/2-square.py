#!/usr/bin/python3
"""a class square that defines a square by:
    (based on 0-square.py)

    """


class Square:
    """square class with a private attribute -
    size.

    """

    def __init__(self, size = 0):
        """initializes size attribute as a private
        instance variable

        Args:
            __size (int): the __size of the new square.

        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
