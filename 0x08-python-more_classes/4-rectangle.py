#!/usr/bin/python3
""" class Rectangle that defines a rectangle """


class Rectangle:
    """ defines a rectangle """
    def __init__(self, width=0, height=0):
        """ __init__ method
        width: rectangle width
        height: retcatngle height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ returns value of width """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter
        raises:
            TypeError: if width is not an integer
            ValueError: if width is < 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ returns the value of height """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter
        raises:
            TypeError: if height is not an integer
            ValueError: if height is < 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ method that calculates the area of the rectangle """
        return self.width * self.height

    def perimeter(self):
        """ method that calculates the perimeter of the rectangle """
        if self.width == 0 or self.height == 0:
            return 0

        return 2 * (self.width + self.height)

    def __str__(self):
        """ returns the string representation of the rectangle using # """
        rectangle = ""

        if self.width == 0 or self.height == 0:
            return rectangle

        for i in range(self.height):
            rectangle += ("#" * self.width + "\n")
        return rectangle[:-1]

    def __repr__(self):
        """ returns the object funstion rep of rectangle """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)
