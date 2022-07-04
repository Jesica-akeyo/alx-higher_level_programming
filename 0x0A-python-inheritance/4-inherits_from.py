#!/usr/bin/python3
"""
This module contains the function: inherits_from
"""


def inherits_from(obj, a_class):
    """
    returns True if obj is an instance of aclass that
    inherited (directly/indirectly) from a_class
    otherwise False
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
