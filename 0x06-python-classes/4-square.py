#!/usr/bin/python3
""" module Square """


class Square:
    """ defines a square by private instance attribute: size """
    def __init__(self, size=0):
        """
        initializes square objects,
        size must be an integer and must be greater than 0
        """
        self.__size = size
    @property
    def size(self):
        """
        gets value of __size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        sets value of __size
        """
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ instance method that returns the current square area """
        return (self.__size) ** 2
