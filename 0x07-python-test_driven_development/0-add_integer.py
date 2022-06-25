#!/usr/bin/python3
"""
this module has a function that adds two numbers
"""


def add_integer(a, b=98):
    """
    Function that adds two integers or floats
   Args:
       a: first number
       b: second number
   Raises:
       TypeError if a or b aren't integers and/or floats
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
