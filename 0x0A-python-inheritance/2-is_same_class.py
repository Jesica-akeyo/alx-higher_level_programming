#!/usr/bin/python3
"""
This module contains the function: is_same_class
"""


def is_same_class(obj, a_class):
    """
    True if obj is exactly an instance of a_class
    False, otherwise
    """
    return type(obj) is a_class
