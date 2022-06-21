#!/usr/bin/python3
""" Module Square """


class Square:
    """
    defines a square by size(private instance attribute)
    size must be an integer and must not be negative
    """
    def __init__(self, size=0):
        """ __init__ method """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        self.__size = size
