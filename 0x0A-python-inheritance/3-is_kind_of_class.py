#!/usr/bin/python3
"""
This module has the function: is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    returns True if the obj is an instance of
    or if the obj is an instance of a class that inherited
    from a_class
    False, otherwise
    """
    return isinstance(obj, a_class)
