#!/usr/bin/python3
"""author: Mitch"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    "an inheritence of class rectangle"

    def __init__(self, size):
        BaseGeometry.integer_validator(self, "size", size) 
        self.__size = size
        print (self.__size)

    def __str__(self):
        return ("[{}] {}/{}"
        .format(self.__class__.__name__, self.__size, self.__size))

    def area(self):
        return (self.__size * self.__size)
