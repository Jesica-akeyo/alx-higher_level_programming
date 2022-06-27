#!/usr/bin/python3
""" class Rectangle that defines a rectangle """


class Rectangle:
    """ class that defines a rectangle """
    def __init__(self, width=0, height=0):
        """
        __init method
        width: rectangular width
        height: rectangular height
        Raises:
            TypeError if width and height aren't integers
            ValueError if width and height < 0
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
            ValueError: if width is less than zero
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ returns value of height """

        return self.__height

    @height.setter
    def height(self, value):
        """ height setter
        raises:
            TypeError: if height is not an integer
            ValueError: if height is less than zero
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Method that calculates the Rectangle area """

        return self.width * self.height

    def perimeter(self):
        """ Method that calculates the Rectangle perimeter """

        if self.width == 0 or self.height == 0:
            return 0

        return 2 * (self.width + self.height)
