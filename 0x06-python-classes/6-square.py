#!/usr/bin/python3
""" module Square """


class Square:
    def __init__(self, size=0, position=(0, 0)):
        """ sets the size and position of square,
        size (int): size of square
        position (tuple): position of Square
        """
        self.size = size
        self.position = position

    def area(self):
        """ returns the current square area """
        return (self.__size) ** 2

    @property
    def size(self):
        """ gets the size of square """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets the size of square """
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ gets position of square """
        return self.__postion

    @position.setter
    def position(self, value):
        """
        sets position of Square
        position must be a tuple of 2 positive integers
        otherwise raise TypeError
        """
        if isinstance(value, tuple) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """
        prints in stdout the square with the character #
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print("")
            for j in range(self.__size):
                print("{}{}".format(" " * self.__position[0], "#" * self.__size))
