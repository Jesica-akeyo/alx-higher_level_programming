#!/usr/bin/python3
"""
This module contains class: BaseGeometry
"""


class BaseGeometry:
    """ public instance method """
    def area(self):
        """ raises exception error with msg """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value """
        if type(value) is not int:
            raise TypeError("{} must be an integer")
        if value <= 0:
            raise ValueError("{} must be greater than 0")
