#!/usr/bin/python3
"""creating python package"""


class Base():
    """create class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """alter id"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects
