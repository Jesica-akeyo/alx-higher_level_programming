#!/usr/bin/python3
""" class Rectangle that defines a rectangle """


class Rectangle:
    def __init__(self, width=0, height=0):
        """
        __init__ method
        width: integer rectangle width
        height: integer rectangle height
        Raises:
            TypeError if width and height arent integers
            ValueError if width and height are less than 0
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """ getter for width """
            return self.__width

        @width.setter
        def width(self, value):
            """ setter for width """
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """ getter for height """
            return self.__height

        @height.setter
        def height(self, value):
            """ setter for height """
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError(" height must be >= 0")
            self.__height = value
