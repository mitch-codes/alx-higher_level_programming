#!/usr/bin/python3
"""author: Mitch"""

from 7-base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    "an inheritence of Base Geometry"
    
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", width)
        self.__width = width
        self.__height = width
