#!/usr/bin/python3
""" module Square """


class Square:
    """
    defines a square by private instance attribute: size
    """
    def __init__(self, size=0):
        """
        initializes Square objects,
        size must be an integer and greater than 0
        """
        self.__size = size

    @property
    def size(self):
        """ gets the value of __size """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets the value of __size """
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError(" size must be >= 0")
        self.__size = value

    def area(self):
        """
        instance method that returns the current square area
        """
        return (self.__size) ** 2

    def my_print(self):
        """
        instance method that prints in stdout the square with the character #
        """
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")

