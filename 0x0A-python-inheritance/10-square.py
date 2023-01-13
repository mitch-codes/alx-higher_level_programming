#!/usr/bin/python3
"""author: Mitch"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    "an inheritence of class rectangle"

    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return (self.__size * self.__size)
