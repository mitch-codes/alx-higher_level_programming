#!/usr/bin/python3
"""inherit a class"""
from models.base import Base


class Rectangle(Base):
    """class to define rectangle

    Args:
        Base(model): the inherited class

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """set attributes

        Args:
            width(int): value of width
            height(int): value of height
            x(int): x value
            y(int): y value
            id(int): the id

        """

        super().__init__(id)

        if isinstance(width, int) is not True:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

        if isinstance(height, int) is not True:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

        if isinstance(x, int) is not True:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        if isinstance(y, int) is not True:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def width(self):
        """getter returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter gets width

        Args:
            value(int): value of width

        """
        if isinstance(value, int) is not True:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter returns width"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter sets width

        Args:
            value(int): value of height

        """
        if isinstance(value, int) is not True:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter returns width"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter gets widt

        Args:
            value(int): x value

        """
        if isinstance(value, int) is not True:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter returns width"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter gets width

        Args:
            value(int): y value

        """
        if isinstance(value, int) is not True:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """display the rectangle graphically"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for i in range(self.__x):
                print(" ", end="")
            for i in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """overide str method"""
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x,
                    self.__y, self.__width, self.__height)

    def update(self, *args):
        """update class attributes

        Args:
            args: atguments to be passed

        """
        listatr = []
        for arg in args:
            listatr.append(arg)
        if listatr[0] is not None:
            super().__init__(listatr[0])
        if listatr[1] is not None:
            self.__width = listatr[1]
        if listatr[2] is not None:
            self.__height = listatr[2]
        if listatr[3] is not None:
            self.__x = listatr[3]
        if listatr[4] is not None:
            self.__y = listatr[4]
