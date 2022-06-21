#!/usr/bin/python3
""" Module Square """


class Square:
    """ defines a square by a private instance attribute:
    size """
    def __init__(self, size=0):
        """ initializes square objects """
        self.__size = size
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
