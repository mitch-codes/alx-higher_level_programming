#!/usr/bin/python3
"""author: Mitch"""


class BaseGeometry():
    """ class raising type and value errors"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if (type(value) is not int):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
